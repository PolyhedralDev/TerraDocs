============
Config Files
============

The majority of config development involves creating and manipulating
`configuration
files <https://en.wikipedia.org/wiki/Configuration_file>`__. *In the
context of config development*, configuration files (or simply
*configs*) are files contained within a `config pack <./Config-Packs>`__
that define data that Terra uses to determine how worlds generate.

File Formats
============

Typically, configuration file formats in applications are based on
`data-serialization
languages <https://en.wikipedia.org/wiki/Serialization>`__ such as JSON,
XML, and YAML.

In Terra the file formats used in config packs are flexible, as the
functionality for reading and parsing different formats is provided via
addons - this allows flexibility for developers to use whatever format
they're most comfortable in. Files contained inside a `config
pack <./Config-Packs>`__ will only attempt to load as configuration
files if a **language addon** is installed that supports the file type.

YAML
----

The standard file format / language supported in Terra configurations is
`YAML <https://en.wikipedia.org/wiki/YAML>`__, as support for it comes
pre-installed as a language addon with standard Terra releases. Because
of this, YAML will be the primary language used in examples and guides
on this wiki.

The YAML language addon attempts to load all text files with the
extension ``.yml`` contained inside config packs, which are required
to abide by the `YAML spec <https://yaml.org/spec/>`__ in order to
load correctly.

.. _create-config-file:

Creating a Config File
======================

If you have not installed any other language addons, the assumed process
of creating a standard config file simply involves creating a new text
file with the extension ``.yml``.

Otherwise, when prompted to create a new config file, it is implied that
you should create a new file using a format supported by your installed
*language addon(s)*.

Config File Organization
------------------------

As a general rule of thumb, a config file's file name and subdirectory
within the config pack is mostly ignored by Terra. Because of this
you're free to name your config files however you want and organize them
in whatever directory structure you'd like. The pack manifest is the one
exception, and is required to be defined directly in the pack directory,
using the name ``pack`` (excluding the file extension).