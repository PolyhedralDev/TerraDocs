====================
Config Documentation
====================

.. seealso::

    :doc:`/config/development/index` :octicon:`chevron-right`

    :doc:`/config/development/config-data` :octicon:`chevron-right`

    :doc:`/config/development/config-files` :octicon:`chevron-right`

    :doc:`/config/development/config-system` :octicon:`chevron-right`

Configuration Files
===================

.. .. toctree::
..     :maxdepth: 1
..     :glob:

..     files/*

Object Configs
==============

.. toctree::
    :maxdepth: 1
    :glob:
    :hidden: 

    objects/*

.. _config-documentation-format:

Documentation Format
====================

Configs are documented in the following format:

.. container:: nested-cards

    .. card::

        .. include:: examples/config.rst

\*Some documented configs may not contain any optional parameters and or an
example config.

Config Specific Objects
-----------------------

Some parameters may require a type specific to that particular config. In
these cases, the documentation of that contained type will be included in
the main config's documentation:

.. container:: nested-cards

    .. card::

        .. include:: examples/subtype.rst
