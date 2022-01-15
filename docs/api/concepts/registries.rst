==========
Registries
==========

.. javadoc-import::
    com.dfsek.terra.api.registry.meta.RegistryHolder
    com.dfsek.terra.api.config.ConfigPack
    java.lang.Class
    com.dfsek.terra.api.registry.meta.CheckedRegistryHolder
    com.dfsek.terra.api.registry.CheckedRegistry
    com.dfsek.terra.api.registry.Registry
    com.dfsek.terra.api.registry.key.RegistryKey
    com.dfsek.terra.api.registry.key.Namespaced
    com.dfsek.terra.api.registry.key.StringIdentifiable
    com.dfsek.terra.api.registry.key.Keyed
    com.dfsek.terra.api.registry.meta.RegistryProvider

Registries are a very important concept in Terra. They allow Terra, the platform, and other addons to know
your addon's objects exist, and how to identify those objects.

What is a Registry
==================

A registry can be thought of as a map_ of *Registry Keys* to *Entries*. Registries register a particular type
of object, grouping them together. Registries *uniquely identify* their entries, only one entry can exist per key.


What are Registries Used For?
=============================

In Terra, registries are used for referencing items between addons and config packs. They provide a simple way for
addons and configs to create and share data between each other with no special compatibility measures required.

Working with Registries
=======================

Most interactions with the Terra API require working with registries at some point.

Registry Keys
-------------

Registries use :javadoc:`RegistryKey`\s to identify values. Registry Keys consist of a *Namespace* and an *Identifier*.

Registry keys can be created by the ``RegistryKey#parse`` method, to parse a registry key with the ``namespace:id``
syntax. They can also be created with a namespace and ID with the ``RegistryKey#of`` method.

Namespace
^^^^^^^^^

The namespace is the provider of the value being registered, usually your addon or config pack. Objects which hold a
namespace implement the :javadoc:`Namespaced` interface. Namespaced objects can create registry keys in their namespace
via the ``key(String identifier)`` method.

Identifier
^^^^^^^^^^

The identifier is the name of the value itself. Multiple items with the same identifier may exist, so long as they
have different namespaces. Items which provide their own identifiers implement :javadoc:`StringIdentifiable`.

Keyed
^^^^^

The :javadoc:`Keyed` interface is implemented by objects which provide their own Registry Keys.


Getting a Registry
------------------

Registries can be retrieved from objects implementing :javadoc:`RegistryHolder`. Most commonly, this will be a
:javadoc:`ConfigPack`. ``RegistryHolder`` defines several methods for fetching registries, most commonly you'll use
the methods accepting a :javadoc:`Class` instance, and :doc:`Type Keys<type-key>`. There is an unchecked method which
accepts a raw ``Type`` instance, its use is generally discouraged.

Let's get the Structure registry from a config pack instance!

.. literalinclude:: code/registry/structure-registry.java
    :language: java

Getting a Writable Registry
---------------------------

The registry we fetched in the previous example is *read-only*. It's useful for *retrieving* information, but you'll
frequently want to register your own objects. For that, we'll use a :javadoc:`CheckedRegistry`, which can be retrieved
from a :javadoc:`CheckedRegistryHolder` in the same manner as :javadoc:`Registry` can be retrieved from
:javadoc:`RegistryHolder`.

Let's register something!

.. literalinclude:: code/registry/registering.java
    :language: java

Creating a Registry
-------------------

Sometimes, you may wish to create a registry for registering your own objects. Objects which implement
:javadoc:`RegistryProvider` can create :javadoc:`CheckedRegistry` instances via their ``#getOrCreateRegistry`` methods.


.. _map: https://en.wikipedia.org/wiki/Associative_array