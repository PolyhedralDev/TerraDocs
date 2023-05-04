===========================
Color Sampler Configuration
===========================

A color sampler is a config defined function that assigns a color for every XZ coordinate pair.
Color samplers are typically used to distribute things across the entire world by utilizing color data,
for example using a heightmap to shape terrain, or an image to draw where biomes should go.

Color samplers differ from :doc:`image` s in that they can provide colors for any XZ coordinate, whereas
``Image`` s only work with a set size. 

Color Sampler Categories
========================

.. container:: nested-cards

    .. card:: **Generative Color Samplers**

        Color samplers that provide color data.

        - `COLOR`_

        .. card:: **Image Color Samplers**

            Color samplers that source color data from image(s).

            - `SINGLE_IMAGE`_
            - `TILED_IMAGE`_

    .. card:: **Mutator Color Samplers**

        Color samplers that take other samplers as inputs and manipulate their outputs in some way.

        - `ROTATE`_
        - `TRANSLATE`_

Color Sampler Types
===================

COLOR
-----

Provides the same color for any input.

:bdg-primary:`color` ``Color``
The color to output.

SINGLE_IMAGE
------------

Outputs the pixels of an ``Image``, colors for coordinates outside the bounds of the image
are provided by a 'fallback' color sampler, which typically will be the `COLOR`_ type.

.. include:: parameter-groups/image-color-sampler.rst

:bdg-success:`outside-sampler` ``ColorSampler``
The sampler that provides colors for coordinates outside the bounds of the ``Image`` .

TILED_IMAGE
-----------

Outputs a repeating grid of pixels sourced from the provided ``Image`` .

.. include:: parameter-groups/image-color-sampler.rst

ROTATE
------

.. include:: parameter-groups/mutate-color-sampler.rst

:bdg-primary:`angle` ``Float``

TRANSLATE
---------

.. include:: parameter-groups/mutate-color-sampler.rst

:bdg-primary:`x` ``Integer``

:bdg-primary:`y` ``Integer``

