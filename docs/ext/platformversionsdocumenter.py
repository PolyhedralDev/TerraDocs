from pathlib import Path
import os
import sys
import yaml
import rstutils as rst
from urllib.parse import urlparse

version_stages = {
    "BETA": ":bdg-warning:`Beta`",
    "ALPHA": ":bdg-danger:`Alpha`",
    "DEVELOPMENT": ":bdg-secondary:`In Development`",
}

yes = ":bdg-success:`Yes`"
no = ":bdg-danger:`No`"

def setup(app):
    ver_dir = os.path.join(app.srcdir, 'install')
    ver_doc  = os.path.join(ver_dir, 'versions.yml')
    output_doc = os.path.join(ver_dir, 'versions.rst')
    output_vers_dir = os.path.join(ver_dir, 'versions/platforms')

    with open(ver_doc, 'r') as file:
        vers_yaml = yaml.safe_load(file)

    output_rst = ["""========
Versions
========

.. toctree::
    :glob:
    :hidden:

    versions/platforms/*/*

On this page you can find the latest releases of Terra for each platform & Minecraft version.

.. warning::

    \*Releases labelled :bdg-secondary:`In Development` are strictly available for previewing and development only.
    You should not use any of these releases in production as they may be unstable and subject to changes."""]

    for platform_name, platform_description in vers_yaml.items():
        output_rst.append(f".. _{platform_name}-versions:")
        output_rst.append(rst.h2(platform_name))
        if "description" in platform_description:
            output_rst.append(platform_description["description"])

        if "versions" in platform_description:
            versions = platform_description["versions"]

            output_rst.append(""".. list-table::
    :header-rows: 1
    
    *
        - Minecraft Version [1]_
        - Latest Terra Version [2]_
        - Supported [3]_
        - Maintained [4]_
        - Download [5]_
        - Backwards Compatibility [6]_""")

            for version in versions:
                mc_ver = version["mc-ver"]
                terra_ver = version["terra-ver"]
                stage = version_stages.get(version["stage"], "")
                terra_ver_formatted = f"{terra_ver} {stage}"

                supported = version.get("supported", False)
                supported_badge = yes if supported else no

                maintained = version.get("maintained", False)
                maintained_badge = yes if maintained else no

                legacy = version.get("legacy", False)

                link = version["link"]
                link_domain = urlparse(link).netloc

                if legacy or not supported:
                    platform_dir = os.path.join(output_vers_dir, platform_name)
                    Path(platform_dir).mkdir(parents=True, exist_ok=True)
                    ver_file = os.path.join(platform_dir, f"{terra_ver}.rst")

                    ver_output_rst = [rst.h1(f"{platform_name} Legacy {terra_ver}" if legacy else f"{platform_name} {terra_ver}")]

                    if not supported:
                        ver_output_rst.append(".. include:: ../../unsupported.rst")

                    ver_output_rst.append(f":bdg-primary:`Download` - {link}")
                    
                    if legacy:
                        ver_output_rst.append(".. include:: ../../5.x-wiki.rst")

                    ver_output_rst.append(f":ref:`Other {platform_name} versions <{platform_name}-versions>` :octicon:`chevron-right`")

                    with open(ver_file, 'w') as file:
                        file.write("\n\n".join(ver_output_rst))

                    link_formatted = f":doc:`{link_domain} <versions/platforms/{platform_name}/{terra_ver}>`"
                else:
                    link_formatted = f"`{link_domain} <{link}>`__"

                output_rst.append(f"""    *
        - **{mc_ver}**
        - {terra_ver_formatted}
        - {supported_badge}
        - {maintained_badge}
        - {link_formatted}
        - N/A""")

    output_rst.append("""Definitions
===========

.. [1] **Minecraft Version** - The vanilla Minecraft version for the relevant platform.

.. [2] **Latest Terra Version** - The latest Terra version supporting the corresponding Minecraft version.  

.. [3] **Supported** - Whether or not you will receive official support for using the release.

.. [4] **Maintained** - Whether or not new Terra releases will be developed for the corresponding Minecraft version.

.. [5] **Download** - Downloads for the latest Terra version for the corresponding Minecraft version.

.. [6] **Backwards Compatibility** - Some releases of Terra are backwards compatible with older versions of Minecraft, the oldest of which is listed under this column. This however does not guarantee backwards compatibility of config packs shipped with the release.""")

    with open(output_doc, 'w') as file:
        file.write("\n\n".join(output_rst))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
