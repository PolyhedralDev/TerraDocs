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

.. include:: parameter-groups/noise.rst

POSITIVE_WHITE_NOISE
--------------------

.. include:: parameter-groups/noise.rst

GAUSSIAN
--------

.. include:: parameter-groups/noise.rst

PERLIN
------

.. include:: parameter-groups/noise.rst

SIMPLEX
-------

.. include:: parameter-groups/noise.rst

OPEN_SIMPLEX_2
--------------

.. include:: parameter-groups/noise.rst

OPEN_SIMPLEX_2S
---------------

.. include:: parameter-groups/noise.rst

VALUE
-----

.. include:: parameter-groups/noise.rst

VALUE_CUBIC
-----------

.. include:: parameter-groups/noise.rst

GABOR
-----

.. include:: parameter-groups/noise.rst

:bdg-success:`rotation` ``Float``

:bdg-success:`isotrophic` ``Boolean``

:bdg-success:`deviation` ``Float``

:bdg-success:`impulses` ``Float``

:bdg-success:`frequency_0` ``Float``

CELLULAR
--------

Produces noise derived from an infinite grid of 'cells'.

.. image:: /img/concepts/noise/cellular_256x256.png

**DIAGRAM**

.. image:: /img/concepts/noise/cellular_diagram.svg

- Black dots: The center of each cell.
- Red lines: A random direction and distance from the cell center, called 'jitter'.
- Blue dots: The cell origin, determined by jitter from the cell center.

**PARAMETERS**

.. include:: parameter-groups/noise.rst

:bdg-success:`distance` ``String``
The method used for calculating the distance from the cell origin. Only relevant
for ``return`` types 

Default - ``EuclideanSq``

Distance types:

- ``Euclidean``
- ``EuclideanSq``
- ``Manhattan``
- ``Hybrid``

:bdg-success:`return` ``String``
The function the sampler will use to calculate the noise.

Default - ``Distance``

Return types:

- ``CellValue`` - Returns a random value based on the nearest cell origin.
- ``Distance`` - Returns the distance from the nearest cell origin.
- ``Distance2``
- ``Distance2Add``
- ``Distance2Sub``
- ``Distance2Mul``
- ``Distance2Div``
- ``NoiseLookup`` - Passes the coordinates of the nearest cell origin into a sampler, and returns the output.
- ``Distance3``
- ``Distance3Add``
- ``Distance3Sub``
- ``Distance3Mul``
- ``Distance3Div``
- ``Angle`` - Returns the angle from the sampled coordinates to the nearest cell origin in radians.


:bdg-success:`jitter` ``Float``
Determines how far cell origins can randomly spread out from the ceneter of cells.

A jitter of ``0`` places cell origins exactly in the center of each cell, resulting in a perfect grid.
Values between ``-1`` and ``1`` are recommended, as values outside that range may produce artifacts.

:bdg-success:`lookup` ``Sampler``
The lookup sampler used when the ``distance`` parameter is set to ``NoiseLookup``

IMAGE
-----

:bdg-primary:`image` ``String``

:bdg-primary:`frequency` ``Float``

:bdg-primary:`channel` ``String``

CONSTANT
--------

Outputs a constant value, regardless of the inputs.

:bdg-success:`value` ``Float``
The value to be outputted.

DOMAIN_WARP
-----------

Warps a sampler by another sampler. See :ref:`Domain Warping <domain-warping>` for more information.

:bdg-primary:`warp` ``Sampler``

:bdg-primary:`sampler` ``Sampler``

:bdg-success:`amplitude` ``Float``

KERNEL
------

:bdg-primary:`kernel` ``List`` of ``List`` of ``Float``

:bdg-primary:`sampler` ``Sampler``

:bdg-success:`factor` ``Float``

:bdg-success:`frequency` ``Float``

LINEAR_HEIGHTMAP
----------------

:bdg-primary:`base` ``Float``

:bdg-success:`sampler` ``Sampler``

:bdg-success:`scale` ``Float``

FBM
---

.. include:: parameter-groups/fractalizer.rst

PING_PONG
---------

.. include:: parameter-groups/fractalizer.rst

:bdg-success:`ping-pong` ``Float``

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

:bdg-success:`samplers` ``Map`` < ``String`` : ``DimensionApplicableSampler`` >

:bdg-success:`functions` ``Map`` < ``String`` : ``MathFunction`` >
