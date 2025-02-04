===============================
Creating a Feature from Scratch
===============================

This guide will outline the process of creating a new feature from the beginning.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/index>`
for more information before continuing.

For a more detailed and in-depth guide about creating a new feature from scratch, please read this unofficial
development guide, `Feature Config <https://terra.atr.sh/#/page/feature%20config>`__.

Setting up a New Feature
========================

`PROCEDURE`

1. Add feature stage(s)
-----------------------

.. card::

    Your pack will need feature stages in order to generate features.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the ``generation-stage-feature`` addon as a dependency, using versions ``1.+``.

    This addon will allow us to create new feature stages for features within the pack manifest.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 9

        id: YOUR_PACK_ID

        version: 0.1.0

        addons:
          language-yaml: "1.+"
          chunk-generator-noise-3d: "1.+"
          ...
          generation-stage-feature: "1.+"

    Add the highlighted lines below to your pack manifest to create these feature stages.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 5-10

        id: YOUR_PACK_ID

        ...

        stages:
          - id: trees
            type: FEATURE

          - id: landforms
            type: FEATURE

    We'll only be using the ``trees`` stage for this guide.

    .. tip::

        The feature stage ids can be named to your liking and feature stages will generate in order from top to bottom.

2. Create your structure file
-----------------------------

.. card::

    Structure files can either be dynamic TerraScript ``.tesf`` or static schematics ``.schem`` files.

    .. tab-set::

            .. tab-item:: TerraScript

                TerraScript files consist of :doc:`TerraScript </config/documentation/terrascript/index>` language
                that typically generate structures procedurally and can create unique complex structure layouts.

                1. Add the ``structure-terrascript-loader`` addon to the pack manifest, using versions ``1.+``

                2. Create a blank ``.tesf`` file.

                3. Add TerraScript within the .tesf file to generate the structure.

                ``oak_tree.tesf`` will be used for this guide.

            .. tab-item:: Schematic

                Schematic files consist of an arrangement of blocks that make up a structure that can be saved through
                `WorldEdit <https://worldedit.enginehub.org/en/latest/usage/clipboard/>`__.

                1. Add the ``structure-sponge-loader`` addon to the pack manifest, using versions ``1.+``

                2. Save your structure using `WorldEdit <https://worldedit.enginehub.org/en/latest/usage/clipboard/>`__.

                3. Add the ``.schem`` file to your pack.

                ``oak_tree.schem`` will be used for this guide.


3. Create your feature config
-----------------------------

.. card::

    Add the ``config-feature`` addon to the pack manifest, using versions ``1.+``.

    This addon will allow us to create feature config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 7

        id: YOUR_PACK_ID

        version: 0.1.0

        addons:
          ...
          config-feature: "1.+"

    :ref:`Create a blank config file <create-config-file>` and open it your editor.

    Set the :ref:`config type <config-types>` via the ``type``
    parameter, and config ``id`` as shown below. ``oak_trees.yml`` will be used for this guide.

    .. code-block:: yaml
        :caption: oak_trees.yml
        :linenos:

        id: OAK_TREES
        type: FEATURE

4. Create the feature distributor
---------------------------------

.. card::

    Distributors determine the x-axis and z-axis placement of a feature in the world.

    Add the ``config-distributors`` addon to the pack manifest, using versions ``1.+``.

    This addon will allow us to create distributors within feature config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 7

        id: YOUR_PACK_ID

        version: 0.1.0

        addons:
          ...
          config-distributors: "1.+"

    Configure the ``oak_trees.yml`` config to utilize ``PADDED_GRID`` distributor type as shown below.

    .. code-block:: yaml
        :caption: oak_trees.yml
        :linenos:
        :emphasize-lines: 4-8

        id: OAK_TREES
        type: FEATURE

        distributor:
          type: PADDED_GRID
          width: 12
          padding: 4
          salt: 5864

    The ``PADDED_GRID`` distributor type utilizes cells in a grid with
    the feature placed within each cell with padding between each cell
    to ensure that features don't generate too close to one another.

    ``PADDED_GRID`` utilizes the parameters ``width``, ``padding``, and ``salt``.

    * ``Width`` - Determines the size of each cell that will contain your feature
    * ``Padding`` - Determines the gap between each cell
    * ``Salt`` - Offsets the results of the distributor to prevent overlap

