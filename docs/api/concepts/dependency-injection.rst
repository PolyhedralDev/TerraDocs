.. _dependency-injection:

====================
Dependency Injection
====================

.. javadoc-import::
    com.dfsek.terra.api.Platform
    com.dfsek.terra.api.addon.BaseAddon
    com.dfsek.terra.api.inject.annotations.Inject
    org.slf4j.Logger

Terra uses a simple annotation-based dependency injection framework to provide instances of important API objects
to addons. The dependency injection framework reduces boilerplate by allowing addons to choose which objects they
need to have access to.

Injecting to a Field
====================

To inject to a field, simply make the field non-final and non-static, and annotate it :javadoc:`Inject`.

Example
-------

.. literalinclude:: code/dependency-injection.java
    :language: java

This example demonstrates injecting the :javadoc:`Platform` and :javadoc:`BaseAddon` instances. This is a very common
scenario, as both of these objects are required for :ref:`handling events<handling-events>`

Dependency Injection in all Addons
==================================

The :javadoc:`Platform` instance is injected into all addons.

Dependency Injection in the Manifest Addon Loader
=================================================

The Manifest Addon Loader injects additional types into its entry points, to simplify addon development.

- The :javadoc:`Platform` instance
- The :javadoc:`BaseAddon` instance
  (In Manifest Addons, the :javadoc:`BaseAddon` instance is separate from the entry points, as the addon can have
  multiple entry points, hence the ability to inject the addon instance into entry points)
- A :javadoc:`Logger` instance specific to the entry point




