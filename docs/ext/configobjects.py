import rstutils as rst
import warnings
import re

from yamlutils import *

def addon_text(addon_name: str, thing: str) -> list[str]:
    lines = []
    if addon_name != "base":
        lines.append(f":superscript:`*{thing} requires the '{addon_name}' addon to use`")
    return lines

def merge_abstract_params(raw_templates, template_name, visited=None):
    # Ensure extensions follow a DAG
    if visited is None:
        visited = set()
    if template_name in visited:
        raise ValueError("Recursion detected")
    visited.add(template_name)

    template = ensure_dict(raw_templates.get(template_name))
    parameters = template.get("params", {}) 

    if "extends" in template: # Merge in parameters from parent if present
        parent_key = template["extends"]
        parameters = merge_abstract_params(raw_templates, parent_key, visited) | parameters

    return parameters

def resolve_abstract_templates(raw_templates):
    return {
        template_name: ensure_dict(template) | { "params": merge_abstract_params(raw_templates, template_name) }
        for (template_name, template)
        in raw_templates.items()
        if not ensure_dict(template).get("abstract", False)
    }

class RegistryKey:
    def __init__(self, addon, key):
        self.addon = addon
        self.key = key

    def __str__(self):
        return self.addon + ":" + self.key

class Parameter:
    def __init__(self, yaml, addon):
        self.value_type = yaml["type"]
        self.summary = "- " + yaml["summary"] if "summary" in yaml else ""
        self.description = yaml.get("description")
        self.default_value = yaml.get("default")
        self.inline_types = set(yaml.get("inline-types", []))
        self.addon = addon

    def to_rst_lines(self, name, objects, include_addon: bool=False) -> list[str]:
        required = self.default_value is None
        badge_role = ":bdg-primary:" if required else ":bdg-success:"

        def map_types(type_expression):
            def map_to_link_if_present(match):
                type_string = match.group(0)
                if type_string not in objects:
                    warnings.warn(f"Parameter '{name}' is set to undocumented object '{type_string}'")
                    return type_string
                return f":doc:`/config/documentation/objects/{type_string}`\\"
            unescaped = re.sub(r'\w+', map_to_link_if_present, type_expression)
            return re.sub(r'(`\w+`)(\S)', lambda match: match.group(1) + "\\" + match.group(2), unescaped) # Escape any non whitespace characters following the :doc: role TODO BROKEN

        strings = [f"{badge_role}`{name}` {map_types(self.value_type)} {self.summary}"]

        if include_addon:
            strings += addon_text(self.addon, "Parameter")

        if not required:
            strings.append(f"Default: ``{self.default_value}``")

        if self.description is not None:
            strings.append(self.description)

        for inline_type in self.inline_types:
            if inline_type not in objects:
                warnings.warn(f"Parameter '{name}' references undocumented object '{inline_type}' for inline documentation")
            else:
                strings += rst.wrap_in_card(objects[inline_type].to_rst_lines(inline_type, objects, include_heading=False), title=inline_type, link=inline_type, link_type="doc")

        return strings

class Template:
    def __init__(self, yaml, addon):
        self.description = yaml.get("description")
        self.parameters = { param_key: Parameter(param, addon) for (param_key, param) in ensure_dict(yaml.get("params")).items() }
        self.footer = yaml.get("footer")
        self.addon = addon

    def to_rst_lines(self, objects) -> list[str]:
        strings = []
        if self.description:
            strings.append(self.description)
        if self.parameters:
            for param_name, param in self.parameters.items():
                strings += param.to_rst_lines(param_name, objects)
        if self.footer:
            strings.append(self.footer)
        return strings

class ObjectType:

    def __init__(self, description, addon):
        self.description = description
        self.addon = addon

    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = []
        if include_heading:
            lines.append(rst.h1(object_name))
        lines += addon_text(self.addon, "Config object")
        if self.description:
            lines.append(self.description)
        return lines

class MultiType(ObjectType):
    def __init__(self, yaml, addon: str):
        super().__init__(description=yaml.get("description"), addon=addon)
        documented_types = yaml.get("types", {})
        object_types = {}
        if "map" in documented_types:
            object_types["map"] = Template(documented_types["map"], addon)
        if "int" in documented_types:
            object_types["int"] = documented_types["int"]["description"] # Unsafe, assumes 'description' is defined
        self.types = object_types;

    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = super().to_rst_lines(object_name, objects)
        if "int" in self.types:
            lines.append(self.types["int"])
        if "map" in self.types:
            lines += self.types["map"].to_rst_lines(objects)
        return lines

class Templated(ObjectType):
    def __init__(self, yaml, addon: str):
        self.templates = {} 
        super().__init__(yaml.get("description"), addon=addon)

    def add_templates(self, templates: dict[RegistryKey, Template]):
        self.templates.update(templates)

    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = super().to_rst_lines(object_name, objects, include_heading)
        lines += [
            rst.h2("Types"), 
            f"Different types of ``{object_name}`` provide different behaviours and may have additional parameters for configuring that behavior.",
            "The type is specified by setting the :bdg-primary:`type` parameter to the name of the type. If the same name is used by two different addons, you can prefix the name with ``ADDON_NAME:`` to specify which one to use.",
            f"A list of available types for ``{object_name}`` are listed below:"
        ]
        for template_regkey, template in self.templates.items():
            lines += ["---------", rst.h3(template_regkey.key)]
            if template.addon is not self.addon:
                lines += addon_text(template_regkey.addon, "Type")
            lines += template.to_rst_lines(objects)
        return lines

class Primitive(ObjectType):
    def __init__(self, yaml, addon: str):
        super().__init__(yaml.get("description"), addon=addon)

    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        return super().to_rst_lines(object_name, objects, include_heading)

type_keys = {
    "MULTI_TYPE": MultiType,
    "TEMPLATED": Templated,
    "PRIMITIVE": Primitive,
}

class ConfigType():
    def __init__(self, yaml, addon):
        yaml = ensure_dict(yaml)
        self.description = yaml.get("description")
        self.addon = addon
        self.params = {} 

    def add_params(self, params):
        self.params.update(params)

    def to_rst_lines(self, config_name, objects, include_heading: bool=True) -> list[str]:
        lines = []
        if include_heading:
            lines.append(rst.h1(config_name))
        lines += addon_text(self.addon, "Config type")
        if self.description:
            lines.append(self.description)
        for param_name, param in self.params.items():
            lines += param.to_rst_lines(param_name, objects, include_addon=param.addon is not self.addon)
        return lines

