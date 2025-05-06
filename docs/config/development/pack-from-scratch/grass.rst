===============================
Creating a Feature from Scratch
===============================

This guide will outline the process of creating a new feature from the beginning with adding grass.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/index>`
for more information before continuing.

For a more detailed and in-depth guide about creating a new feature from scratch, please read
this unofficial development guide, `Feature Config <https://terra.atr.sh/#/page/feature%20config>`__.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up a New Feature
========================

`PROCEDURE`

1. Add feature stage(s)
-----------------------

.. card::

    Feature generation is divided up into generation stages. Your pack will need
    to define at least one generation stage in order to generate any features.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the ``generation-stage-feature`` addon as a dependency, using versions ``1.+``.

    This addon will allow us to create new generation stages for features within the pack manifest.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.4.0

        addons:
          ...
          generation-stage-feature: "1.+"

    Add the highlighted lines below to your pack manifest to create these generation stages.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 5-10

        id: YOUR_PACK_ID

        ...

        stages:
          - id: flora
            type: FEATURE

          - id: trees
            type: FEATURE

    We'll only be using the ``flora`` stage for this guide.

    .. tip::

        The generation stage ids can be named to your liking and generation stages will generate in order from top to bottom.

2. Create your feature config
-----------------------------

.. card::

    Add the ``config-feature`` addon to the pack manifest, using versions ``1.+``.

    This addon will allow us to create feature config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.4.0

        addons:
          ...
          config-feature: "1.+"

    :ref:`Create a blank config file <create-config-file>` with the file name ``grass_feature.yml``.

    Set the :ref:`config type <config-types>` via the ``type``
    :ref:`parameter <parameters>`, and config ``id`` as shown below.

    .. code-block:: yaml
        :caption: grass_feature.yml
        :linenos:

        id: GRASS_FEATURE
        type: FEATURE

3. Add the feature distributor
------------------------------

.. card::

    :doc:`Distributors </config/documentation/objects/Distributor>` determine the x-axis and z-axis placement of a feature in the world.

    Add the ``config-distributors`` addon to the pack manifest, using versions ``1.+``.

    This addon provides a set of :doc:`distributors </config/documentation/objects/Distributor>` to use within feature config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.4.0

        addons:
          ...
          config-distributors: "1.+"

    Configure the ``grass_feature.yml`` config to utilize the ``POSITIVE_WHITE_NOISE`` distributor type as shown below.

    .. code-block:: yaml
        :caption: grass_feature.yml
        :linenos:
        :emphasize-lines: 4-8

        id: GRASS_FEATURE
        type: FEATURE

        distributor:
          type: SAMPLER
          sampler:
            type: POSITIVE_WHITE_NOISE
          threshold: 0.25

    .. note::
        Documentation of distributor types can be found :doc:`here </config/documentation/objects/Distributor>`.

        Documentation of ``POSITIVE_WHITE_NOISE`` and other noise samplers can be found :doc:`here </config/documentation/objects/NoiseSampler>`.

4. Add the feature locator
--------------------------

.. card::

    :doc:`Locators </config/documentation/objects/Locator>` determine the y-axis placement of a feature in the world.

    Add the ``config-locators`` addon to the pack manifest, using versions ``1.+``.

    This addon provides a set of :doc:`locators </config/documentation/objects/Locator>` to use within feature config files.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.4.0

        addons:
          ...
          config-locators: "1.+"

    Configure the ``grass_feature.yml`` config to utilize the ``SURFACE`` locator type as shown below.

    .. code-block:: yaml
        :caption: grass_feature.yml
        :linenos:
        :emphasize-lines: 7-11

        id: GRASS_FEATURE
        type: FEATURE

        distributor:
          ...

        locator:
          type: SURFACE
          range:
            min: 0
            max: 319

    The ``SURFACE`` locator type will place the feature above any block with air above it.

    Each locator will typically require the ``range`` that it can check.

    ``range`` has ``min`` (minimum) and a ``max`` (maximum) :ref:`parameters <parameters>`.

    .. note::
        Documentation of the various locator types available can be found :doc:`here </config/documentation/objects/Locator>`.

5. Improve feature locator
--------------------------

