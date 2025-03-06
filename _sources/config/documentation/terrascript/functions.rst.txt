=====================
TerraScript Functions
=====================

Terra’s TerraScript implementation contains many functions for
interacting with the world, getting and setting data, and debugging.

.. _function-block:

block
-----

The block function sets a block at a location.

Arguments:

+------------------------+---------------+-------------------------------+
| Parameter              | Type          | Description                   |
+========================+===============+===============================+
| ``x``                  | ``num``       | X coordinate (relative to     |
|                        |               | origin) to place block        |
+------------------------+---------------+-------------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to     |
|                        |               | origin) to place block        |
+------------------------+---------------+-------------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to     |
|                        |               | origin) to place block        |
+------------------------+---------------+-------------------------------+
| ``data``               | ``str``       | Block Data string to place    |
|                        |               | (must be constant             |
|                        |               | expression)                   |
+------------------------+---------------+-------------------------------+
| ``replace``            | ``bool``      | (Optional; Default: ``true``) |
|                        |               | Whether to replace an         |
|                        |               | existing block. This is       |
|                        |               | true. When true, any block    |
|                        |               | will be overwritten (this     |
|                        |               | is the default behavior       |
|                        |               | when this parameter is        |
|                        |               | unspecified) When false,      |
|                        |               | only air will be              |
|                        |               | overwritten.                  |
+------------------------+---------------+-------------------------------+
| ``physics``            | ``bool``      | (Optional; Default: ``false``)|
|                        |               | Whether to tick update the    |
|                        |               | block after the initial       |
|                        |               | chunk generation. Allows      |
|                        |               | blocks like water to          |
|                        |               | flow or sand to fall          |
|                        |               | when placed.                  |
+------------------------+---------------+-------------------------------+

Returns: ``VOID``

.. _function-check:

check
-----

The check function checks the “type” of a location. It is a fast way to
tell whether a location is in the air, ocean, or ground. While it cannot
provide specific block state information, it is much faster than
``getBlock``, and does not force-load chunks it is used in. It is
recommended to avoid ``getBlock`` in regular structures, and use
``check`` whenever possible.

Arguments:

+------------------------+---------------+-------------------------------+
| Parameter              | Type          | Description                   |
+========================+===============+===============================+
| ``x``                  | ``num``       | X coordinate (relative to     |
|                        |               | origin) to check              |
+------------------------+---------------+-------------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to     |
|                        |               | origin) to check              |
+------------------------+---------------+-------------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to     |
|                        |               | origin) to check              |
+------------------------+---------------+-------------------------------+

Returns: ``STRING`` - The type of the location at the parameter
coordinates, added to the structure origin. **Must** be one of the following:

* ``AIR`` - The location is air.
* ``LAND`` - The location is in the land.
* ``OCEAN`` - The location is in the ocean.

.. _function-structure:

structure
---------

The structure function generates another :doc:`structure </config/documentation/objects/Structure>` within the current
structure, with an offset origin and rotation.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to place structure  |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to place structure  |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to place structure  |
+------------------------+---------------+-----------------------------+
| ``structure``          | ``str``       | ID of structure to generate |
|                        |               | (equal to the ``id``        |
|                        |               | statement of that           |
|                        |               | structure’s script)         |
+------------------------+---------------+-----------------------------+
| ``rotation``           | ``str...``    | Rotations to generate this  |
|                        |               | structure with. One of      |
|                        |               | these rotations will be     |
|                        |               | randomly selected. Valid    |
|                        |               | rotations are: ``NONE`` (No |
|                        |               | rotation), ``CW_90``        |
|                        |               | (Clockwise 90 degrees),     |
|                        |               | ``CCW_90``                  |
|                        |               | (Counterclockwise 90        |
|                        |               | degrees), and ``CW_180``    |
|                        |               | (180 degrees)               |
+------------------------+---------------+-----------------------------+

``...`` in the ``rotation`` parameter type description means that it
is a *vararg* parameter - it may contain any number of values.

