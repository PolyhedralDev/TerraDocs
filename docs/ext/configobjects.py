import rstutils as rst
import warnings
import re
from operator import itemgetter

from yamlutils import *

def addon_text(addon_name: str, thing: str) -> list[str]:
    lines = []
    if addon_name != "base":
        require_text = "require" if thing.endswith("s") else "requires"
        lines.append(f":superscript:`*{thing} {require_text} the '{addon_name}' addon to use`")
    return lines

def merge_abstract_params(raw_templates, template_key, visited=None):
    # Ensure extensions follow a DAG
    if visited is None:
        visited = set()
    if template_key in visited:
        raise ValueError("Recursion detected")
    visited.add(template_key)

    template = ensure_dict(raw_templates.get(template_key))
    parameters = template.get("params", {}) 

    if "extends" in template: # Merge in parameters from parent if present
        parent_key = template["extends"]
        parameters = merge_abstract_params(raw_templates, parent_key, visited) | parameters

    return parameters

def resolve_abstract_templates(raw_templates):
    return {
        template_key: ensure_dict(template) | { "params": merge_abstract_params(raw_templates, template_key) }
        for (template_key, template)
        in raw_templates.items()
        if not ensure_dict(template).get("abstract", False)
    }

class RegistryKey:
    def __init__(self, addon, key):
        self.addon = addon
        self.key = key

    def __str__(self):
        return self.addon + ":" + self.key
    
type_expression_regex = r'\w+'

def map_types(type_expression, objects):
    def map_to_link_if_present(match):
        type_string = match.group(0)
        if type_string not in objects:
            return type_string
        return f":doc:`/config/documentation/objects/{type_string}`"
    unescaped = re.sub(type_expression_regex, map_to_link_if_present, type_expression)
    return re.sub(r'(:doc:`[\w/]+`)(\S)', lambda match: match.group(1) + "\\" + match.group(2), unescaped) # Escape any non whitespace characters following the :doc: role
    
class Parameter:
    def __init__(self, name, yaml, template, objects):
        self.value_type = yaml["type"]
        self.summary = "- " + yaml["summary"] if "summary" in yaml else ""
        self.description = yaml.get("description")
        self.default_value = yaml.get("default")
        self.inline_types = set(yaml.get("inline-types", []))
        self.name = name
        self.template = template
        for match in re.finditer(type_expression_regex, self.value_type):
            type_string = match.group(0)
            if type_string in objects:
                objects[type_string].add_reference(self)
            
    def ref_name(self) -> str:
        return f"parameter-{str(self.template.__hash__())}-{self.name}"
    
    def badge(self) -> str:
        badge_role = ":bdg-primary:" if self.is_required() else ":bdg-success:"
        return f"{badge_role}`{self.name}`"
    
    def ref_badge(self) -> str:
        badge_role = ":bdg-ref-primary:" if self.is_required() else ":bdg-ref-success:"
        return f"{badge_role}`{self.name} <{self.ref_name()}>`"
    
    def summary_line(self, objects) -> str:
        return f"{self.badge()} {map_types(self.value_type, objects)} {self.summary}"
    
    def to_rst_lines(self, objects) -> list[str]:
        strings = [f".. _{self.ref_name()}:", self.summary_line(objects)]

        if not self.is_required():
            strings.append(f"Default: ``{self.default_value}``")

        if self.description is not None:
            strings.append(self.description)

        for inline_type in self.inline_types:
            if inline_type not in objects:
                warnings.warn(f"Parameter '{self.name}' references undocumented object '{inline_type}' for inline documentation")
            else:
                strings += rst.wrap_in_card(objects[inline_type].to_rst_lines(inline_type, objects, include_heading=False), title=inline_type, link=inline_type, link_type="doc")

        return strings

    def is_required(self) -> bool:
        return self.default_value is None

def sort_params(params: dict[str, Parameter]) -> dict[str, Parameter]:
    sorted_params = sorted(params.items(), key=itemgetter(0)) # Sort alphabetically
    sorted_params = sorted(sorted_params, key=lambda pair: pair[1].is_required(), reverse=True) # Put required params first
    return dict(sorted_params)

class Template:
    def __init__(self, yaml, addon, parent, objects, name=None):
        self.name = name
        self.description = yaml.get("description")
        self.parameters = { param_key: Parameter(param_key, param, self, objects) for (param_key, param) in ensure_dict(yaml.get("params")).items() }
        self.footer = yaml.get("footer")
        self.addon = addon
        self.parent = parent

    def to_rst_lines(self, objects) -> list[str]:
        strings = []
        if self.description:
            strings.append(self.description)
        if self.parameters:
            for param_name, param in sort_params(self.parameters).items():
                strings += param.to_rst_lines(objects)
        if self.footer:
            strings.append(self.footer)
        return strings