.. card::

    The ``SURFACE`` locator is handy for placing features on top of blocks, but it doesn't check the block it places
    the feature upon.

    Utilizing the ``AND`` locator, we can use multiple :doc:`locators </config/documentation/objects/Locator>` for
    stricter criteria for where the feature can generate.

    Using the ``PATTERN`` locator with the ``type`` specified to use ``MATCH_SET`` will allow us to specify the blocks
    that must match in order to generate the feature.

    Add the highlighted lines below to add the additional locator.

    .. code-block:: yaml
        :caption: feature.yml
        :linenos:
        :emphasize-lines: 8-21

        id: GRASS_FEATURE
        type: FEATURE

        distributor:
          ...

        locator:
          type: AND
          locators:
            - type: SURFACE
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

    The ``AND`` locator list contains both the ``SURFACE`` and ``PATTERN`` locators with the range anchored in ``SURFACE``
    being referenced by the range in ``PATTERN``.

    The ``PATTERN`` locator with the ``MATCH_SET`` ``type`` consists of the :ref:`parameters <parameters>` ``blocks``
    and ``offset``.

    * ``blocks`` - List of blocks that must match in order to generate the feature
    * ``offset`` - The y-level offset of the checked block

    The blocks ``minecraft:grass_block`` and ``minecraft:dirt`` will suffice with an offset of -1 to check the block that
    is specifically right underneath the feature.

6. Add the structure
--------------------

.. card::

    The ``structure-block-shortcut`` addon will provide the capability to use a shortcut within structure distribution
    to directly place a block rather than having to create an entire structure file for just a single block.

    Add the ``structure-block-shortcut`` addon to the pack manifest, using versions ``1.+``.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.4.0

        addons:
          ...
          structure-block-shortcut: "1.+"

    We will now utilize the ``structure-block-shortcut`` addon that was added above to
    easily define single blocks rather than a :doc:`structure </config/documentation/objects/Structure>`.

    .. note::
        Versions prior to 1.20.3 will need to use ``minecraft_grass``.

    .. code-block:: yaml
        :caption: grass_feature.yml
        :linenos:
        :emphasize-lines: 10-13

        id: GRASS_FEATURE
        type: FEATURE

        distributor:
          ...

        locator:
          ...

        structures:
          distribution:
            type: CONSTANT
          structures: BLOCK:minecraft:short_grass

    The ``structures`` parent key consists of the nested :ref:`parameters <parameters>`
    ``structures.structures`` and  ``structures.distribution``.

    ``structures.structures`` determines the structure or :doc:`weighted list </config/documentation/objects/WeightedList>`
    of structures to select from upon feature generation in the world.

    ``structures.distribution`` determines the :doc:`noise sampler </config/documentation/objects/NoiseSampler>`
    that influences the structure selection results.

.. tip::

    Features can select from a :doc:`weighted list </config/documentation/objects/WeightedList>` of structures or blocks
    in this particular case with a :doc:`noise sampler </config/documentation/objects/NoiseSampler>` to guide
    the structure selection as shown below.

    .. code-block:: yaml
        :caption: feature.yml
        :linenos:

        structures:
          distribution:
            type: WHITE_NOISE
            salt: 4357
          structures:
            - BLOCK:minecraft:poppy: 1
            - BLOCK:minecraft:blue_orchid: 1
            - BLOCK:minecraft:dandelion: 1

    Weighted lists covered in detail :ref:`here <weighted-list>`.

6. Apply feature to biome
-------------------------

.. card::

    We'll now add the grass feature to ``FIRST_BIOME``.

    Add the highlighted lines below to the ``FIRST_BIOME`` config.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 8-10

        id: FIRST_BIOME
        type: BIOME

        vanilla: minecraft:plains

        ...

        features:
          flora:
            - GRASS_FEATURE

    The ``GRASS_FEATURE`` should now generate grass in ``FIRST_BIOME``.

.. tip::

    Multiple generation stages in biome configs will be done as shown below:

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 6-10

        id: FIRST_BIOME
        type: BIOME

        ...

        features:
          flora:
            - GRASS_FEATURE
          trees:
            - OAK_TREES

7. Load your pack
-----------------
At this stage, your pack should now be capable of generating grass! You can load up your pack by starting your
development client / server which contains the pack you have just defined. You can confirm that your pack has loaded
if the pack id (as specified in the pack manifest) appears when using the ``/packs`` command, or in your console
when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

Conclusion
==========

Once you have verified your pack has loaded correctly, you can now generate a world with grass using features!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/4-adding-grass>`_.

.. image:: /img/config/development/pack-from-scratch/first-biome-grass.png