Returns: ``BOOlEAN`` - ``true`` if structure successfully generated,
``false`` if generation failed.

.. _function-randomInt:

randomInt
---------

The randomInt function returns a random value within a range.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``range``              | ``num``       | Maximum value (exclusive)   |
+------------------------+---------------+-----------------------------+

Returns: ``NUMBER`` - A random integer (whole number) between ``0``
(inclusive) and ``range`` (exclusive).

For example, ``randomInt(10)`` would return a number from ``0`` to ``9``.

.. _function-recursions:

recursions
----------

The recursions function gets the number of recursions that have occurred
prior to the generation of the structure. It is incredibly useful for
preventing infinite recursion in recursive structures.

Arguments: none

Returns: ``NUMBER`` - The number of recursions that have occurred.

If ``structure_a`` is generates ``structure_b`` via the ``structure``
function, ``recursions()`` would return ``0`` in ``structure_a``, then
``1`` in ``structure_b``. If ``structure_b`` then generated
``structure_a`` again, ``recursions()`` would return ``2`` *in the
second instance of ``structure_a`` only*.

.. _function-setMark:

setMark
-------

The setMark function is one of two functions for interacting with Marks,
which allow data to be stored in structures and accessed later, without
affecting generation. A Mark is a string assigned to a location in a
structure. It is set by the ``setMark`` function, and then can be
retrieved by the ``getMark`` function. One possible use case includes
marking locations where structures generate, then checking them with
``getMark`` to ensure structures do not overlap.

Marks set in recursive structures are visible by parent structures. if
``structure_a`` generates ``structure_b`` via the ``structure``
function, and ``structure_b`` sets a mark, ``structure_a`` can retrieve
that mark. Marks are set relative to the added origins of all
recursions.

Setting a mark that already exists will overwrite it with a new value.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to set mark         |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to set mark         |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to set mark         |
+------------------------+---------------+-----------------------------+
| ``content``            | ``str``       | Content of the mark         |
|                        |               | to place                    |
+------------------------+---------------+-----------------------------+

Returns: ``VOID``

.. _function-getMark:

getMark
-------

The getMark function is one of two functions for interacting with Marks,
which allow data to be stored in structures and accessed later, without
affecting generation. A Mark is a string assigned to a location in a
structure. It is set by the ``setMark`` function, and then can be
retrieved by the ``getMark`` function. One possible use case includes
marking locations where structures generate, then checking them with
``getMark`` to ensure structures do not overlap.

Marks set in recursive structures are visible by parent structures. if
``structure_a`` generates ``structure_b`` via the ``structure``
function, and ``structure_b`` sets a mark, ``structure_a`` can retrieve
that mark. Marks are set relative to the added origins of all
recursions.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to check mark       |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to check mark       |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to check mark       |
+------------------------+---------------+-----------------------------+

Returns: ``STRING`` - The content of the mark at the location. Returns
``""`` (empty string) if the mark is empty or not present.

.. _function-pull:

pull
----

The pull function sets a block at a location, then “pulls” it down to
ground. The pull function will search at the specified location, then
downwards, until the block is **not** air.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to place block      |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to start search     |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to place block      |
+------------------------+---------------+-----------------------------+
| ``data``               | ``str``       | Block Data string to place  |
|                        |               | (must be constant           |
|                        |               | expression)                 |
+------------------------+---------------+-----------------------------+

Returns: ``VOID``

.. _function-loot:

loot
----

The loot function populates a container with loot. A container is any
block with an inventory (chests, shulker boxes, furnaces, brewing
stands, etc.)

Arguments:

+------------------------+---------------+-------------------------------+
| Parameter              | Type          | Description                   |
+========================+===============+===============================+
| ``x``                  | ``num``       | X coordinate (relative to     |
|                        |               | origin) to fill loot          |
+------------------------+---------------+-------------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to     |
|                        |               | origin) to fill loot          |
+------------------------+---------------+-------------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to     |
|                        |               | origin) to fill loot          |
+------------------------+---------------+-------------------------------+
| ``table``              | ``str``       | Filename of the loot table,   |
|                        |               | relative to                   |
|                        |               | ``pack/structures/loot``.     |
|                        |               |                               |
|                        |               | Example:                      |
|                        |               | ``village/village_house.json``|
+------------------------+---------------+-------------------------------+

