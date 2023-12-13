from pathlib import Path
import os
import sys
import yaml
import shutil
import rstutils as rst
from configobjects import *

from yamlutils import *

def clean_dir(directory):
    path = Path(directory)
    if path.exists():
        if path.is_dir():
            shutil.rmtree(directory)
            path.mkdir()
        else:
            raise FileExistsError(f"Could not clear {path}, file not directory")
    else:
        path.mkdir(parents=True, exist_ok=True)
    return directory

def setup(app):
    doc_dir = os.path.join(app.srcdir, 'config/documentation')
    addons_dir = os.path.join(doc_dir, 'addons')

    addons = {}

    for filename in os.listdir(addons_dir):
        file = os.path.join(addons_dir, filename)
        if not filename.endswith(".yml") or not os.path.isfile(file):
            continue
        with open(file, 'r') as file:
            for addon_name, addon in ensure_dict(yaml.safe_load(file)).items():
                if addon_name in addons:
                    raise ValueError(f"Addon {addon_name} is defined multiple times across multiple files")
                addons[addon_name] = ensure_dict(addon)

    objects = {}
    configs = {}

    for addon_name, addon in addons.items():
        # Create objects
        for object_name, object_description in ensure_dict(addon.get("objects")).items():
            if object_name in objects:
                raise ValueError(f"Multiple addons define a description for object {object_name}")
            object_type = object_description.get("type")
            objects[object_name] = type_keys[object_type](object_description, addon_name)
        # Create config files
        for config_name, config_yaml in ensure_dict(addon.get("configs")).items():
            if config_name in configs:
                raise ValueError(f"Multiple addons define a description for config type {config_name}")
            configs[config_name] = ConfigType(config_yaml, addon_name)

    for addon_name, addon in addons.items():
        # Add templates to templated objects
        for object_name, templates in addon.get("templates", {}).items(): 
            if object_name not in objects:
                continue
            templates = resolve_abstract_templates(ensure_dict(templates))
            templates = { RegistryKey(addon_name, template_name): Template(template, addon_name) for (template_name, template) in templates.items() }
            objects[object_name].add_templates(templates)

        for config_name, templates in addon.get("config-templates", {}).items(): 
            if config_name not in configs:
                continue
            templates = resolve_abstract_templates(ensure_dict(templates))
            templates = { RegistryKey(addon_name, template_name): Template(template, addon_name) for (template_name, template) in templates.items() }
            for template_name, template in templates.items():
                configs[config_name].add_templates(templates)

    # Write objects into rst files
    objects_dir = clean_dir(os.path.join(doc_dir, 'objects'))
    for object_name, object_description in objects.items():
        output_file = os.path.join(objects_dir, object_name + '.rst')
        with open(output_file, 'w') as file:
            file.write("\n\n".join(object_description.to_rst_lines(object_name, objects)))

    # Write configs into rst files
    configs_dir = clean_dir(os.path.join(doc_dir, 'configs'))
    for config_name, config_description in configs.items():
        output_file = os.path.join(configs_dir, config_name + '.rst')
        with open(output_file, 'w') as file:
            file.write("\n\n".join(config_description.to_rst_lines(config_name, objects)))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
