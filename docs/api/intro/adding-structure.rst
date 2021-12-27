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

In this tutorial, we'll be creating and registering a structure that can generate in the world.

Structures
==========

The structure interface represents a *structure* that can generate in the world; a section of blocks
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