Returns: ``VOID``

.. _function-entity:

entity
------

The entity function spawns an entity at a location.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to spawn entity     |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to spawn entity     |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to spawn entity     |
+------------------------+---------------+-----------------------------+
| ``entity``             | ``str``       | Entity ID to spawn          |
+------------------------+---------------+-----------------------------+

Returns: ``VOID``

.. _function-getBiome:

getBiome
--------

The getBiome function gets the Terra biome at a location.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to check biome      |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to check biome      |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to check biome      |
+------------------------+---------------+-----------------------------+

Returns: ``STRING`` - The ID of the biome, E.G. ``"ARID_MOUNTAINS"``.

.. _function-getBlock:

getBlock
--------

The getBlock function checks the Block State at a location. **It should
NOT be used in regular structures!**

The getBlock function force-loads chunks when it runs. This is fine in
trees, which load chunks anyways, but in regular structures it will
cause cascading chunk loading whenever a structure generates. **Use the
``check`` function instead in regular structures!**

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) to check block      |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) to check block      |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) to check block      |
+------------------------+---------------+-----------------------------+

Returns: ``STRING`` - The ID of the block, without properties, E.G.
``"minecraft:stone"``.

.. _function-state:

state
-----

The state function manipulates NBT data on block entities (like signs
and mob spawners).

Data is formatted as ``"key1=value1,key2=value2"``. E.G.
``"text1=hello,text2=world"`` applied to a sign would cause the sign to
read:

::

   hello
   world

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``x``                  | ``num``       | X coordinate (relative to   |
|                        |               | origin) of block            |
+------------------------+---------------+-----------------------------+
| ``y``                  | ``num``       | Y coordinate (relative to   |
|                        |               | origin) of block            |
+------------------------+---------------+-----------------------------+
| ``z``                  | ``num``       | Z coordinate (relative to   |
|                        |               | origin) of block            |
+------------------------+---------------+-----------------------------+
| ``data``               | ``str``       | Data to apply to block      |
+------------------------+---------------+-----------------------------+

Returns: ``VOID``

.. _function-print:

print
-----

The print function prints a string to the console. It is a debug
function, and as such will only work with debug mode enabled.

Arguments:

+------------------------+---------------+-----------------------------+
| Parameter              | Type          | Description                 |
+========================+===============+=============================+
| ``message``            | ``str``       | Message to print to console |
+------------------------+---------------+-----------------------------+

Returns: ``VOID``

.. _function-sampler:

sampler
-------

The sampler function allows for a cached :doc:`noise sampler </config/documentation/objects/NoiseSampler>`
of a config pack to be used within TerraScript and output noise values.

Arguments:

+------------------------+------------+-----------------------------------------+
| Parameter              | Type       | Description                             |
+========================+============+=========================================+
| ``sampler``            | ``str``    | ID of noise sampler                     |
|                        |            |                                         |
+------------------------+------------+-----------------------------------------+
| ``x``                  | ``num``    | X coordinate (relative to origin)       |
|                        |            | for noise input                         |
+------------------------+------------+-----------------------------------------+
| ``z``                  | ``num``    | Z coordinate (relative to origin)       |
|                        |            | for noise input                         |
+------------------------+------------+-----------------------------------------+
| ``y``                  | ``num``    | (Optional)                              |
|                        |            | Y coordinate (relative to origin)       |
|                        |            | for noise input                         |
+------------------------+------------+-----------------------------------------+

Returns: ``num`` - value output of :doc:`noise sampler </config/documentation/objects/NoiseSampler>`.

Provided by the ``terrascript-function-sampler`` addon.