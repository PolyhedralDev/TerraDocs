=====================
Sampler Configuration
=====================

.. seealso::

    :doc:`/config/development/samplers/index`

    :ref:`Config Documentation Format <config-documentation-format>` :octicon:`chevron-right`

A sampler is a config defined function that maps coordinates and the world seed to a set
of output values.

A 'sample' is defined as a single calculation provided by a sampler, and the result of
that calculation is regarded as the 'output value'. A collective set of output values is
regarded as 'noise'.

The output values determine some kind of behaviour for each block or column. This behaviour
is dependent on the context of the sampler definition. 

Shared Parameters
=================

:bdg-primary:`type` ``String``
The ID of a sampler. Determines what kind of sampler is used, as well as what additional
parameters become available to configure the sampler.

DimensionApplicableSampler
--------------------------

The following is only required for ``DimensionApplicableSampler``\s

:bdg-primary:`dimensions` ``Integer``
How many dimensions the sampler operates. Must only be either ``2``, or ``3``.


- 2D samplers provide the same output value for blocks contained within the
  same world column (since the Y axis is not factored in 2D sampling). 
- A 3D sampler defined in a parameter that expects a 2D sampler will result in the Y
  coordinate input defaulting to a constant value during sampling.

Sampler Categories
==================

.. container:: nested-cards

    .. card:: **Noise Samplers**

        Samplers that 'produce noise', i.e some pattern of values based on
        the input.

        - `IMAGE`_
        - `CONSTANT`_

        .. card:: **Random Noise Samplers**

            Samplers that use random values for every input, with no regard for producing any
            discernable structure. Outputs tend to look like tv-static.

            - `WHITE_NOISE`_
            - `POSITIVE_WHITE_NOISE`_
            - `GAUSSIAN`_

        .. card:: **Gradient Noise Samplers**

            Samplers where outputs produce structured noise. Inputs close in distance tend to
            produce similar output values.

            - `VALUE`_
            - `VALUE_CUBIC`_
            - `GABOR`_
            - `CELLULAR`_

            .. card:: **Simplex Samplers**

                A group of samplers that use similar algorithms that produce outputs dubbed
                'simplex' noise.

                - `PERLIN`_
                - `SIMPLEX`_
                - `OPEN_SIMPLEX_2`_
                - `OPEN_SIMPLEX_2S`_

    .. card:: **Mutator Samplers**

        Samplers that take other samplers as inputs. Mutator samplers typically act as 'filters'
        that provide some kind of modification to the output of other sampler(s).

        - `DOMAIN_WARP`_
        - `KERNEL`_
        - `LINEAR_HEIGHTMAP`_

        .. card:: **Fractalizer Samplers**

            A category of mutator samplers that fractalize the input sampler.

            - `FBM`_
            - `PING_PONG`_
            - `RIDGED`_

        .. card:: **Normalizer Samplers**

            A category of mutator samplers that redistribute the output values of a sampler.

            .. hlist::

                - `LINEAR`_
                - `CLAMP`_
                - `NORMAL`_
                - `PROBABILITY`_
                - `SCALE`_
                - `POSTERIZATION`_

        .. card:: **Binary Arithmetic Samplers**

            Mutator samplers that combine the outputs of two samplers together using a
            math operator

            .. hlist::

                - `ADD`_
                - `SUB`_
                - `MUL`_
                - `DIV`_
                - `MAX`_
                - `MIN`_

    .. card:: **Other Samplers**
        
        Other samplers that do not strictly fit into a single category.

        - `EXPRESSION`_

Sampler Types
=============

WHITE_NOISE
-----------

Produces `White noise`_.

.. image:: /img/concepts/noise/whitenoise64x64.png

.. include:: parameter-groups/noise.rst

POSITIVE_WHITE_NOISE
--------------------

Identical to `WHITE_NOISE`_, but redistributed to only produce positive
values for convenience.

.. include:: parameter-groups/noise.rst

GAUSSIAN
--------

Identical to `WHITE_NOISE`_, but redistributed to follow a `gaussian distribution`_\.

.. include:: parameter-groups/noise.rst

PERLIN
------

Produces `Perlin noise`_.

.. include:: parameter-groups/noise.rst