class ObjectType:

    def __init__(self, name, description, addon):
        self.name = name
        self.description = description
        self.addon = addon
        self.references = set()

    def header_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = []
        if include_heading:
            lines.append(rst.h1(object_name))
        lines += addon_text(self.addon, "Config object")
        if self.description:
            lines.append(self.description)
        return lines
    
    def footer_rst_lines(self, objects) -> list[str]:
        lines = [rst.h2("Uses")]
        match len(self.references):
            case 0:
                lines.append("This object is not referenced by any parameters")
            case 1:
                lines.append("This object is used in one place:")
            case _:
                lines.append(f"Used by {len(self.references)} parameters:")
        for parameter in self.references:
            context = "In "
            if parameter.template.name:
                context += f"{parameter.template.name} in "
            context += parameter.template.parent.name
            lines += rst.bullet_lines([
                rst.ref(parameter.ref_name(), context) + ":",
                parameter.summary_line(objects)
            ])
        return lines

    def add_reference(self, reference: Parameter):
        self.references.add(reference)
        
    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = self.header_rst_lines(object_name, objects, include_heading)
        lines += self.footer_rst_lines(objects)
        return lines

class MultiType(ObjectType):
    def __init__(self, name, yaml, addon: str, objects):
        super().__init__(name=name, description=yaml.get("description"), addon=addon)
        documented_types = yaml.get("types", {})
        object_types = {}
        if "map" in documented_types:
            object_types["map"] = Template(documented_types["map"], addon, self, objects)
        if "int" in documented_types:
            object_types["int"] = documented_types["int"]["description"] # Unsafe, assumes 'description' is defined
        self.types = object_types

    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = super().header_rst_lines(object_name, objects)
        if "int" in self.types:
            lines.append(self.types["int"])
        if "map" in self.types:
            lines += self.types["map"].to_rst_lines(objects)
        lines += super().footer_rst_lines(objects)
        return lines

class Templated(ObjectType):
    def __init__(self, name, yaml, addon: str, objects):
        super().__init__(name=name, description=yaml.get("description"), addon=addon)
        self.templates: dict[RegistryKey, Template] = {} 

    def add_templates(self, templates: dict[RegistryKey, Template]):
        self.templates.update(templates)

    def to_rst_lines(self, object_name, objects, include_heading: bool=True) -> list[str]:
        lines = super().header_rst_lines(object_name, objects, include_heading)
        lines += [
            rst.h2("Types"), 
            f"Different types of ``{object_name}`` provide different behaviours and may have additional parameters for configuring that behavior.",
            "The type is specified by setting the :bdg-primary:`type` parameter to the name of the type. If the same name is used by two different addons, you can prefix the name with ``ADDON_NAME:`` to specify which one to use.",
            f"A list of available types for ``{object_name}`` are listed below:"
        ]
        for template_regkey, template in self.templates.items():
            lines += [rst.sep, rst.h3(template_regkey.key)]
            if template.addon is not self.addon:
                lines += addon_text(template_regkey.addon, "Type")
            lines += template.to_rst_lines(objects)
        lines += super().footer_rst_lines(objects)
        return lines

class Primitive(ObjectType):
    def __init__(self, name, yaml, addon: str, objects):
        super().__init__(name=name, description=yaml.get("description"), addon=addon)

class RegistryKeyObjectType(ObjectType):
    def __init__(self, name, yaml, addon: str, objects):
        super().__init__(name=name, description=yaml.get("description"), addon=addon)

type_keys = {
    "MULTI_TYPE": MultiType,
    "TEMPLATED": Templated,
    "PRIMITIVE": Primitive,
    "REGISTRY_KEY": RegistryKeyObjectType,
}

class ConfigType():
    def __init__(self, name, yaml, addon, objects):
        yaml = ensure_dict(yaml)
        self.description = yaml.get("description")
        self.addon = addon
        self.templates = {}
        self.registers = yaml.get("registers")
        self.use_global_template = yaml.get("use-global-template", True)
        self.objects = objects
        self.name = name

    def add_templates(self, templates: dict[RegistryKey, Template]):
        self.templates.update(templates)
        
    def to_rst_lines(self, objects, include_heading: bool=True) -> list[str]:
        lines = []

        if include_heading:
            lines.append(rst.h1(self.name))

        lines += addon_text(self.addon, "Config type")
        
        if self.registers:
            references_role = f":doc:`/config/documentation/objects/{self.registers}`" 
            lines.append(f"This config type creates instances of {references_role}.")

        if self.description:
            lines.append(self.description)
            
        # Sort by addon, make templates added by the config's addon first in the list
        global_templates = [] if not self.use_global_template else [
            (RegistryKey("base", "global"), Template(
            addon="base",
            yaml={
                "params": {
                    "id": {
                        "type": "String",
                        "summary": f"An identifier used to reference this config from other configs.",
                        "description": None if not self.registers else f"The instance of {references_role} created by a config using this config type is identified using this parameter."
                    },
                    "extends": {
                        "type": f"List<String>",
                        "summary": f"A list of other ``{self.name}`` configs to copy parameters from.",
                        "description": "Parameters from extended configs are only used if they have not already been defined in the current config. Configs listed first take precedence. This allows for re-use of parameters across multiple config files."
                    }
                }
            },
            parent=self,
            objects=self.objects
            )),
        ]

        sorted_templates = global_templates + sorted(self.templates.items(), key=lambda pair: (pair[0].addon != self.addon, pair[0].addon))
        for i, (template_regkey, template) in enumerate(sorted_templates):
            if i != 0:
                lines += [rst.sep]
            if template.addon is not self.addon:
                lines += addon_text(template_regkey.addon, "Parameters")
            lines += template.to_rst_lines(objects)

        return lines
