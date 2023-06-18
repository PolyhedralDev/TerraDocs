==================================
Image Noise Sampler Configurations
==================================

.. container:: nested-cards

   .. card::

        - `CHANNEL`_
        - `DISTANCE_TRANSFORM`_

Noise Sampler Types
===================

CHANNEL
-------

Outputs a channel from a color sampler.

:bdg-primary:`color-sampler` ``ColorSampler``
The color sampler to extract channel values from.

:bdg-success:`normalize` ``Boolean``
If the channel should be normalized to range [-1, 1] or not.

Default: ``true``

:bdg-success:`premultiply` ``Boolean``
Whether to multiply color channels by the alpha channel or not. If you
are expecting pixel transparency to reduce the output value then this should
be set to true.

Default: ``false``

DISTANCE_TRANSFORM
------------------

Returns the result of a `distance transform <https://homepages.inf.ed.ac.uk/rbf/HIPR2/distance.htm>`_ on an image.

:bdg-primary:`image` ``Image``

:bdg-success:`threshold` ``Integer``

Default: ``127``

:bdg-success:`clamp-to-max-edge` ``Boolean``

Default: ``false``

:bdg-success:`channel` ``Channel``

Default: ``GRAYSCALE``

:bdg-success:`cost-function` ``String``

- ``Channel``
- ``Threshold``
- ``ThresholdEdge``
- ``ThresholdEdgeSigned``

Default: ``Channel``

:bdg-success:`invert-threshold` ``Boolean``

Default: ``false``

:bdg-success:`Normalization` ``String``

- ``None``
- ``Linear``
- ``SmoothPreserveZero``

Default: ``None``
