==================
Adding a Structure
==================

.. javadoc-import::
    com.dfsek.terra.api.structure.Structure
    com.dfsek.terra.api.world.WritableWorld
    com.dfsek.terra.api.block.state.BlockState
    com.dfsek.terra.api.handle.WorldHandle
    com.dfsek.terra.api.Platform
    java.lang.String
    com.dfsek.terra.api.util.generic.Lazy
    com.dfsek.terra.api.registry.key.Keyed
    com.dfsek.terra.api.registry.key.RegistryKey
    java.lang.Comparable
    com.dfsek.terra.api.event.events.config.pack.ConfigPackPreLoadEvent
    com.dfsek.terra.api.registry.key.Namespaced
    com.dfsek.terra.api.addon.BaseAddon
    com.dfsek.terra.api.config.ConfigPack


In this tutorial, we'll be creating and registering a structure that can generate in the world.

Structures
==========

The Structure interface represents a *structure* that can generate in the world; a section of blocks
that generate at a location. Some examples of where structures may be used are:

- Grass
- Flowers
- Trees
- Rocks

Structures are generally used to decorate the world after generation.


Creating a Structure
====================

To create a structure, create a new class and implement the :javadoc:`Structure` interface. In this tutorial, we'll
call our example structure ``com.example.addon.structure.ExampleStructure``. You can call yours whatever you want!

.. literalinclude:: code/adding-structure/example-structure.java
    :language: java

Generating Something
====================

Right now, our ``Structure`` implementation won't generate anything. To generate blocks in the world, we can use one
:javadoc:`WritableWorld`'s many ``#setBlockState`` methods. Let's generate a tree!

Getting a Block State
---------------------

First, we'll need to get a :javadoc:`BlockState` to generate. To do that, we'll need the :javadoc:`WorldHandle`,
which we can get from the :javadoc:`Platform` instance. Let's pass the ``Platform`` into our ``Structure``'s
constructor, and use :javadoc:`WorldHandle#createBlockState(String)` to create a block state!

.. literalinclude:: code/adding-structure/get-block-data.java
    :language: java

.. note::
    If you're used to the Bukkit API, Terra's :javadoc:`BlockState` is roughly equivalent to Bukkit's ``BlockData``.
    We chose the name Block State as it is more accurate to what the object represents, as well as the name
    Minecraft itself uses internally.

.. warning::
    If you're implementing a structure in your addon, you'll definitely want to get your block state *once* on
    initialization, then use the existing instance in your structure's ``#generate`` method.
    We're getting them in the ``#generate`` method to make this tutorial simpler.


    It's generally encouraged to make the block state configurable, as that keeps your addon platform-agnostic,
    but if you're set on hard-coding your block states, you can:

    - Initialize them in the structure's constructor.
    - Initialize them in your addon's entry point and pass them to the structure.
    - Use the :javadoc:`Lazy` utility class for lazy initialization.

Generating Blocks
-----------------

Now that we have a block state, let's place it in the world! To do that, we'll use the ``#setBlockState`` methods of
:javadoc:`WritableWorld`. Let's generate a simple tree by generating some leaves, then generating a stick through them:

.. literalinclude:: code/adding-structure/tree.java
    :language: java

.. note::
    If you're used to the Bukkit API, you may be looking for Terra's equivalent to the ``Location`` class, which
    combines a ``World`` and a ``Vector3``. The Terra API has no such class. Separating the world from the
    position allows for much cleaner integration of more world types.

    The Terra API also lacks an analogous class to Bukkit's ``Block``, for the same reason. Bukkit's ``Block`` is
    an even messier combination of a ``World``, a ``Vector3Int`` *and* a ``BlockState``.

Registering the Structure
=========================

Now that we've made our structure, if you compile and install the addon, you'll see that... nothing happens. That's
because we haven't *registered* our structure. If we don't register the structure, Terra doesn't know it exists.

Implementing Keyed
------------------

While it's entirely possible to register things by providing a :javadoc:`RegistryKey` instance, it's generally
cleaner to implement the :javadoc:`Keyed` interface in the object you want to register. This will become especially
apparent when you're registering many of the same type of object at once. The pattern to implement keyed is generally

``class Thing implements Keyed<Thing>``.

If you've worked with :javadoc:`Comparable`, the idea is similar; the type parameter of ``Keyed`` should almost
always be the same as the class it's implemented in.

Let's implement ``Keyed`` in our example structure:

.. literalinclude:: code/adding-structure/keyed.java
    :language: java

When an object implements ``Keyed``, it must provide an instance of :javadoc:`RegistryKey`, the key that identifies it.
We'll get that instance by putting it in a field set in the constructor.


Creating a Key
--------------

Now that we have a ``Keyed`` structure, let's register it! Back in our entry point, let's revisit our
:javadoc:`ConfigPackPreLoadEvent` listener.

First, let's create an instance to register. Our structure requires the :javadoc:`Platform` instance, and a unique
:javadoc:`RegistryKey` instance.

- We have the ``Platform`` instance from dependency injection.
- We can create a ``RegistryKey`` instance from any object which implements :javadoc:`Namespaced`. In this case, we
  want to use the namespace of our addon, so let's use the :javadoc:`BaseAddon` instance (which we've also injected)
  to create a key:

  .. literalinclude:: code/adding-structure/get-key.java
      :language: java

Now that we have both objects required to instantiate our structure, let's create an instance:

.. literalinclude:: code/adding-structure/instantiate-structure.java
    :language: java

Registering the Instance
------------------------

Now that we have an instance, we can finally register it! To do that, we'll need a registry. We can get that from the
:javadoc:`ConfigPack` provided by :javadoc:`ConfigPackPreLoadEvent`:

.. literalinclude:: code/adding-structure/get-pack.java
    :language: java

We can then get a registry using ``#getOrCreateRegistry``. We want the :javadoc:`Structure` registry, so let's get
it!

.. literalinclude:: code/adding-structure/get-structure-registry.java
    :language: java

Now that we have the structure registry, we can finally register our structure instance with ``#register``!

.. literalinclude:: code/adding-structure/register-structure.java
    :language: java

Including the Structure in World Generation
===========================================

Now that our structure is registered, it can be used in world generation. Let's add it to a config pack!

Creating a Feature
------------------

Use this feature config to create a *feature* that generates your structure:

.. literalinclude:: code/adding-structure/feature.yml
    :language: yaml

.. warning::
    The ``generation-stage-feature``, ``config-feature``, ``config-locators``, and ``config-distributors`` core addons
    are required for this config! These are all core addons, included by default in Terra, but if you made your
    own pack, be sure to depend on them!

Including the Feature in a Biome
--------------------------------

Now, simply include your new feature in a biome by adding it to the ``features`` key! Here's an example of adding it
to the default pack's ``PLAINS`` biome:

.. literalinclude:: code/adding-structure/feature-in-biome.yml
    :language: yaml


Conclusion
==========

Now launch your Terra installation, and when you create a new world, you should see your structure generating in the
biome you chose!

.. image:: /img/api/intro/structure/generation.png

You're now able to create and register objects to Terra's registries!