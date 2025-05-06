======================================
Creating a Biome Provider from Scratch
======================================

This guide will outline the process of creating a :doc:`biome provider </config/documentation/objects/BiomeProvider>`
from the beginning using the pipeline type to distribute biomes.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/index>`
for more information before continuing.

For a more detailed and in-depth guide about creating a new biome provider from scratch, please read
this unofficial development guide, `Pipeline Biome Provider <https://terra.atr.sh/#/page/pipeline%20biome%20provider>`__.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up a New Pipeline
=========================

`PROCEDURE`

1. Add pipeline biome provider
------------------------------

.. card::

    A :doc:`biome provider </config/documentation/objects/BiomeProvider>` determines and configures where biomes
    will generate in the world.

    The pipeline :doc:`biome provider </config/documentation/objects/BiomeProvider>` is typically
    used to procedurally distribute biomes in 2D.

    The pipeline operates utilizing an initial biome layout that goes through consecutive stages that
    modify this layout to a final layout result that determines the biome distribution placement.

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Add the ``biome-provider-pipeline-v2`` addon as a dependency, using versions ``1.+``.

    This addon will allow us to create a pipeline biome provider.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 6

        id: YOUR_PACK_ID
        version: 0.6.0

        addons:
          ...
          biome-provider-pipeline-v2: "1.+"

    Add the highlighted lines below to replace the current ``SINGLE`` biome provider and start creating the biome pipeline.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 5-7

        id: YOUR_PACK_ID

        ...

        biomes:
          type: PIPELINE
          resolution: 4

    ``resolution`` determines the size of each biome ‘pixel’ in blocks.

    Increasing ``resolution`` will improve performance at the cost of blocky edges in biome placement
    with a resolution of 4 being the best balance between performance and obvious blocky edges.

2. Add pipeline blending
------------------------

.. card::

    The biome pipeline will require blending that will warp the edges between biomes
    in order to lessen the blocky edges created from the pipeline resolution increase.

    Add the highlighted lines below to add blending to the biome pipeline.

    ``OPEN_SIMPLEX_2`` will be utilized for this.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 8-12

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

    ``blend.amplitude`` determines the strength of the blending between each biome.

    ``blend.sampler`` will contain the :doc:`noise sampler </config/documentation/objects/NoiseSampler>` and its
    :ref:`parameters <parameters>` that will blend the edges between biomes.

    .. note::
        Documentation of ``OPEN_SIMPLEX_2`` and other noise samplers can be found :doc:`here </config/documentation/objects/NoiseSampler>`.


3. Add the pipeline source
--------------------------

.. card::

    The biome pipeline will require a source that will serve as the initial biome layout.

    Add the highlighted lines below to add a source to the biome pipeline.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 13-20

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
                type: CONSTANT
              biomes:
                - land: 1

    ``source.sampler`` utilizes a :doc:`noise sampler </config/documentation/objects/NoiseSampler>` to distribute
    the initial biome layout. We'll leave it as ``CONSTANT`` as this is a rather simple pipeline source.

    ``source.biomes`` consists of the :doc:`weighted list </config/documentation/objects/WeightedList>` of
    :doc:`pipeline biomes </config/documentation/objects/PipelineBiome>` that will serve as the initial layout.

    In this case, we're using a placeholder or ephemeral :doc:`pipeline biome </config/documentation/objects/PipelineBiome>`
    that will have to be replaced by an actual biome through a :doc:`pipeline stage </config/documentation/objects/Stage>`
    later on, otherwise the pack won't load.

    .. tip::
        It is best to put placeholder biomes in all lowercase to distinguish them from biome IDs that are typically
        in all uppercase.

4. Add the pipeline stage
-------------------------

.. card::

    The biome pipeline will require a stage to replace the placeholder biome that the source initially laid out.

    Add the highlighted lines below to add a ``REPLACE`` stage to the biome pipeline.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 21-29

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
                type: CONSTANT
              biomes:
                - land: 1
            stages:
              - type: REPLACE
                sampler:
                  type: OPEN_SIMPLEX_2
                  frequency: 0.01
                from: land
                to:
                  - FIRST_BIOME: 1
                  - SECOND_BIOME: 1

    The ``stages`` parameter consists of the list of :doc:`pipeline stages </config/documentation/objects/Stage>` that will
    modify the source layout.

    The ``REPLACE`` pipeline stage utilizes the :ref:`parameters <parameters>` ``sampler``, ``from``, and ``to``.

    * ``Sampler`` - Determines the :doc:`noise sampler </config/documentation/objects/NoiseSampler>` that will influence replacement biome selection
    * ``From`` - Specifies the :doc:`tag </config/documentation/objects/Tag>` or biome that will be replaced
    * ``To`` - Specifies the :doc:`weighted list </config/documentation/objects/WeightedList>`
      of :doc:`pipeline biome(s) </config/documentation/objects/PipelineBiome>` that will replace
      the ``from`` biome

    Weighted lists covered in detail :ref:`here <weighted-list>`.

    .. note::

        You'll need to source your own biomes other than ``FIRST_BIOME`` to have other biomes to distribute
        through the pipeline.

        If needed, there is a ``SECOND_BIOME`` sample with a palette located on
        `GitHub <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/6-adding-pipeline>`_.

.. tip::

    You can utilize multiple stages consecutively to further distribute the biome placement with ``SELF`` representing
    the ``from`` biome being replaced.

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 17-20

        stages:
          - type: REPLACE
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.01
            from: land
            to:
              - FIRST_BIOME: 1
              - SECOND_BIOME: 1
              - THIRD_BIOME: 1

          - type: REPLACE
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.01
              salt: 3423
            from: FIRST_BIOME
            to:
              - SELF: 1
              - FOURTH_BIOME: 1

    For the case above, the ``land`` placeholder biome will be distributed into the ``FIRST_BIOME``, ``SECOND_BIOME``,
    and ``THIRD_BIOME`` by the first ``REPLACE`` stage then the following ``REPLACE`` stage will distribute the
    ``FIRST_BIOME`` into ``FIRST_BIOME`` represented by ``SELF`` and ``FOURTH_BIOME`` as well.

5. Load your pack
-----------------
At this stage, your pack should now be capable of biome distribution! You can load up your pack by starting your
development client / server which contains the pack you have just defined. You can confirm that your pack has loaded
if the pack id (as specified in the pack manifest) appears when using the ``/packs`` command, or in your console
when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to :doc:`contact us </contact>` with any relevant errors.

.. note::
    The ``/packs reload`` command cannot be used when new biome config files are added to a
    config pack since the biome registry gets frozen upon world generation.

    Using the command will result with a ``An internal error occured while
    attemping to perform this command`` message.

    Clients might only need to create a new world while servers may need to
    completely restart in order to load new biomes when the biome registry isn't frozen.

.. tip::
    A useful tool for visually previewing the biome distribution defined by your biome provider is the Biome Tool that
    can be found `here <https://github.com/PolyhedralDev/BiomeTool>`__.

Conclusion
==========

Once you have verified your pack has loaded correctly, you can now generate a world with multiple biomes distributed
through the biome provider pipeline!

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/6-adding-pipeline>`_.

.. image:: /img/config/development/pack-from-scratch/pipeline.png