5. Create the feature locator
-----------------------------

.. card::

    Locators determine the y-axis placement of a feature in the world.

    Add the ``config-locators`` addon to the pack manifest, using versions ``1.+``.

    This addon will allow us to create locators within feature config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 7

        id: YOUR_PACK_ID

        version: 0.1.0

        addons:
          ...
          config-locators: "1.+"

    Configure the ``oak_trees.yml`` config to utilize the ``TOP`` locator type as shown below.

    .. code-block:: yaml
        :caption: oak_trees.yml
        :linenos:
        :emphasize-lines: 7-11

        id: OAK_TREES
        type: FEATURE

        distributor:
          ...

        locator:
          type: TOP
          range:
            min: 0
            max: 319

    The ``TOP`` locator type will place the feature on the block located at the highest possible y-level.

.. tip::

    You can utilize multiple locators for stricter criteria as shown below with the ``AND`` locator.

    .. code-block:: yaml
        :caption: feature.yml
        :linenos:
        :emphasize-lines: 2

        locator:
          type: AND
          locators:
            - type: TOP
              range: &range  #range values anchored for other locators to use
                min: 0
                max: 319
            - type: PATTERN
              range: *range  #references previously anchored range values
              pattern:
                type: MATCH_SET
                blocks:
                  - minecraft:grass_block
                  - minecraft:dirt
                offset: -1

6. Apply the structure
----------------------

.. card::

    You can now add your structure to the ``oak_trees.yml`` config with the highlighted lines below.

    .. code-block:: yaml
        :caption: oak_trees.yml
        :linenos:
        :emphasize-lines: 10-13

        id: OAK_TREES
        type: FEATURE

        distributor:
          ...

        locator:
          ...

        structures:
          distribution:
            type: CONSTANT
          structures: oak_tree

    The ``structures`` sub-configuration consists of a structure or list of structures for
    the feature config to select from to generate in the world.

    It also consists of a distributor type to influence the structure selection.

.. tip::

    Features can select from a list of structures with a distribution type to guide the structure selection
    as shown below:

    .. code-block:: yaml
        :caption: feature.yml
        :linenos:

        structures:
          distribution:
            type: WHITE_NOISE
            salt: 4357
          structures:
            - oak_tree_1: 1
            - oak_tree_2: 1
            - oak_tree_3: 1

7. Apply feature to biomes
--------------------------

.. card::

    Open a biome file with your editor.

    We'll use ``FIRST_BIOME`` from
    :doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/index>` for this guide

    Add the highlighted lines below to the ``FIRST_BIOME`` config.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 15-17

        id: FIRST_BIOME

        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: LINEAR_HEIGHTMAP
            base: 64

        palette:
          - BLOCK:minecraft:stone: 319

        features:
          trees:
            - OAK_TREES

    The ``OAK_TREES`` feature should now generate your oak tree structures in ``FIRST_BIOME``.

.. tip::

    Multiple feature stages in biome configs will be done as shown below:

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 7-11

        id: FIRST_BIOME

        type: BIOME

        ...

        features:
          trees:
            - OAK_TREES
          landforms:
            - ROCKS

8. Load your pack
-----------------
At this stage, your pack should now be capable of generating oak trees! You can load up your pack by starting your
development client / server which contains the pack you have just defined. You can confirm that your pack has loaded
if the pack id (as specified in the pack manifest) appears when using the ``/packs`` command, or in your console
when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

Conclusion
==========

Once you have verified your pack has loaded correctly, you can now generate a world with your new oak trees!