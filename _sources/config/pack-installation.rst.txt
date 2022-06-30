=================
Pack Installation
=================

Config packs are installed similarly to resource packs, which is a fairly straight forward process:

1. Download your config pack.
-----------------------------

.. card::
    
    Typically packs are distributed as ``.zip`` files, however they can be loaded from folders too.
    You can find a list of available packs on the :doc:`/config/community-packs` page. 
    
    Before proceeding, make sure to:
    
    - Check if the pack has specific installation instructions, and follow them if so.
    
    - Check that the pack you wish to install is compatible with your version of Terra.

2. Place the config pack into the packs directory.
----------------------------------------------------

.. card::

    This will differ slighly between versions:

    - Fabric - ``/config/Terra/packs``

    - Bukkit - ``/plugins/Terra/packs``

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