.. tip::

    It is recommended to use other simplex based samplers rather than PERLIN, as
    Perlin noise produces signficant directional artifacts, which may be undesired.

SIMPLEX
-------

Produces `Simplex noise`_.

.. include:: parameter-groups/noise.rst

OPEN_SIMPLEX_2
--------------

Produces `Simplex noise`_ (using the algorithm from OpenSimplex2_).

.. image:: /img/concepts/noise/opensimplex2_64x64.png

.. include:: parameter-groups/noise.rst

OPEN_SIMPLEX_2S
---------------

Produces smoother `Simplex noise`_ (using the algorithm from OpenSimplex2_).

.. include:: parameter-groups/noise.rst

VALUE
-----

Produces `Value noise`_ using `linear interpolation`_ (`bilinear`_ for 2D, `trilinear`_ for 3D).

.. include:: parameter-groups/noise.rst

VALUE_CUBIC
-----------

Identical to `VALUE`_ except using `cubic interpolation`_ (`bicubic`_ for 2D, `tricubic`_ for 3D).

.. include:: parameter-groups/noise.rst

GABOR
-----

Produces `Gabor noise`_.

.. warning::

    The GABOR sampler is significantly slower at producing noise compared to other noise samplers.

.. include:: parameter-groups/noise.rst

:bdg-success:`rotation` ``Float``

Default: ``0.25``

:bdg-success:`isotrophic` ``Boolean``

Default: ``true``

:bdg-success:`deviation` ``Float``

Default: ``1.0``

:bdg-success:`impulses` ``Float``

Default: ``64.0``

:bdg-success:`frequency_0` ``Float``

Default: ``0.625``

CELLULAR
--------

Produces cellular / `Worley noise`_.

.. image:: /img/concepts/noise/cellular_256x256.png

**DIAGRAM**

.. image:: /img/concepts/noise/cellular_diagram.svg

- Black dots: The center of each cell.
- Red lines: A random direction and distance from the cell center, called 'jitter'.
- Blue dots: The cell origin, determined by jitter from the cell center.
- Green dot: Coordinates being sampled.
- Purple line: Distance to the closest cell origin.
- Orange line: Distance to the second closest cell origin.
- Gold line: Distance to the third closest cell origin.

**PARAMETERS**

.. include:: parameter-groups/noise.rst

:bdg-success:`distance` ``String``
The method used for calculating the distance from the cell origin.

Default: ``EuclideanSq``

**Distance Types**

- ``Euclidean``
- ``EuclideanSq``
- ``Manhattan``
- ``Hybrid``

:bdg-success:`return` ``String``
The function the sampler will use to calculate the noise.

Default: ``Distance``

**Return Types**

Definitions:

``s`` - The coordinates being sampled.

``c`` - The coordinates of the nearest cell origin.

``d1`` - The distance from the nearest cell origin.

``d2`` - The distance from the second nearest cell origin

``d3`` - The distance from the third nearest cell origin

Types:

- ``NoiseLookup`` - Passes ``c`` into a sampler, and returns the output.
- ``CellValue`` - Returns a random value based on ``c`` (Equivalent to ``NoiseLookup`` with a `WHITE_NOISE`_ sampler).
- ``Angle`` - Returns the angle from ``s`` to ``c``.
- ``Distance`` - Returns ``d1``.
- ``Distance2``- Returns ``d2``.
- ``Distance2Add`` - Returns ``(d1 + d2) / 2``.
- ``Distance2Sub`` - Returns ``d2 - d1``.
- ``Distance2Mul`` - Returns ``(d1 * d2) / 2``.
- ``Distance2Div`` - Returns ``d1 / d2``.
- ``Distance3`` - Returns ``d3``.
- ``Distance3Add`` - Returns ``(d1 + d3) / 2``.
- ``Distance3Sub`` - Returns ``d3 - d1``.
- ``Distance3Mul`` - Returns ``d3 * d1``.
- ``Distance3Div`` - Returns ``d1 / d3``.

:bdg-success:`jitter` ``Float``
Determines how far cell origins can randomly spread out from the center of cells.

Default: ``1``

A jitter of ``0`` places cell origins exactly in the center of each cell, resulting in a perfect grid.
Values between ``-1`` and ``1`` are recommended, as values outside that range may produce artifacts.

