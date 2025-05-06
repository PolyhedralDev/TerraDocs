=============================
Creating Carving From Scratch
=============================

This guide will continue the process of creating a new Terra config
pack from the beginning with creating caves through carving.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/introduction>`
for more information before continuing.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up Carving
==================

`PROCEDURE`

1. Add cached sampler
---------------------

.. card::

    Utilizing a cached sampler will make config development easier when creating
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>` expressions.

    Cached samplers allow a sampler to be used anywhere in the pack for
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>` expressions and
    the :ref:`TerraScript Sampler Function <function-sampler>`.

    Cached samplers are extremely convenient especially when you have various expressions that utilize the same
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>`.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the following lines below to cache some samplers.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 9-23

        id: YOUR_PACK_ID

        addons:
          ...

        stages:
          ...

        samplers:
          simplex:
            dimensions: 2
            type: FBM
            octaves: 4
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.0075
          simplex3:
            dimensions: 3
            type: FBM
            octaves: 4
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.0075

    These samplers are little different from your usual ones through the use of :ref:`fractalization <sampler-fractalization>`.

    The fractalizer type ``FBM`` combines multiple layers (or octaves) of the :doc:`noise sampler </config/documentation/objects/NoiseSampler>`
    in order to add more detail to the sampler.

    The newly cached ``simplex`` sampler will be generally used for terrain samplers as they typically
    utilize 2 dimensions.

    The newly cached ``simplex3`` sampler will be used for the carving that will implemented in this guide as
    they work with 3 dimensions.

2. Add carving abstract config
------------------------------

.. card::

    An abstract carving config will be utilized for biomes to easily extend and inherit the carving.

    :ref:`Create a blank config file <create-config-file>` with the file name ``carving_land.yml``.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, config ``id``, and ``abstract`` as shown below.

    .. code-block:: yaml
        :caption: carving_land.yml
        :linenos:
    
        id: CARVING_LAND
        type: BIOME
        abstract: true

    Add the following lines to add the carving sampler.

    .. code-block:: yaml
        :caption: carving_land.yml
        :linenos:
        :emphasize-lines: 5-29

        id: CARVING_LAND
        type: BIOME
        abstract: true

        carving:
          sampler:
            dimensions: 3
            type: EXPRESSION
            variables:

              carvingThreshold: 0.55 # Higher = less carving
              carvingMinHeight: -63
              carvingMaxHeight: 140
              carvingCap: 1 # Caps the amount of base carving

              spaghettiStrengthLarge: 0.59
              spaghettiStrengthSmall: 0.57

            expression: |
              -carvingThreshold
              + if(y<carvingMinHeight||y>carvingMaxHeight,0, // Skip unnecessary calculations
                min(carvingCap,
                  // Spaghetti Caves
                  max(
                    spaghettiStrengthLarge * ((-(|simplex3(x,y+0000,z)|+|simplex3(x,y+1000,z)|)/2)+1),
                    spaghettiStrengthSmall * ((-(|simplex3(x,y+2000,z)|+|simplex3(x,y+3000,z)|)/2)+1)
                  )
                )
              )

    .. tip::

        It is recommended to have read the :doc:`Creating Terrain From Scratch </config/development/pack-from-scratch/terrain>`
        and the :doc:`TerraScript Syntax </config/documentation/terrascript/syntax>` to have a better
        understanding.


    This carving sampler will carve out non-air blocks between the set maximum y-level of ``140`` and
    minimum y-level ``-63``.

    The sampler expression will produce results that resemble that of spaghetti caves.

    This guide will not go into the full depth of how this carving sampler works, but at least
    give a brief limited explanation.

    Starting with the expression is with the ``carvingThreshold`` value set to negative, which
    gets added to by the rest of the expression.

    The rest of the expression states that if ``y`` is less than ``carvingMinHeight`` or ``y`` is
    greater than ``carvingMaxHeight``, then output ``0``.

    This results in no block placement at that coordinate.

    The argument after ``0`` can be seen as the else statement. It contains ``min()``
    , which takes the lowest value between ``carvingCap`` and the ``max()`` that takes the
    highest value between two sets of simplex3 samplers with each sampler slightly offset from
    the other and added together.

    .. note::

        This carving contains only the spaghetti cave aspect from the default overworld config carving, which
        can be viewed through `GitHub <https://github.com/PolyhedralDev/TerraOverworldConfig/>`__.

3. Extend carving abstract
--------------------------

