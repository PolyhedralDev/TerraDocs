=================
Pack Installation
=================

Config packs are installed similarly to resource packs:

1. Download your config pack.
-----------------------------

.. card::

    You can find a list of available packs on the :doc:`/config/community-packs` page. 

    Before proceeding, make sure to:
    
    - Check if the pack has specific installation instructions, and follow them if so.
    
    - Check that the pack you wish to install is compatible with your version of Terra.
    
    Typically packs are distributed as ``.zip`` files, however they can be loaded from folders too.

    .. container:: nested-cards

        .. card:: Downloading From GitHub

            If you are downloading a config pack from GitHub, first check out the **README** section
            which can be found by scrolling down below the source files. This may contain additional
            important information and or instructions for the config pack.

            If the README does not contain explicit instructions on how to download and install
            the config pack then look for the **Releases** section:

            .. image:: /img/config/github-releases-section.png

            .. card:: If the GitHub repository has a releases section

                1. Navigate to it

                2. Once you're on the releases page, find the release you want to use

                3. Expand the 'Assets' drop down if it is not already expanded:

                .. image:: /img/config/github-release-assets.png

                4. Download the relevant ``.zip`` corresponding to the config pack.
                **Do not download** files labelled as 'Source code', the name of the file
                may be different and depends on what the config pack maintainer has uploaded it as.

                .. image:: /img/config/github-release-asset-config-pack.png

            .. card:: If there is no releases section

                1. Find the **Code** drop down:

                .. image:: /img/config/github-code-download.png

                2. Click **Download ZIP**:

                .. image:: /img/config/github-source-download.png

                This should download a ``.zip`` file, containing a folder.

                3. Unzip or open the ``.zip`` file using a graphical tool like 7zip or WinRAR.

                4. From the zip contents, find the folder containing ``pack.yml``. This
                will typically be the first folder directly inside the zip, but might not necessarily
                be the case. 

                For example, the pack is highlighted inside the zip file:

                .. image:: /img/config/pack-zip-file.png

                This folder is the config pack you install.

                .. note::
                  
                    If you wish to re-zip this folder to upload to a server, make sure the contents of
                    the config pack are directly inside the zip at the top level and not nested within
                    a folder like how GitHub packages source code.
    
2. Place the config pack into the packs directory.
----------------------------------------------------

.. card::

    This will differ slighly between versions:

    - Fabric - ``/config/Terra/packs``

    - Bukkit - ``/plugins/Terra/packs``

    .. tip::

        For ``Allay`` you need to edit ``world-settings.yml``

        .. code-block:: yaml
            :caption: world-settings.yml
            :linenos:

            worlds:
              world:
                enable: true
                runtime-only: false
                storage-type: LEVELDB
                overworld:
                  generator-type: TERRA
                  generator-preset: pack=<your pack id>;seed=<a number>
                nether: null
                the-end: null
            default-world: world

3. Ensure the correct directory structure.
------------------------------------------

.. card::

    Generally, packs will be set up to simply be dropped into the packs folder when they're distributed
    as a ``.zip`` file.

    If this is not the case, or the pack fails to load, ensure that the pack manifest or ``pack.yml`` is
    contained directly inside the folder / archive like so:

    :bdg-success:`CORRECT` - `Terra/packs/pack-to-be-installed/pack.yml`

    .. code-block::
    
        Terra/
        ├── packs/
        ┆   ├── default.zip
            └── pack-to-be-installed/
                ├── pack.yml
                ┆

    :bdg-danger:`INCORRECT` - `Terra/packs/pack-to-be-installed/<Folder>/pack.yml`

    .. code-block::
    
        Terra/
        ├── packs/
        ┆   ├── default.zip
            └── pack-to-be-installed/
                └── folder/
                    └── pack.yml

4. Verify the pack loads
------------------------

.. card::

    Start up your client / server and look for the pack ID in :ref:`console <Console>`.
    If you see:

    .. code-block::

        [XX:XX:XX INFO]: [Terra] Loading config pack "CUSTOM"
        [XX:XX:XX INFO]: [Terra] CUSTOM <PACK VERSION> by <AUTHOR> loaded in XXXX.XXXXms.

    Then your pack should be ready for use.