:bdg-success:`lookup` ``Sampler``
The lookup sampler used when the ``distance`` parameter is set to ``NoiseLookup``

Default: `OPEN_SIMPLEX_2`_ sampler

IMAGE
-----

Outputs the channel of an image that is tiled, redistributed from the channel range [0-255] to output range [-1, 1].

:bdg-primary:`image` ``String``
Path to the image relative to the config pack directory. (For Windows users: Use the ``/`` directory separator instead of ``\``)

Example path: `path/to/the/image.png`

:bdg-primary:`frequency` ``Float``
:ref:`Frequency <sampler-frequency>` of the image. Determines how the image gets scaled.

A frequency of ``1.0`` means 1 pixel = 1 block, a frequency of ``2.0`` means 2 pixels = 1 block.

.. attention::

    Frequencies below ``1.0`` are not recommended, as pixels aren't interpolated when upscaled;
    results may look pixelated depending on use.

    .. grid:: 3

        .. grid-item:: **grayscale_circles.png**
            :padding: 0

            .. image:: /img/concepts/noise/image/grayscale_circles.png
                :width: 200

        .. grid-item:: **1.0 Frequency**

            .. image:: /img/concepts/noise/image/image_sampler_circles_frequency_1.0_zoomed.png
                :width: 200

        .. grid-item:: **0.25 Frequency**

            .. image:: /img/concepts/noise/image/image_sampler_circles_frequency_0.25_zoomed.png
                :width: 200

    ``0.25`` frequency = ``0.25 pixels = 1 block`` or ``1 pixel = 4 blocks`` (as demonstrated above using a block grid).

:bdg-primary:`channel` ``String``
Which channel of the image to output.

Valid channels:

- ``GRAYSCALE``
- ``ALPHA``
- ``RED``
- ``GREEN``
- ``BLUE``

.. card:: Channel Examples

    .. grid:: 6

        .. grid-item:: Original Image
            :columns: 4

            .. image:: /img/concepts/noise/image/pacman_ghosts.png

        .. grid-item:: Grayscale
            :columns: 4

            .. image:: /img/concepts/noise/image/pacman_ghosts_grayscale.png

        .. grid-item:: Alpha Channel*
            :columns: 4

            .. image:: /img/concepts/noise/image/pacman_ghosts_alpha_channel.png

        .. grid-item:: Red Channel
            :columns: 4

            .. image:: /img/concepts/noise/image/pacman_ghosts_red_channel.png

        .. grid-item:: Green Channel
            :columns: 4

            .. image:: /img/concepts/noise/image/pacman_ghosts_green_channel.png

        .. grid-item:: Blue Channel
            :columns: 4

            .. image:: /img/concepts/noise/image/pacman_ghosts_blue_channel.png

    \*The alpha channel is all white because there is no transparency in the original image.

.. dropdown:: Example Image Samplers

    .. grid:: 3

        .. grid-item:: **grayscale_circles.png**
            :padding: 0

            .. image:: /img/concepts/noise/image/grayscale_circles.png
                :width: 200

        .. grid-item:: **mountain_heightmap.png**

            .. image:: /img/concepts/noise/image/mountain_heightmap.png
                :width: 200

    World generated using the mountain heightmap to shape the terrain, and the circles
    to determine biome temperature:

    .. image:: /img/concepts/noise/image/image_distributed_biomes.png
        :width: 50%

    **Terrain Sampler** (Using `LINEAR_HEIGHTMAP`_ to work as a terrain sampler)

    .. code-block:: yaml
        
        type: LINEAR_HEIGHTMAP
        base: 128
        scale: 64
        sampler:
          type: IMAGE
          image: mountain_heightmap.png
          channel: GRAYSCALE
          frequency: 1

    **Temperature Sampler**

    .. code-block:: yaml

        type: IMAGE
        image: grayscale_circles.png
        channel: GRAYSCALE
        frequency: 1

CONSTANT
--------

Outputs a constant value, regardless of the inputs. Typically used in cases where you
don't want the sampler to do anything.

:bdg-success:`value` ``Float``
The value to be outputted.

Default: ``0.0``

DOMAIN_WARP
-----------

Warps a sampler by another sampler. See :ref:`Domain Warping <domain-warping>` for more information.

:bdg-primary:`warp` ``Sampler``

