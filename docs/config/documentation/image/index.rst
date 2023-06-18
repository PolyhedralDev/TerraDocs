===================
Image Configuration
===================

This page contains documentation for configurations related to the ``library-image`` addon.

Overview
========

The generation process via ``library-image`` typically follows a two-step process: 1) retrieve a
color value from 2D coordinates, and 2) convert that color to something else such as a biome or a
height value for use in world generation.

.. graphviz:: diagram/overview.dot
   :align: center

Image Configurations
--------------------

An :doc:`image configuration <image>` defines how Terra should load image data, typically this
is as simple as defining the path to the image. Image configs are used by other configs related
to ``library-image`` to source colors for use in generation.

Color Samplers
--------------

The configuration type primarily responsible for the first step of retriving color values is called a
:doc:`color sampler <color-sampler>`. Color samplers differ from image configurations in that they can
provide colors for an infinite* space, whereas image configurations are limited to operating within a
set width and height. In some cases a config may use just a image configuration directly to source
colors rather than a color sampler.

Color samplers may utilize image configurations to source color data, but can also do things
like translate where images will generate in world space. Color samplers operate similarly to how
:doc:`noise samplers </config/documentation/sampler/index>` do, with the key difference being that color
samplers output colors rather than numbers.

.. graphviz:: diagram/color-sampler-abstract.dot
   :align: center

Color Conversion
----------------

The second step of converting the color to something else is configured differently depending on the particular
use case. You can find documentation for relevant configs below under `Application Specific Configs`_.

Index
=====

General Configs
---------------

.. toctree::
    :maxdepth: 1

    color-sampler
    image

Application Specific Configs
----------------------------

.. toctree::
    :maxdepth: 1

    noise-samplers
    image-biome-provider-v2
    pipeline-image-source

