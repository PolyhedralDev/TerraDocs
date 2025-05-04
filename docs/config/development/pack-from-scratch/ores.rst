==========================
Creating Ores From Scratch
==========================

This guide will continue the process of creating a new Terra config
pack from the beginning with creating ores.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/introduction>`
for more information before continuing.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up Ores
===============

`PROCEDURE`

1. Create an abstract ore config
--------------------------------

.. card::

    An ore config file will allow you configure ores that will generate in your world.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the ``config-ore`` addon as a dependency, using versions ``1.+``.

    This addon will allow us to create palette config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.9.0

        addons:
          ...
          config-ore: "1.+"

    :ref:`Create a blank config file <create-config-file>` and open it your editor.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    An abstract ore config file will be necessary for ore configs to inherit from and easily configure.

    ``abstract_ore.yml`` will be example file name used for this abstract ore file in this guide.

    .. code-block:: yaml
        :caption: abstract_ore.yml
        :linenos:

        id: ABSTRACT_ORE
        type: ORE
        abstract: true

        replace:
          - minecraft:stone
          - minecraft:deepslate

    The ``abstract`` parameter with a value of true will allow this abstract config to not have the mandatory
    parameters required for an ore config file.

    The ``replace`` parameter consists a block or list of blocks that the ore config will be able to
    replace, which is stone and deepslate in this case.

2. Create an ore config file
----------------------------

.. card::

    With an abstract ore config prepared, an ore config can now be created to inherit those abstract parameters.

    :ref:`Create a blank config file <create-config-file>` and open it your editor.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    ``coal_ore.yml`` will be example file name used for this ore file in this guide.

    .. code-block:: yaml
        :caption: coal_ore.yml
        :linenos:

        id: COAL_ORE
        type: ORE
        extends: ABSTRACT_ORE

        material: minecraft:coal_ore

        material-overrides:
          minecraft:deepslate: minecraft:deepslate_coal_ore

        size: 10

    ``COAL_ORE`` will extend ``ABSTRACT_ORE`` in order to be able to replace stone and deepslate blocks.

    ``material`` determines the block that this ore config will place, which will be coal ore.

    ``material-overrides`` determines different blocks to be placed if specified blocks are replaced by the ore.

    If a deepslate block is replaced, then deepslate coal ore will be placed instead of regular coal ore for this case.

    ``size`` determines the size of the ore vein that will generate

3. Add ore feature config file
------------------------------

.. card::

    With an ore config file created, a feature config file will be needed in order to place that ore as a feature in
    a generation stage.

    :ref:`Create a blank config file <create-config-file>` and open it your editor.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    ``coal_ore_feature.yml`` will be example file name used for this ore feature config file in this guide.

    .. code-block:: yaml
        :caption: coal_ore_feature.yml
        :linenos:

        id: COAL_ORE_FEATURE
        type: FEATURE

        distributor:
          type: SAMPLER
          sampler:
            type: POSITIVE_WHITE_NOISE
            salt: 1234
          threshold: 10 * (1/256)
        #averageCountPerChunk Divide by 16^2 to get % per column

        locator:
          type: GAUSSIAN_RANDOM
          amount: 1
          height:
            min: -64
            max: 192
          standard-deviation: (192-(-64))/6
        # Divide distance from min to max by 6 to fit 3 standard deviations (~99.7% of results) within the range.

        structures:
          distribution:
            type: CONSTANT
          structures: COAL_ORE

  The feature config for this ore is set up and configurable to best resemble ore generation.

  The :doc:`distributor </config/documentation/objects/Distributor>` threshold utilizes a number that represents the average ore count per chunk, which proceeds
  to get divided by 256.

  The :doc:`locator </config/documentation/objects/Locator>` utilizes ``GAUSSIAN_RANDOM`` with a standard deviation that adds the max and min range values, which get
  get divided by 6 in order to fit 3 standard deviations (~99.7% of results) within the range. Furthermore, ore
  generation results are higher towards the middle of the range.

    .. note::

      A uniform ore distribution generates ore with equal chance across the entire range rather than more towards the
      middle of the range with a normal distribution.

      A uniform ore distribution will use the locator shown below.

      .. code-block:: yaml
          :caption: coal_ore_uniform.yml
          :linenos:

          locator:
            type: RANDOM
            amount: 1
            height:
              min: -64
              max: 192
            salt: 1234

4. Add ores feature stage
-------------------------

.. card::

    We will now utilize the ``generation-stage-feature`` addon that was added in
    :doc:`Setting up a New Feature </config/development/pack-from-scratch/grass>` to add a new generation stage for ores.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the following lines to add a generation stage for ores.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 15-16

        id: YOUR_PACK_ID

        ...

        stages:
          - id: preprocessors
            type: FEATURE

          - id: flora
            type: FEATURE

          - id: trees
            type: FEATURE

          - id: ores
            type: FEATURE

    The ores generation stage can now generate ores as features and kept separate from other generation stages.

5. Create an abstract ore biome config
--------------------------------------

.. card::

    Instead of adding ``COAL_ORE`` to every individual biome config, an abstract biome config can be extended
    by biomes for them to inherit the ore feature generation.

    This eases the config development process down the line especially as more biomes and ores get added to
    the config pack without having to individually update every config file.

    :ref:`Create a blank config file <create-config-file>` and open it your editor.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    ``ores_default.yml`` will be example file name used for this abstract ore file in this guide.

    .. code-block:: yaml
        :caption: ores_default.yml
        :linenos:

        id: ORES_DEFAULT
        type: BIOME
        abstract: true

        features:
          ores:
            - COAL_ORE_FEATURE

    ``ORES_DEFAULT`` allows for the ores generation stage to be configured in one config, which can be extended to
    biomes that will generate ores.

6. Extend abstract ore biome config
-----------------------------------

.. card::

    The biome configs can now be configured to extend ``ORES_DEFAULT`` in order to inherit and generate ore features.

    While you could extend ``ORES_DEFAULT`` to each biome individually, you already have an abstract ``BASE`` config
    that is extended to each biome.

    With that in mind, you can simply extend ``ORES_DEFAULT`` through ``BASE`` to allow those biomes that extend ``BASE``
    to inherit ore generation with ease.

    Open your ``BASE`` config in your :ref:`editor of choice <editor>`.

    Add the following line to extend ``ORES_DEFAULT`` to the ``BASE`` config.

    .. code-block:: yaml
        :caption: base.yml
        :linenos:
        :emphasize-lines: 4

        id: BASE
        type: BIOME
        abstract: true
        extends: ORES_DEFAULT

        ocean:
          palette: BLOCK:minecraft:water
          level: 62

        features:
          preprocessors:
            - CONTAIN_FLOATING_WATER

    ``ORES_DEFAULT`` should now be extended to all biome config that extend ``BASE`` and generate ``COAL_ORE_FEATURE``.

7. Load your pack
-----------------
At this stage, your pack should now be capable of generating ores! You can load up your pack by starting your
development client / server which contains the pack you have just defined. You can confirm that your pack has loaded
if the pack id (as specified in the pack manifest) appears when using the ``/packs`` command, or in your console
when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

Conclusion
==========

Now that you've verified your pack has loaded correctly, you can
now generate a world with ores!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/9-adding-ores>`_.