:bdg-primary:`sampler` ``Sampler``

:bdg-success:`amplitude` ``Float``

Default: ``1.0``

KERNEL
------

:bdg-primary:`kernel` ``List`` of ``List`` of ``Float``

:bdg-primary:`sampler` ``Sampler``

:bdg-success:`factor` ``Float``

Default: ``1.0``

:bdg-success:`frequency` ``Float``

Default: ``1.0``

LINEAR_HEIGHTMAP
----------------

Treats a 2D sampler as a heightmap, converting it to a 3D `SDF`_
for use as a terrain sampler.

:bdg-primary:`base` ``Float``
The base y level of the terrain.

:bdg-success:`sampler` ``Sampler``
The sampler to be used as a heightmap.

Default: `CONSTANT`_ sampler

:bdg-success:`scale` ``Float``
Scales the height of the heightmap.

Default: ``1.0``

FBM
---

.. include:: parameter-groups/fractalizer.rst

PING_PONG
---------

.. include:: parameter-groups/fractalizer.rst

:bdg-success:`ping-pong` ``Float``

Default: ``2.0``

RIDGED
------

.. include:: parameter-groups/fractalizer.rst

LINEAR
------

.. include:: parameter-groups/normalizer.rst

:bdg-primary:`max` ``Float``

:bdg-primary:`min` ``Float``

CLAMP
-----

.. include:: parameter-groups/normalizer.rst

:bdg-primary:`max` ``Float``

:bdg-primary:`min` ``Float``

NORMAL
------

.. include:: parameter-groups/normalizer.rst

:bdg-primary:`mean` ``Float``

:bdg-primary:`standard-deviation` ``Float``

:bdg-success:`groups` ``Integer``

Default: ``16384``

PROBABILITY
-----------

.. include:: parameter-groups/normalizer.rst

SCALE
-----

.. include:: parameter-groups/normalizer.rst

:bdg-primary:`amplitude` ``Float``

POSTERIZATION
-------------

.. include:: parameter-groups/normalizer.rst

:bdg-primary:`steps` ``Integer``

ADD
---

.. include:: parameter-groups/binary-arithmetic.rst

SUB
---

.. include:: parameter-groups/binary-arithmetic.rst

MUL
---

.. include:: parameter-groups/binary-arithmetic.rst

DIV
---

.. include:: parameter-groups/binary-arithmetic.rst

MAX
---

.. include:: parameter-groups/binary-arithmetic.rst

MIN
---

.. include:: parameter-groups/binary-arithmetic.rst

EXPRESSION
----------

:bdg-primary:`expression` ``String``

:bdg-success:`variables` ``Map`` < ``String`` : ``Float`` >

Default: Empty map

:bdg-success:`samplers` ``Map`` < ``String`` : ``DimensionApplicableSampler`` >

Default: Empty map

:bdg-success:`functions` ``Map`` < ``String`` : ``MathFunction`` >

Default: Empty map

.. _OpenSimplex2: https://github.com/KdotJPG/OpenSimplex2
.. _gaussian distribution: https://en.wikipedia.org/wiki/Normal_distribution
.. _White noise: https://en.wikipedia.org/wiki/White_noise
.. _Perlin noise: https://en.wikipedia.org/wiki/Perlin_noise
.. _Simplex noise: https://en.wikipedia.org/wiki/Simplex_noise
.. _SDF: https://en.wikipedia.org/wiki/Signed_distance_function
.. _Value noise: https://en.wikipedia.org/wiki/Value_noise
.. _linear interpolation: https://en.wikipedia.org/wiki/Linear_interpolation
.. _bilinear: https://en.wikipedia.org/wiki/Bilinear_interpolation
.. _trilinear: https://en.wikipedia.org/wiki/Trilinear_interpolation
.. _cubic interpolation: https://en.wikipedia.org/wiki/Cubic_Hermite_spline#Interpolation_on_a_single_interval
.. _bicubic: https://en.wikipedia.org/wiki/Bicubic_interpolation
.. _tricubic: https://en.wikipedia.org/wiki/Tricubic_interpolation
.. _Gabor noise: https://graphics.cs.kuleuven.be/publications/GLLD12GNBE/
.. _Worley noise: https://en.wikipedia.org/wiki/Worley_noise