===============================
Creating a Palette From Scratch
===============================

This guide will continue the process of creating a new Terra config
pack from the beginning with creating a new palette.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/introduction>`
for more information before continuing.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up a New Palette
========================

`PROCEDURE`

1. Create your palette config
-----------------------------

.. card::

    Palettes define the blocks that will make up each layer of terrain.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the ``config-palette`` addon as a dependency, using versions ``1.+``.

    This addon will allow us to create palette config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 8

        id: YOUR_PACK_ID
        version: 0.2.0

        addons:
          language-yaml: "1.+"
          chunk-generator-noise-3d: "1.+"
          ...
          config-palette: "1.+"

    :ref:`Create a blank config file <create-config-file>` with the file name ``grass_palette.yml``.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    .. code-block:: yaml
        :caption: grass_palette.yml
        :linenos:

        id: GRASS_PALETTE
        type: PALETTE

2. Add palette layers
---------------------

.. card::

    Palette configs consist of :doc:`palette layers </config/documentation/objects/PaletteLayer>` that
    each contain the materials or :doc:`blocks </config/documentation/objects/Block>` for that layer.

    Each :doc:`palette layer </config/documentation/objects/PaletteLayer>` also includes the number of
    layers that the blocks will span across on the y-axis.

    Add the highlighted lines below to your palette config to create the palette layers for ``grass_palette.yml``.

    .. code-block:: yaml
        :caption: grass_palette.yml
        :emphasize-lines: 4-15
        :linenos:

        id: GRASS_PALETTE
        type: PALETTE

        layers:
           # Top palette layer
           - materials: minecraft:grass_block
             layers: 1

           # Second palette layer that will be 2 layers thick
           - materials: minecraft:dirt
             layers: 2

           # Last palette layer. Also will make up the rest of the palette
           - materials: minecraft:stone
             layers: 1 #

.. tip::

    Palette layers can select from a :doc:`weighted list </config/documentation/objects/WeightedList>` of
    :doc:`blocks </config/documentation/objects/Block>` alongside each layer being capable of using a
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>`
    to influence the block selection for terrain generation.

    .. code-block:: yaml
        :caption: grass_snow_mix.yml
        :linenos:

        layers:
          - materials:
              - minecraft:grass_block: 3
              - minecraft:coarse_dirt: 1
              - minecraft:snow_block: 5
            layers: 1
            sampler:
              type: DOMAIN_WARP
              amplitude: 1
              warp:
                type: GAUSSIAN
              sampler:
                type: OPEN_SIMPLEX_2
                frequency: 0.02
          - materials:
              - minecraft:coarse_dirt: 1
              - minecraft:dirt: 2
            layers: 1
            sampler:
              type: WHITE_NOISE
              salt: 9231
          - materials: minecraft:stone
            layers: 1

    Weighted lists covered in detail :ref:`here <weighted-list>`.

3. Apply palette to biome
-------------------------

.. card::

    You can now apply your :doc:`palette </config/documentation/objects/Palette>` to ``FIRST_BIOME``.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 12

        id: FIRST_BIOME
        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: LINEAR_HEIGHTMAP
            base: 64

        palette:
          - GRASS_PALETTE: 319
          - BLOCK:minecraft:bedrock: -61

4. Load up your pack
--------------------

At this stage, your pack should now be capable of generating a palette with grass blocks with dirt and stone underneath!
You can load up your pack by starting your development client / server which contains the pack you have just defined.
You can confirm that your pack has loaded if the pack id (as specified in the pack manifest) appears when using the
``/packs`` command, or in your console when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

5. Additional Palette of bedrock
--------------------------------

Conclusion
==========

Once you have verified your pack has loaded correctly, you can now generate a world with palettes!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/2-adding-palette>`_.

.. image:: /img/config/development/pack-from-scratch/terrain/flat-terrain.png