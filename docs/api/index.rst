=========
Terra API
=========

Terra implements an advanced platform-agnostic world generation API for extending configuration schemas via addons.
In fact, all of Terra's default config schemas are implemented by addons_.


Addons
======

Addons are extensions to Terra. On its own, Terra is just an API with some platform implementations, addons and
configurations are required to implement any functionality. Addons create the config schemas which configurations
then use to implement functionality.

Sometimes, an addon may directly implement something rather than delegating it
to a config, though generally configuration is encouraged.


.. _addons: https://github.com/PolyhedralDev/Terra/tree/ver/6.0.0/common/addons


.. toctree::
    :maxdepth: 2
    :titlesonly:

    intro/index