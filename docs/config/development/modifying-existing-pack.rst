==========================
Modifying an Existing Pack
==========================

This guide will outline the process of duplicating an existing Terra configuration pack for use in
personal modification. This guide will not cover how to modify specific features of world generation,
only the initial set up required to make your own modifications. If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>`
for more information before continuing.

.. card::

    If you wish to **create a pack from scratch** rather than modifying an existing one,
    please refer to the :doc:`/config/development/pack-from-scratch/index` guide instead.

.. attention::

    This guide is written for Terra version 6.0.+ and will not be applicable to prior versions!

Setting up a New Pack
=====================

`PROCEDURE`

1. Find a suitable pack for your version.
-----------------------------------------

.. card::

    If you wish to modify the default pack that comes preinstalled with Terra, you can find it in the 
    :ref:`packs directory <packs-directory>`. You can find the source for the default pack over at the
    `Overworld`_ repository.

    For other available packs, refer to the :doc:`/config/community-packs` page. Be sure to check that the
    pack you wish to modify is compatible with your version of Terra before proceeding.

1. Create your config pack directory
------------------------------------

.. card::

    Navigate to your :ref:`packs directory <packs-directory>` and create a new folder inside, the
    name of this folder is up to you to decide. For this guide we will use ``custom-pack`` as an
    example.

    You should have the following directory structure: `Terra/packs/custom-pack`

    .. code-block::
        
        Terra/
        ├── packs/
        ┆   ├── default.zip
            └── custom-pack/ <- New folder you've just created

2. Copy the contents of the pack you wish to modify
---------------------------------------------------

.. card::

    Copy the contents of the pack you wish to modify into the new directory you created in the
    previous step. If the pack you're modifying has been distributed as a ``.zip`` file, extract
    the contents into your new directory.

    .. admonition:: Modifying the default pack
        :class: tip

        If you wish to make modifications to the default pack, extract the contents of ``default.zip``
        into your new folder.

    .. tip::

        Packs can be loaded from both folders and ``.zip`` archives, so you **do not** have to re-zip
        a pack in order for it to load.

    If you have correctly copied the contents over, the pack manifest aka ``pack.yml`` should be directly
    inside your new pack directory like so:
    
    :bdg-success:`CORRECT` - `Terra/packs/custom-pack/pack.yml`
    
    .. code-block::
        
        Terra/
        ├── packs/
        ┆   ├── default.zip
            └── custom-pack/
                ├── pack.yml
                ┆

    :bdg-danger:`INCORRECT` - `Terra/packs/custom-pack/folder/pack.yml`

    .. code-block::
        
        Terra/
        ├── packs/
        ┆   ├── default.zip
            └── custom-pack/
                └── folder/
                    ├── pack.yml
                    ┆

    :bdg-danger:`INCORRECT` - `Terra/packs/custom-pack/original-pack.zip`

    .. code-block::
        
        Terra/
        ├── packs/
        ┆   ├── default.zip
            └── custom-pack/
                └── original-pack.zip

    :bdg-danger:`INCORRECT` - `Terra/packs/pack.yml`

    .. code-block::
        
        Terra/
        ├── packs/
        ┆   ├── default.zip
            ├── pack.yml
            ┆

    .. warning::

        Any folder or zip contained within the packs directory will attempt to load as a config pack.
        Do not leave any folders or zips you do not intend to load as packs within the packs directory.

3. Set a custom ID for your new pack
------------------------------------

.. card::

    #. Open ``pack.yml`` contained in your pack folder.

    #. Locate the line that begins with ``id:``.

    #. Replace the id specified after ``id:`` with an ID of your choice. We will use ``CUSTOM`` as an example.

    Pack IDs must only contain uppercase alphanumeric characters ``A-Z`` ``0-9``, and underscores ``_``.

    :bdg-success:`VALID`
    
    .. code-block:: yaml
        :caption: pack.yml

        id: CUSTOM

    :bdg-danger:`INVALID`

    .. code-block:: yaml
        :caption: pack.yml

        id: custom id

4. Verify the pack loads
------------------------

.. card::

    Start up your client / server and look for your new custom pack ID in :ref:`console <Console>`.
    If you see:

    .. code-block::

        [XX:XX:XX INFO]: [Terra] Loading config pack "CUSTOM"
        [XX:XX:XX INFO]: [Terra] CUSTOM <PACK VERSION> by <AUTHOR> loaded in XXXX.XXXXms.

    Then your pack should be ready for making modifications!

.. _Overworld: https://www.github.com/PolyhedralDev/TerraOverworldConfig
