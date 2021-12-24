=========
Terra API
=========

Terra implements an advanced platform-agnostic world generation API for extending configuration schemas via addons.
In fact, all of Terra's default config schemas are implemented by addons_.


Addons
======

Addons are extensions to Terra.

Bootstrap Addons
----------------

Bootstrap addons are the only type of addons Terra can load by itself. The bootstrap addon loader is minimal,
depending on the JAR Manifest to locate a single entry point. Bootstrap addons are meant to implement other types
of addon loaders, and should not be used to interface with the whole Terra API.

The Manifest Addon Loader
-------------------------

One of Terra's core addons is the ``manifest-addon-loader`` addon. It loads addons from JAR files, gathering entry
points and metadata from a YAML manifest, ``terra.addon.yml``, at the addon root.

.. _addons: https://github.com/PolyhedralDev/Terra/tree/ver/6.0.0/common/addons


.. toctree::
    :maxdepth: 2
    :titlesonly:

    intro