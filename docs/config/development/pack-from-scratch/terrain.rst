=============================
Creating Terrain From Scratch
=============================

This guide will continue the process of creating a new Terra config
pack from the beginning with creating terrain.

If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/introduction>`
for more information before continuing.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

Setting up New Terrain
======================

`PROCEDURE`

1. Add EXPRESSION sampler
-------------------------

.. card::

    The ``EXPRESSION`` :doc:`noise sampler </config/documentation/objects/NoiseSampler>` allows for
    configuration of an :doc:`expression </config/documentation/objects/Expression>` for sampler output
    with the capability of using functions in-built or user-defined along with other samplers within itself.

    Open your ``FIRST_BIOME`` :doc:`BIOME </config/documentation/configs/BIOME>` config in your :ref:`editor of choice <editor>`.

    Add the highlighted lines below to replace the current terrain sampler with an ``EXPRESSION`` sampler.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 8-10

        id: FIRST_BIOME
        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 64

        ...

    ``terrain.sampler`` consists of the nested :ref:`parameters <parameters>` ``type``, ``dimensions``, and ``expression``.

    * ``type`` - Determines the :doc:`noise sampler </config/documentation/objects/NoiseSampler>` that will generate the terrain
    * ``dimensions`` - Determines the amount of dimensional coordinates (x, y, & z) for input sampling
    * ``expression`` - The expression configured by the user to create sampler output for terrain

    Terrain generation is determined by whether the :doc:`expression </config/documentation/objects/Expression>` output
    is positive or negative.

    Positive output results in solid terrain whereas negative output results in air.

    The sampler :doc:`expression </config/documentation/objects/Expression>` ``-y + 64`` just takes into account the
    y-coordinate in particular for the moment.

    The :doc:`expression </config/documentation/objects/Expression>` result will remain positive and generate terrain
    till the y-coordinate in the world reaches ``64`` leading to the expression looking like ``-64 + 64`` equaling
    ``0``, which isn't positive meaning no terrain generation will occur here and beyond ``64``.

    Y-coordinates greater than ``64`` will result in a negative output like ``-90 + 64`` equaling ``-26`` that will
    result in no terrain.

    The expression ``-y +64`` results in perfectly flat terrain.

    .. image:: /img/config/development/pack-from-scratch/terrain/flat-terrain.png

.. note::
    Documentation of ``EXPRESSION`` and other noise samplers can be found :doc:`here </config/documentation/objects/NoiseSampler>`.

    Documentation of mathematical expressions can be found :doc:`here </config/documentation/objects/Expression>`.

.. tip::
    You can add variables for :doc:`expressions </config/documentation/objects/Expression>` to use to allow for easier configuration.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 5-7

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            variables:
              base: 64
            expression: -y + base

    You can even reference anchored variables not directly attached to the sampler.

      .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 1-2,8

        vars: &variables #variables anchored for samplers to use
          base: 64

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            variables: *variables #references previously anchored variables
            expression: -y + base

2. Add sampler-2d
-----------------

.. card::

    The :doc:`expression </config/documentation/objects/Expression>` ``-y + 64`` results in perfectly flat terrain that
    will be used as the base terrain in which we'll apply :doc:`noise </config/development/noise/index>` to using
    ``terrain.sampler-2d``.

    ``terrain.sampler-2d`` is recommended to configure alongside the ``terrain.sampler`` as it allows for easier
    adding or subtracting from the base terrain especially with being in 2D, which doesn't account for the y-coordinate.

    ``terrain.sampler-2d`` may be less performant, but results in more detailed terrain with being full resolution rather
    than interpolated.

    Add the highlighted lines below to add the ``terrain.sampler-2d``

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 12-15

        id: FIRST_BIOME
        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 64

          sampler-2d:
            type: EXPRESSION
            dimensions: 2
            expression:

        ...

    ``terrain.sampler-2d`` will consist of the same nested :ref:`parameters <parameters>` ``type``, ``dimensions``, and ``expression``.

    As ``terrain.sampler-2d`` is 2D, it will have 2 dimensions rather than 3 dimensions.

3. Add sampler for use
----------------------

.. card::

    ``terrain.sampler-2d`` will now require an :doc:`expression </config/documentation/objects/Expression>` to
    influence the flat generation created by the ``terrain.sampler`` expression.

    Either a cached :doc:`noise sampler</config/documentation/objects/NoiseSampler>` referenced through the pack
    manifest or one provided within ``sampler-2d.samplers`` will be needed in order to use it within the
    ``terrain.sampler-2d`` expression.

    Add the highlighted lines below to provide a ``OPEN_SIMPLEX_2`` :doc:`noise sampler</config/documentation/objects/NoiseSampler>`
    for use in the expression.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 16-20

        id: FIRST_BIOME
        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 64

          sampler-2d:
            type: EXPRESSION
            dimensions: 2
            expression:
            samplers:
              simplex:
                type: OPEN_SIMPLEX_2
                dimensions: 2
                frequency: 0.04

        ...

    ``sampler-2d.samplers`` consists of the noise samplers provided for use within the expression parameter.

    Samplers are defined with a function name hand picked by the user with this case being ``simplex``.

    ``simplex`` will have to contain the :ref:`parameters <parameters>` required for the
    :doc:`noise sampler </config/documentation/objects/NoiseSampler>`, which are ``dimensions`` and ``frequency``.

    ``frequency`` is explained in detail :ref:`here <sampler-frequency>`.

4. Apply sampler to expression
------------------------------

.. card::

    The ``simplex`` sampler can now be utilized within the ``terrain.sampler-2d`` expression.

    Add the highlighted line to the expression line below to implement ``simplex`` into the terrain.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 15

        id: FIRST_BIOME
        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 64

          sampler-2d:
            type: EXPRESSION
            dimensions: 2
            expression: simplex(x, z)
            samplers:
              simplex:
                type: OPEN_SIMPLEX_2
                dimensions: 2
                frequency: 0.04

        ...

    The terrain generates with 1 block elevation differences in response with ``simplex`` output.

    .. image:: /img/config/development/pack-from-scratch/terrain/bumpy-terrain.png

5. Adjust sampler-2d expression
-------------------------------

.. card::

    The ``sampler-2d`` expression can be adjusted in a multitude of different ways to help achieve the result you
    terrain desire.

    As the output range of ``OPEN_SIMPLEX_2`` is ``[-1, 1]``, adding ``1`` to the ``simplex`` output within the expression
    will lead to the output range always resulting positive. With that, terrain will only be added on top of the base
    terrain without any subtraction as there is no possible negative output.

    This is useful if you want terrain to be maintained above a certain y-level.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 10

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 64

          sampler-2d:
            type: EXPRESSION
            dimensions: 2
            expression: simplex(x, z)+1
            samplers:
              simplex:
                type: OPEN_SIMPLEX_2
                dimensions: 2
                frequency: 0.04

    Multiplying ``simplex`` with a value within the expression will lead to more hilly terrain as the ``simplex`` output
    gets increased along with expanding the range between the minimum and maximum output.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 10

        terrain:
          sampler:
            type: EXPRESSION
            dimensions: 3
            expression: -y + 64

          sampler-2d:
            type: EXPRESSION
            dimensions: 2
            expression: (simplex(x, z)+1) * 4
            samplers:
              simplex:
                type: OPEN_SIMPLEX_2
                dimensions: 2
                frequency: 0.04

    .. tip::
        Make sure you put the addition operation within parentheses to make sure it happens before the
        multiplication operation

    The terrain elevation has some variety to it now. You can adjust the multiply value by increasing it to have bigger
    hills and decreasing it for smaller hills.

    .. image:: /img/config/development/pack-from-scratch/terrain/hill-terrain.png

Conclusion
==========

This guide only covers the surface level capability in which you can configure terrain expressions.

There is limitless potential with more complex and intricate :doc:`expressions </config/documentation/objects/Expression>`
that utilize various features such as built-in functions, user-defined functions, and multiple
:doc:`noise samplers </config/documentation/objects/NoiseSampler>` to achieve terrain from that of
simple landscapes to floating islands.

Reference configurations for this guide can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/3-adding-terrain>`_.

.. note::
    A useful tool for visually previewing your sampler configs is the Noise Tool that can be found and explained
    in more detail :ref:`here <noise-tool>`.












