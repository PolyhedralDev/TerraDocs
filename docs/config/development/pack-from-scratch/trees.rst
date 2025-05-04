================================================
Creating a Feature with a Structure From Scratch
================================================

This guide will outline the process of creating a new feature from the beginning
with adding tree structures.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/grass>`
for more information before continuing.

For a more detailed and in-depth guide about creating a new feature from scratch, please read
this unofficial development guide, `Feature Config <https://terra.atr.sh/#/page/feature%20config>`__.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up a New Structure
==========================

`PROCEDURE`

1. Create your structure file
-----------------------------

.. card::

    :doc:`Structure </config/documentation/objects/Structure>` files can
    either be dynamic TerraScript ``.tesf`` or static schematic ``.schem`` files.

    .. tab-set::

            .. tab-item:: TerraScript

                TerraScript files are written in the :doc:`TerraScript Language </config/documentation/terrascript/index>`.
                TerraScript allows for procedurally generated structures and unique complex structure layouts.

                1. Add the ``structure-terrascript-loader`` addon to the pack manifest, using versions ``1.+``

                2. Create a blank ``.tesf`` file.

                3. Add TerraScript within the ``.tesf`` file to generate the structure.

                ``oak_tree.tesf`` will be the example file name used for this guide.

                A sample ``oak_tree.tesf`` file has been provided below if you need it.

                .. code-block:: yaml
                    :caption: oak_tree.tesf
                    :linenos:

                    block(0, 0, 0, "minecraft:oak_log", true);
                    block(0, 1, 0, "minecraft:oak_leaves", false);

            .. tab-item:: Schematic

                Schematic files consist of an arrangement of blocks that make up a structure that can be saved through
                `WorldEdit <https://worldedit.enginehub.org/en/latest/usage/clipboard/>`__.

                1. Add the ``structure-sponge-loader`` addon to the pack manifest, using versions ``1.+``

                2. Source a ``.schem`` file, these can be created using `WorldEdit <https://worldedit.enginehub.org/en/latest/usage/clipboard/>`__ if you wish to create your own.

                3. Add the ``.schem`` file to your pack.

                ``oak_tree.schem`` will be the example file name used for this guide.

                A sample ``oak_tree.schem`` can be found `here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/4-adding-trees>`_ if needed.


2. Create your feature config
-----------------------------

.. card::

    We will now utilize the ``config-feature`` addon that was added in
    :doc:`Setting up a New Feature </config/development/pack-from-scratch/grass>` to
    create a new feature config file.

    ``oak_tree_feature`` will be example file name used for the feature config in this guide.

    .. code-block:: yaml
        :caption: oak_tree_feature.yml
        :linenos:

        id: OAK_TREE_FEATURE
        type: FEATURE

3. Add the feature distributor
------------------------------

.. card::

    We will now utilize the ``config-distributors`` addon that was added in
    :doc:`Setting up a New Feature </config/development/pack-from-scratch/grass>` to add the distributor.

    Configure the ``oak_tree_feature`` config to utilize the ``PADDED_GRID`` distributor type as shown below.

    .. code-block:: yaml
        :caption: oak_tree_feature.yml
        :linenos:
        :emphasize-lines: 4-8

        id: OAK_TREE_FEATURE
        type: FEATURE

        distributor:
          type: PADDED_GRID
          width: 12
          padding: 4
          salt: 5864

    The ``PADDED_GRID`` distributor type utilizes cells in a grid with
    the feature placed within each cell with padding between each cell
    to ensure that features don't generate too close to one another.

    ``PADDED_GRID`` utilizes the nested :ref:`parameters <parameters>` ``width``, ``padding``, and ``salt``.

    * ``Width`` - Determines the size of each cell that will contain your feature
    * ``Padding`` - Determines the gap between each cell
    * ``Salt`` - Typically a random number that offsets the distributor results to prevent feature placement overlap with the same distributor type. Salt function covered in detail :ref:`here <noise-sampler-salt-theory>`.

    .. image:: /img/config/development/pack-from-scratch/paddedgrid.png
        :width: 75%

    .. note::
        Documentation of ``PADDED_GRID`` and other distributor types can be found :doc:`here </config/documentation/objects/Distributor>`.

4. Add the feature locator
--------------------------

.. card::

    We will now utilize the ``config-locators`` addon that was added in
    :doc:`Setting up a New Feature </config/development/pack-from-scratch/grass>` to add the locator.

    Configure the ``oak_tree_feature`` config to utilize the ``TOP`` locator type as shown below.

    .. code-block:: yaml
        :caption: oak_tree_feature.yml
        :linenos:
        :emphasize-lines: 7-11

        id: OAK_TREE_FEATURE
        type: FEATURE

        distributor:
          ...

        locator:
          type: TOP
          range:
            min: 0
            max: 319

    The ``TOP`` locator type will place the feature on the block located at the highest y-level rather than every block
    with air above it with the ``SURFACE`` locator.

    .. note::
        Documentation of the various locator types available can be found :doc:`here </config/documentation/objects/Locator>`.


5. Improve feature locator
--------------------------

.. card::

    Just like with the ``SURFACE`` locator when adding short grass, the ``TOP`` locator is handy for placing features at
    the highest block, but it doesn't check the block it places the feature upon.

    Utilizing the ``AND`` locator, we can use multiple :doc:`locators </config/documentation/objects/Locator>` for
    stricter criteria for where the feature can generate.

    Using the ``PATTERN`` locator with the ``type`` specified to use ``MATCH_SET`` will allow us to specify the blocks
    that must match in order to generate the feature.

    Add the highlighted lines below to add the additional locator.

    .. code-block:: yaml
        :caption: feature.yml
        :linenos:
        :emphasize-lines: 8-21

        id: OAK_TREE_FEATURE
        type: FEATURE

        distributor:
          ...

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

5. Add the structure
--------------------

.. card::

    You can now add your :doc:`structure </config/documentation/objects/Structure>` to the ``oak_tree_feature`` config with the highlighted lines below.

    .. code-block:: yaml
        :caption: oak_tree_feature.yml
        :linenos:
        :emphasize-lines: 10-13

        id: OAK_TREE_FEATURE
        type: FEATURE

        distributor:
          ...

        locator:
          ...

        structures:
          distribution:
            type: CONSTANT
          structures: oak_tree

.. tip::

    Features can select from a :doc:`weighted list </config/documentation/objects/WeightedList>` of structures with a
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>`
    to guide the structure selection as shown below.

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

    Weighted lists covered in detail :ref:`here <weighted-list>`.

6. Apply feature to biome
-------------------------

.. card::

    We'll now add the tree feature to ``FIRST_BIOME``.

    Add the highlighted lines below to the ``FIRST_BIOME`` config.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 18-19

        id: FIRST_BIOME

        type: BIOME

        vanilla: minecraft:plains

        ...

        features:
          flora:
            - GRASS_FEATURE
          trees:
            - OAK_TREE_FEATURE

    The ``OAK_TREE_FEATURE`` feature should now generate your oak tree structures in ``FIRST_BIOME``.

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

Once you have verified your pack has loaded correctly, you can now generate a world with oak tree structures
using features!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/5-adding-trees>`_.