.. card::

    The land biome configs will need to extend ``CARVING_LAND`` in order for them to inherit the carving.

    Open ``FIRST_BIOME`` and ``SECOND_BIOME`` in your :ref:`editor of choice <editor>`.

    Add the ``CARVING_LAND`` to the ``extends`` parameter list of ``FIRST_BIOME`` and ``SECOND_BIOME``.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 3-5

        id: FIRST_BIOME
        type: BIOME
        extends:
          - BASE
          - CARVING_LAND

        ...

    .. code-block:: yaml
        :caption: second_biome.yml
        :linenos:
        :emphasize-lines: 3-5

        id: SECOND_BIOME
        type: BIOME
        extends:
          - BASE
          - CARVING_LAND

        ...

    .. warning::

        It is not recommended to add ``CARVING_LAND`` to ``OCEAN_BIOME`` as the carving is set with a max range value
        that will result in carved pockets of air with floating water in the ocean.

        Another abstract carving config with a reduced max carving height is recommended to avoid this issue.

.. image:: /img/config/development/pack-from-scratch/carving/carving.png

4. Load up your pack
--------------------

.. card::

  At this stage, your pack should now be capable of caves through carving.
  You can load up your pack by starting your development client / server which contains the pack you have just defined.
  You can confirm that your pack has loaded if the pack id (as specified in the pack manifest) appears when using the
  ``/packs`` command, or in your console when starting the server / client up.

  If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
  has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
  and follow through the previous steps again carefully.

  If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

  .. attention::
      If you have loaded the pack and did the :doc:`Creating an Ocean from Scratch</config/development/pack-from-scratch/introduction>`,
      previosuly, you'll see cases of floating water, which had their adjacent solid
      blocks carved out by ``CARVING_LAND``.

      This issue will be addressed in the next step.

.. image:: /img/config/development/pack-from-scratch/carving/carving-issue.png

5. Floating Water Issue
-----------------------

.. card::

  There are several methods of dealing with the issue of floating water caused by carving.

  The simpler method that will be used in this guide is a feature that will place stone blocks in order to contain
  floating water blocks.

  :ref:`Create a blank config file <create-config-file>` with the file name ``contain_floating_water.yml``.

  Set the :ref:`config type <config-types>` via the ``type``
  :ref:`parameter <parameters>`, and config ``id`` as shown below.

  .. code-block:: yaml
      :caption: contain_floating_water.yml
      :linenos:

      id: CONTAIN_FLOATING_WATER
      type: FEATURE

  Add the highlighted lines to create this specific feature.

  .. code-block:: yaml
      :caption: contain_floating_water.yml
      :linenos:
      :emphasize-lines: 4-35

      id: CONTAIN_FLOATING_WATER
      type: FEATURE

      distributor:
        type: "YES"

      locator:
        type: AND
        locators:
          - type: PATTERN
            range: &range
              min: 0
              max: 63
            pattern:
              type: MATCH_AIR
              offset: 0
          - type: OR
            locators:
              - type: PATTERN
                range: *range
                pattern:
                  type: MATCH
                  block: minecraft:water
                  offset: 1
              - type: ADJACENT_PATTERN
                range: *range
                pattern:
                  type: MATCH
                  block: minecraft:water
                  offset: 0

      structures:
        distribution:
          type: CONSTANT
        structures: BLOCK:minecraft:stone

  The ``CONTAIN_FLOATING_WATER`` feature simply looks for air blocks with adjacent patterns of water blocks
  and places a stone block at that location.

.. card::

  Open your pack manifest in your :ref:`editor of choice <editor>`.

  Add a generation stage to your pack manifest to allow this feature to generate
  separately from other features.

  The generation stage will be called ``preprocessors`` for this guide.

  .. code-block:: yaml
      :caption: pack.yml
      :linenos:
      :emphasize-lines: 5-7

      id: YOUR_PACK_ID

      ...

      stages:
        - id: preprocessors
          type: FEATURE

        - id: trees
          type: FEATURE

        - id: flora
          type: FEATURE

.. card::

  The ``CONTAIN_FLOATING_WATER`` feature could be added individually to every biome config, but that can be tedious
  depending on the number of biomes your config pack has.

  Like in :doc:`Creating an Ocean from Scratch</config/development/pack-from-scratch/introduction>` with an ocean
  palette, an abstract config can be used to extend features for biomes to inherit and generate.

  Open your ``BASE`` config in your :ref:`editor of choice <editor>`.

  Add the following lines for biomes that extend ``BASE`` to inherit the ``preprocessors``
  feature generation from ``BASE``.

  .. code-block:: yaml
      :caption: base.yml
      :linenos:
      :emphasize-lines: 9-11

      id: BASE
      type: BIOME
      abstract: true

      ocean:
        palette: BLOCK:minecraft:water
        level: 62

      features:
        preprocessors:
          - CONTAIN_FLOATING_WATER

  It's not a perfect method, but it resolves the issue in a simple manner without much complication.

Conclusion
==========

Now that you've verified your pack has loaded correctly and resolved the floating water issue, you can
now generate a world with caves!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/8-adding-carving>`_.

.. image:: /img/config/development/pack-from-scratch/carving/carving-fixed.png