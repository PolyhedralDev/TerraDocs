import rstutils as rst
import warnings
import re

def convert_yaml_template_set(addon_name, raw_templates):
    return {
        RegistryKey(addon_name, template_name): Template(
            parameters={
                param_key: Parameter(param_info)
                for (param_key, param_info)
                in resolve_extensions(raw_templates, template_name).items()
            },
            description=template.get("description"),
            footer=template.get("footer"),
        )
        for (template_name,template)
        in raw_templates.items()
        if not template.get("abstract", False)
    }

class RegistryKey:
    def __init__(self, addon, key):
        self.addon = addon
        self.key = key

    def __str__(self):
        return self.addon + ":" + self.key

class Parameter:
    def __init__(self, yaml):
        self.value_type = yaml["type"]
        self.summary = "- " + yaml["summary"] if "summary" in yaml else ""
        self.description = yaml.get("description")
        self.default_value = yaml.get("default")
        self.inline_types = set(yaml.get("inline-types", []))

    def to_rst_lines(self, name, objects) -> list[str]:
        required = self.default_value is None
        badge_role = ":bdg-primary:" if required else ":bdg-success:"

        def map_types(type_expression):
            def map_to_link_if_present(match):
                type_string = match.group(0)
                if type_string not in objects:
                    warnings.warn(f"Parameter '{name}' is set to undocumented object '{type_string}'")
                    return type_string
                return f":doc:`{type_string}`"
            unescaped = re.sub(r'\w+', map_to_link_if_present, type_expression)
            return re.sub(r'(`\w+`)(\S)', lambda match: match.group(1) + "\\" + match.group(2), unescaped) # Escape any non whitespace characters following the :doc: role

        strings = [f"{badge_role}`{name}` {map_types(self.value_type)} {self.summary}"]

        if not required:
            strings.append(f"Default: ``{self.default_value}``")

        if self.description is not None:
            strings.append(self.description)

        for inline_type in self.inline_types:
            if inline_type not in objects:
                warnings.warn(f"Parameter '{name}' references undocumented object '{inline_type}' for inline documentation")
            else:
                strings += rst.wrap_in_card(objects[inline_type].to_rst_lines(inline_type, objects), title=inline_type, link=inline_type, link_type="doc")

        return strings

def resolve_extensions(raw_templates, template_name, visited=None):
    # Ensure extensions follow a DAG
    if visited is None:
        visited = set()
    if template_name in visited:
        raise ValueError("Recursion detected")
    visited.add(template_name)

    template = raw_templates[template_name]
    parameters = template.get("params", {}); # Unsafe, assumes params is defined

    if "extends" in template: # Merge in parameters from parent if present
        parent_key = template["extends"]
        parameters = resolve_extensions(raw_templates, parent_key, visited) | parameters

    return parameters

class Template:
    def __init__(self, parameters, description, footer):
        self.description = description
        self.parameters = parameters
        self.footer = footer

    def to_rst_lines(self, objects) -> list[str]:
        strings = []
        if self.description:
            strings.append(self.description)
        if self.parameters:
            strings.append("`PARAMETERS:`")
            for param_name, param in self.parameters.items():
                strings += param.to_rst_lines(param_name, objects)
        if self.footer:
            strings.append(self.footer)
        return strings

class ObjectType:

    def __init__(self, description):
        self.description = description

    def to_rst_lines(self, object_name, objects) -> list[str]:
        pass

class MultiType(ObjectType):
    def __init__(self, yaml):
        super().__init__(description=yaml.get("description"))
        documented_types = yaml.get("types", {})
        object_types = {}
        if "map" in documented_types:
            template = documented_types["map"]
            object_types["map"] = Template(
                parameters={
                    param_key: Parameter(param_info)
                    for (param_key, param_info)
                    in template.get("params").items()
                },
                description=template.get("description"),
                footer=template.get("footer"),
            )
        if "int" in documented_types:
            object_types["int"] = documented_types["int"]["description"] # Unsafe, assumes 'description' is defined
        self.types = object_types;

    def to_rst_lines(self, object_name, objects) -> list[str]:
        strings = []
        if self.description:
            strings.append(self.description)
        if "int" in self.types:
            strings.append(self.types["int"])
        if "map" in self.types:
            strings += self.types["map"].to_rst_lines(objects)
        return strings

class Templated(ObjectType):
    def __init__(self, yaml):
        self.templates = {} 
        super().__init__(yaml.get("description"))

    def to_rst_lines(self, object_name, objects) -> list[str]:
        strings = []
        if self.description:
            strings.append(self.description)
        strings += [
            rst.h2("Types"), 
            f"Different types of ``{object_name}`` provide different behaviours and may have additional parameters for configuring that behavior.",
            "The type is specified by setting the ``type`` parameter to the name of the type. If the same name is used by two different addons, you can prefix the name with ``ADDON_NAME:`` to specify which one to use.",
            f"A list of available types for ``{object_name}`` are listed below:"
        ]
        for template_regkey, template in self.templates.items():
            strings += ["---------", rst.h3(template_regkey.key), f":superscript:`Added by the '{template_regkey.addon}' addon`"]
            strings += template.to_rst_lines(objects)
        return strings

class Primitive(ObjectType):
    def __init__(self, yaml):
        super().__init__(yaml.get("description"))

    def to_rst_lines(self, object_name, objects) -> list[str]:
        lines = []
        if self.description:
            lines.append(self.description)
        return lines

type_keys = {
    "MULTI_TYPE": MultiType,
    "TEMPLATED": Templated,
    "PRIMITIVE": Primitive,
}

