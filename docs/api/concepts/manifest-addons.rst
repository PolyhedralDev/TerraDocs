===============
Manifest Addons
===============

.. javadoc-import::
    com.dfsek.terra.api.Platform
    com.dfsek.terra.api.addon.BaseAddon
    com.dfsek.terra.api.inject.annotations.Inject
    org.slf4j.Logger

The Manifest Addon Loader is one of the two default bootstrap addons in Terra. The other is the bootstrap addon
loader itself. Any addon that is not itself a bootstrap addon should not use the bootstrap addon loader, so most
addons will want to use the Manifest Addon Loader, as it is included by default.

The Addon Manifest
==================

The addon manifest contains data that the Manifest Addon Loader requires to load the addon. The manifest is a YAML
file at the root of the JAR called ``terra.addon.yml``.

Here is an example addon manifest:

.. literalinclude:: code/manifest-addon/terra.addon.yml
    :language: yaml

Schema Version
--------------

The ``schema-version`` key tells the loader which schema to load this manifest with. The current latest schema
version is ``1``. We try our best to never change the schema version, so your addon manifest should always work,
but the schema-version is there in case we ever need to.

.. note::
    If we ever release a new schema-version, old schema-versions will continue to load (with warnings) for a few
    versions before being removed.

Contributors
------------

The ``contributors`` key is a list of people who have contributed to the addon. For now, just put your name!

ID
--

The ``id`` key is your addon's ID. This ID is used internally to identify your addon, and as your addon's registry
namespace. Make this something concise, but unlikely to conflict with other addons, as **multiple addons cannot have
the same ID!**

Version
-------

The ``version`` key lets the loader know the version of your addon. Versioning is important, because if someone
depends on your addon, they want to be able to guarantee compatibility by specifying the version to depend on!
Terra, like most software, uses `Semantic Versioning <https://semver.org>`__ for its versioning.

Entry Points
------------

The ``entrypoints`` key defines one or more *entry points* to your addon. Entry points are classes which implement
``AddonInitializer``. TODO

Dependencies
------------

The ``depends`` key specifies which other addons you *depend on*. If you depend on an addon:

- That addon initializes before yours.
- Your addon will fail to load if the dependency is not present.
- Your addon will fail to load if the dependency is the wrong version.

The ``depends`` key is a map of addon IDs to version ranges. Version ranges are a way to determine exactly which
versions of the dependency your addons support.

.. list-table:: Example Version Ranges
    :widths: 25 75
    :header-rows: 1

    * - Version Range
      - Versions Included
    * - ``1.0.0``
      - Match *only* version ``1.0.0``
    * - ``[0.1.0, 1.0.0)``
      - Match everything from version ``0.1.0`` (inclusive) to ``1.0.0`` (exclusive)
    * - ``0.1.+``
      - Match all versions from ``0.1.0`` (inclusive) to ``0.2.0`` (exclusive)


Website
-------

The ``website`` key contains a website configuration. This tells users where to find information about the addon
online, where to file bugs, where the source code is, etc. The website key is optional.

There are three sub-keys in the website config:

.. list-table:: Website Keys
    :widths: 25 75
    :header-rows: 1

    * - Key
      - Description
    * - ``source``
      - Where to find the addon's source code.
    * - ``issues``
      - Where to submit bug reports or make feature requests.
    * - ``docs``
      - Where to find documentation about the addon.

License
-------

The ``license`` key tells users the license under which the addon is available. We strongly recommend choosing
an `Open-Source License <https://opensource.org/licenses>`__ to keep with the free and open-source spirit of Terra.

If your license is OSI-approved (MIT, GPLv3, BSD-3, etc.), you can just put the OSI ID in this parameter. Otherwise,
include a link to your license.

.. note::
    If you don't know what license to use just yet, use ``ARR`` as a placeholder. ARR stands for All Rights Reserved,
    which means people aren't allowed to use anything from your addon without your explicit permission. Publishing
    something as ARR is strongly discouraged, so you should look into switching to an OSI license before
    releasing your addon!

Working with Entry Points
=========================

The addon manifest's `Entry Points`_ key defines a list of entry points of the addon. These entry points
are references to classes which implement ``AddonInitializer``. These entry points are initialized sequentially
when the addon initializes.

.. _di-in-entry-points:

Dependency Injection in Entry Points
------------------------------------

The Manifest Addon Loader injects the following types into entry points:

- The :javadoc:`Platform` instance
- The :javadoc:`BaseAddon` instance
  (In Manifest Addons, the :javadoc:`BaseAddon` instance is separate from the entry points, as the addon can have
  multiple entry points, hence the ability to inject the addon instance into entry points)
- A :javadoc:`Logger` instance specific to the entry point

Read more about :doc:`dependency injection <dependency-injection>` in the main article.