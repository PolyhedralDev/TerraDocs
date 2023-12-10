from pathlib import Path
import os
import sys
import yaml
import rstutils as rst
from configobjects import *

def setup(app):
    doc_dir = os.path.join(app.srcdir, 'config/documentation')
    addons_dir = os.path.join(doc_dir, 'addons')
    output_dir = os.path.join(doc_dir, 'objects')
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    addons = {}

    for filename in os.listdir(addons_dir):
        file = os.path.join(addons_dir, filename)
        if not filename.endswith(".yml") or not os.path.isfile(file):
            continue
        with open(file, 'r') as file:
            for addon_name, addon in yaml.safe_load(file).items():
                if addon_name in addons:
                    raise ValueError(f"Addon {addon_name} is defined multiple times across multiple files")
                addons[addon_name] = addon

    objects = {}

    # Create objects
    for addon_name, addon in addons.items():
        for object_name, object_description in addon.get("objects", {}).items():
            if object_name in objects:
                raise ValueError(f"Multiple addons define a description for object {object_name}")
            object_type = object_description.get("type")
            objects[object_name] = type_keys[object_type](object_description)

    # Add templates to templated objects
    for addon_name, addon in addons.items():
        for object_name, templates in addon.get("templates", {}).items(): 
            if object_name not in objects:
                continue
            objects[object_name].templates.update(convert_yaml_template_set(addon_name, templates))

    # Write objects into rst files
    for object_name, object_description in objects.items():
        output_rst = [rst.h1(object_name)]
        output_rst += object_description.to_rst_lines(object_name, objects)
        output_file = os.path.join(output_dir, object_name + '.rst')
        with open(output_file, 'w') as file:
            file.write("\n\n".join(output_rst))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
