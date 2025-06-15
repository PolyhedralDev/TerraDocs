============================
Creating Oceans From Scratch
============================

This guide will continue the process of creating a new Terra config
pack from the beginning with creating oceans.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/introduction>`
for more information before continuing.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up Oceans
=================

`PROCEDURE`

1. Add ocean biome config
-------------------------

.. card::

    An ocean biome config is necessary to generate oceans and customize the features within them.

    :ref:`Create a blank config file <create-config-file>` with the file name ``ocean_biome.yml``.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    Set the rest of ``OCEAN_BIOME`` parameters as the sample below.

    .. code-block:: yaml
        :caption: ocean_biome.yml
        :linenos:
    
        id: OCEAN_BIOME
        type: BIOME

        vanilla: minecraft:ocean

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 32

          sampler-2d:
            type: EXPRESSION
            dimensions: 2
            expression: (simplex(x, z)+1) * 4
            samplers:
              simplex:
                type: OPEN_SIMPLEX_2
                dimensions: 2
                frequency: 0.04

        palette:
          - SAND_PALETTE: 319

    ``OCEAN_BIOME`` generates terrain at a lower y-level for water to eventually fill up above.

2. Add ocean biome to pipeline
------------------------------

.. card::

    ``OCEAN_BIOME`` will have to be added to the biome pipeline in order to distribute it within the world generation.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the following lines below to add an ephemeral ocean
    :doc:`pipeline biome </config/documentation/objects/PipelineBiome>` with a source
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>`.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 18-19,22,32-38

        id: YOUR_PACK_ID

        ...

        biomes:
          type: PIPELINE
          resolution: 4
          blend:
            amplitude: 2
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.1
          pipeline:
            source:
              type: SAMPLER
              sampler:
                dimensions: 2
                type: OPEN_SIMPLEX_2
                frequency: 0.004
              biomes:
                - land: 1
                - ocean: 1
            stages:
              - type: REPLACE
                sampler:
                  type: OPEN_SIMPLEX_2
                  frequency: 0.01
                from: land
                to:
                  - FIRST_BIOME: 1
                  - SECOND_BIOME: 1
              - type: REPLACE
                sampler:
                  type: OPEN_SIMPLEX_2
                  frequency: 0.01
                from: ocean
                to:
                  - OCEAN_BIOME: 1

    An ephemeral ``ocean`` biome will generate with the ephemeral ``land`` biome.

    The ephemeral ``ocean`` biome is replaced by the ``OCEAN_BIOME`` in a ``REPLACE`` stage later on.

    Don't forget to replace the ``CONSTANT`` sampler for the source ephemeral
    :doc:`pipeline biomes </config/documentation/objects/PipelineBiome>`
    ,or only ``OCEAN_BIOME`` will generate in the world.

    Loading up the world with the newly added ``OCEAN_BIOME`` will present empty oceans
    without any water currently.

    .. image:: /img/config/development/pack-from-scratch/oceans/oceans-empty.png

3. Add ocean palette
--------------------

.. card::

    Water will be needed to fill your oceans.

    This can be done through an ocean palette.

    Open ``OCEAN_BIOME`` in your :ref:`editor of choice <editor>`.

    Add the following lines to add an ocean palette to ``OCEAN_BIOME``.

    .. code-block:: yaml
        :caption: ocean_biome.yml
        :linenos:
        :emphasize-lines: 11-13

        id: OCEAN_BIOME
        type: BIOME

        vanilla: minecraft:ocean

        ...

        palette:
          - SAND_PALETTE: 319

        ocean:
          palette: BLOCK:minecraft:water
          level: 62

    ``ocean.palette`` controls the material or block that will replace air blocks.

    ``ocean.level`` controls the max y-level that the ocean palette will fill.

    In this case, ocean palette will place water blocks to fill any air blocks
    from y-level 62 down to the bottom of the world.

    .. important::

        An issue that should be noted with ``OCEAN_BIOME`` as the only biome config
        with this ocean palette is how biome blending will show obvious air gaps
        when blending with other biomes without this ocean palette.

        You could add this ocean palette to every biome, but that can get tedious
        depending on the number of biomes that will require this ocean palette
        and a ocean palette change requiring an update to each biome config.


.. image:: /img/config/development/pack-from-scratch/oceans/oceans-issue.png

4. Add abstract config
----------------------

.. card::

    In order to make it easier to configure the ocean palette across all biomes, an abstract config file will
    be put to use.

    An abstract config file is very useful for :ref:`parameters <parameters>` that are shared and repeated across several biome configs
    without having to configure the :ref:`parameter <parameters>` in each config individually.

    :ref:`Create a blank config file <create-config-file>`  with the file name ``base.yml``.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    .. code-block:: yaml
        :caption: base.yml
        :linenos:

        id: BASE
        type: BIOME

    Add the following lines to make the config abstract and configure an ocean palette.

    .. code-block:: yaml
        :caption: base.yml
        :linenos:
        :emphasize-lines: 3,5-7

        id: BASE
        type: BIOME
        abstract: true

        ocean:
          palette: BLOCK:minecraft:water
          level: 62

    The ``abstract`` :ref:`parameter <parameters>` set to ``true`` will allow ``BASE`` to not require the mandatory
    :ref:`parameters <parameters>` that are typical for a ``BIOME`` config file.

    Any :ref:`parameters <parameters>` configured in this ``BASE`` config can be easily extended to any ``BIOME`` config file.

5. Extend abstract config
-------------------------

.. card::

    The biome configs will need to extend the ``BASE`` config in order to inherit its :ref:`parameters <parameters>`.

    Open ``OCEAN_BIOME`` in your :ref:`editor of choice <editor>`.

    The ocean palette lines can be removed and add the following line to extend ``BASE``.

    .. code-block:: yaml
        :caption: ocean_biome.yml
        :linenos:
        :emphasize-lines: 3

        id: OCEAN_BIOME
        type: BIOME
        extends: BASE

        vanilla: minecraft:ocean

        ...

        palette:
          - SAND_PALETTE: 319

    ``OCEAN_BIOME`` will now inherit any :ref:`parameters <parameters>` configured in ``BASE`` as it has
    been listed in ``extends`` :ref:`parameter <parameters>` of the ``OCEAN_BIOME`` config file.

    Every biome config will need to extend ``BASE`` in order to inherit the ocean palette as well.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 3

        id: FIRST_BIOME
        type: BIOME
        extends: BASE

        ...

    .. code-block:: yaml
        :caption: second_biome.yml
        :linenos:
        :emphasize-lines: 3

        id: SECOND_BIOME
        type: BIOME
        extends: BASE

        ...

6. Load up your pack
--------------------

At this stage, your pack should now be capable of generating oceans.
You can load up your pack by starting your development client / server which contains the pack you have just defined.
You can confirm that your pack has loaded if the pack id (as specified in the pack manifest) appears when using the
``/packs`` command, or in your console when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

Conclusion
==========

Once you have verified your pack has loaded correctly, you can now generate a world with oceans!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/7-adding-oceans>`_.

.. image:: /img/config/development/pack-from-scratch/oceans/oceans-working.png









