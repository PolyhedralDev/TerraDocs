===================
Image Configuration
===================

This page contains the different ways of defining how an image should
be loaded for use in other configurations requiring the ``Image`` type.

BITMAP
------

Loads a singular image. For very large images that you may have issues loading, 
try the `STITCHED_BITMAP`_ type instead.

:bdg-primary:`path` ``String``
Path to the image relative to the config pack directory.
(For Windows users: Use the ``/`` directory separator instead of ``\``)

STITCHED_BITMAP
---------------

An alternate way of loading ``Image`` s via a set of smaller images
arranged in a grid that are 'stitched' together during generation.
This type is primarily used when singular images are too large to be
loaded into memory (a limit imposed Java's ``BufferedImage`` class implementation).

:bdg-primary:`path-format` ``String``
The format string for the path to the images relative to the config pack directory.
(For Windows users: Use the ``/`` directory separator instead of ``\``)

The file name section of the path format must contain the text ``{row}`` and ``{column}``
indicating the sections of the file names that indicate which rows and columns the files belong to.

Given the following example image files in the pack directory to be stitched into one image:

.. code-block::

    my-config-pack/
    ├── pack.yml
    ├── images
    ┆   └── stitched-image/
            ├ my-image-0-0.png
            ├ my-image-0-1.png
            ├ my-image-1-0.png
            └ my-image-1-1.png

The ``path-format`` to stitch together the images would be: 

.. code-block:: yaml

    path-format: images/stitched-image/my-image-{row}-{column}.png

:bdg-primary:`rows` ``Integer``
How many rows of images to stitch together.

:bdg-primary:`columns` ``Integer``
How many columns of images to stitch together.

:bdg-success:`zero-indexed` ``Boolean``
Should be set to true if the image row and column indexes begin at 0.

Default: ``false``
