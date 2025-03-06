=======================
What TerraScript Can Do
=======================

World Manipulation
------------------
TerraScript has many features that allow for the manipulation of the world that include:

* :ref:`Setting blocks <function-block>`.
* :ref:`Setting block NBT data <function-state>` (Spawner NBT data, sign NBT data, etc).
* :ref:`Setting blocks to auto-pull to the ground <function-pull>`.
* :ref:`Spawning entities <function-entity>`.
* :ref:`Applying loot tables to inventories <function-loot>`. ``In Development``

World Data Reading
------------------
TerraScript is also capable of reading data from the world in different ways
to allow for efficient structure generation that include:

* :ref:`Reading location types <function-check>` (``AIR``, ``LAND``, or ``OCEAN``) for fast checking and spawn validation.
* :ref:`Reading block states <function-getBlock>` for slower, but more accurate checking.
* :ref:`Setting Marks <function-setMark>` that allow scripts to “mark” locations, then :ref:`check marks <function-getMark>` later in a way that does not affect generation.

Recursive Scripting
-------------------
One powerful capability of TerraScript is the ability to generate
scripts recursively with functions to:

* :ref:`Invoke other scripts <function-structure>` at offset locations within the current script, and check whether the sub-structure was successfully generated
* :ref:`Check the amount of recursions <function-recursions>` in the current script

Essential Language Features
---------------------------
TerraScript utilizes essential language features that include:

* :doc:`String</config/documentation/objects/String>`, :doc:`Integer</config/documentation/objects/Integer>`, and :doc:`Boolean</config/documentation/objects/Boolean>` variables
* ``if`` ``else if`` and ``else`` statements
* ``for`` and ``while`` loops along with flow control statements (``continue`` ``break`` and ``return``)

Example Use Cases
-----------------
In the overworld config pack that comes pre-packaged with Terra, TerraScript is utilized for:

* Vegetation features such as trees, giant mushrooms, and giant bushes for various variations.
* Landform features such as boulders, fossils, and icebergs for various variations.
* Dynamic block states for features such as vines, sculk, and coral fans that adjust based on surroundings.
* Randomized block state stages for features such as bee nests, sea pickles, and cocoa beans.
* Checking surrounding blocks for valid feature placement such as lava columns.

.. Note::
    You can take a look at the :doc:`Terra Community Packs </config/community-packs>` and their usage
    of TerraScript in their ``.tesf`` files typically located within a ``structures`` folder.
