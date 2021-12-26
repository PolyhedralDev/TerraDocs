===================
Terra Addon Loading
===================

.. javadoc-import::
    com.dfsek.terra.api.addon.bootstrap.BootstrapBaseAddon
    com.dfsek.terra.api.Platform

This page serves as an explanation of the addon loading process in Terra. None of the information on this page is
strictly necessary for developing a Terra addon, so feel free to skim. However, knowing how the addon loading
process works can be helpful.

The Terra addon loading process can be divided into 2 main steps:

1. Bootstrap Addon Loading
==========================

The only addons Terra itself is capable of loading are Bootstrap Addons. The bootstrap addon loader is an extremely
minimal addon loader; it checks the JAR Manifest of all discovered bootstrap addons (from the ``addons/bootstrap``
directory) for the ``Terra-Bootstrap-Addon-Entry-Point`` attribute, then attempts to load and instantiate the
:javadoc:`BootstrapBaseAddon`-implementing class specified in the attribute.

Bootstrap Addon Initialization
------------------------------

After all bootstrap addons are loaded, the ``#initialize`` method is invoked on each. During initialization, bootstrap
addons load additional addons, but *does not initialize them*.

2. Addon Initialization
=======================

After the bootstrap addons have loaded their addons, the freshly loaded addons must be initialized.

Dependency Sorting
------------------

First, addons' dependencies are inspected. If any dependencies are missing, any invalid versions are found, or any
circular dependencies arise, loading fails.

Addons are then sorted into a `directional acyclic graph`_ based on their dependencies. The graph is used to determine
the order in which addons are loaded, to ensure dependencies are loaded before dependents.

.. _directional acyclic graph: https://en.wikipedia.org/wiki/Directed_acyclic_graph

Initialization
--------------

After the order to load addons is determined, addons can finally be initialized.

Dependency Injection
....................

Terra's addon system makes use of a simple annotation-based dependency injection framework to reduce boilerplate.
When addons are initialised, the :javadoc:`Platform` instance is injected to any valid, annotated fields.


