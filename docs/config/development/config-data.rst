========================
Defining Data in Configs
========================

In this section, we will cover the basic ways data is stored and written
inside config files. Because Terra configs are able to be written in
multiple languages, we use our own standardized set of terms to
reference things that may be named differently between languages.

.. tip::

   If you are already familiar with data structures and
   data-serialization languages, feel free to skim over this section and
   skip forward to the next section.

Types
=====

The main concept to understand is that of **data types** or simply
**types**. Types tell us:

-  How data should be defined

-  What is expected of that data to contain

-  How that data will be used

Typically when writing configs the data type will be inferred, but in
many cases you need to explicitly tell Terra what type you want to use.

A piece of data defined in a config is something we will call an
**object**. All objects can be categorized by having a type, which is
determined by how it is defined in the config. Config files always
define a single object, which is what we will call the **top level
object**.

Integers
--------

To put this information to use, let's create create a new config file in
YAML and define our top level object. For our type let's use something
called an ``Integer``.

Integers represent whole numbers and as such, are
written as whole numbers like so:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml
         
         42

   .. tab-item:: JSON

      .. code:: json

         42

We have now created a config that defines an ``Integer`` as the top
level object, which represents the number ``42``, simple right?

Floats
------

Another numerical type that is slightly different from integers is a
``Float``. The difference between integers and floats is that floats can
represent numbers that contain decimals:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         3.14159

   .. tab-item:: JSON

      .. code:: json

         3.14159

In many cases, we need to distinguish between integers and floats, as it
may not be logical to have numbers with decimals for whatever we're
configuring, having two separate types allows for preventing these
situations. Typically config parameters that require integers will not
accept a float, but parameters that require a float will accept
integers.

Strings
-------

We can also represent data like text using a type called a ``String``:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         This is a config of type string.

   .. tab-item:: JSON

      .. code:: json

         "This is a config of type string."

Strings are useful for specifying the names of things, and are used
everywhere - for example we would need need to use strings to specify
what block IDs we want to use for the blocks in a biome.

In some cases you may want to specify a ``String`` where it might be
interpreted as another type like ``Integer``. To explicitly specify an
object is a ``String``, you can wrap it quotes like so:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         "42"

   .. tab-item:: JSON

      .. code:: JSON

         "42"

      .. note::

         In JSON, strings *must* be explicitly wrapped in quotes.

Maps
----

By themselves, integers, floats, and strings aren't too useful, until we
start assigning labels to them. We can do that using a type called a
``Map``.

.. _key-value-pair:

A map is a *collection of objects*, referred to individually as
**values**, where each **value** in the collection is identified by
another unique object called a **key**. A key and a value together are
called a **key-value pair**.

Here we will make a new config where the *top level object* is of type
``Map``, and both the *key* and *value* are of type ``String``:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         this is a key: this is a value

   .. tab-item:: JSON

      .. code:: json

         {
            "this is a key": "this is a value"
         } 

Since maps are *collections* of objects, we can list multiple key value
pairs within the map like so:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         string: Here is some text.
         pi: 3.14159
         meaning-of-life: 42

   .. tab-item:: JSON

      .. code:: json

         {
            "string": "Here is some text.",
            "pi": 3.14159,
            "meaning-of-life": 42
         }

This is useful because as explained above, configs only contain *one*
top level object. By using maps, we are capable of defining more than
one object within a config, as well as being able to identify what each
of those objects are using keys.

Lists
-----

In addition to maps, we can also use a type called a ``List`` to
indicate a collection of data. Lists differ from maps in that each
object (called an **item**) in a list is not assigned a unique key, but
is instead identified by It's position in the list. Because of this,
*the order in which you define each object is significant*, unlike maps.

Another thing to note is generally, every item contained within a list
will be of the same type.

Here is a config where the *top level object* is a ``List``, which
contains multiple ``String``\ s:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         - A string
         - Another string
         - The final string

   .. tab-item:: JSON

      .. code:: json

         [
            "A string",
            "Another string",
            "The final string"
         ]

Nesting Objects
===============

Because values in maps and items in lists can be of any type, It's
possible to nest maps in maps, lists in lists, lists in maps, and so on.

Here is an example of a ``Map`` contained within the value of another
``Map`` (which is the top level object):

.. tab-set::

   .. tab-item:: YAML

      For simple data types like integers and strings it is clear which key
      corresponds to which value, as they are typically contained on the same
      line, but maps and lists may span multiple lines, so we need a way of
      defining which objects are defined under which keys and items. In YAML,
      we can specify this kind of relationship via *indentation* - which is
      simply how many spaces come before the key one a line. We conventionally
      use two spaces to indicate 'one level' of indentation in YAML configs.

      .. code:: yaml

         parent-key:
            child-key: value
            sibling-key: another value

      You can see that the map containing ``child-key`` and ``sibling-key`` is
      indented by two spaces, and is defined under the ``parent-key`` key,
      signifying that it belongs to that key.

   .. tab-item:: JSON

      .. code:: json

         {
            "parent-key": {
               "child-key": "value",
               "sibling-key": "another value"
            }
         }

And here is a ``Map`` (the top level object) containing a ``List`` of
``String``\ s:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         list of strings:
           - item 1
           - item 2
           - item 3

   .. tab-item:: JSON

      .. code:: json
         
         {
            "list of strings": [
               "item 1",
               "item 2",
               "item 3"
            ]
         }

Combining Everything
====================

We can combine these different types to represent complex data
structures, here is an example representing a shopping list, and some
appointments using everything we have covered thus far:

.. tab-set::

   .. tab-item:: YAML

      .. code:: yaml

         shopping-list:
           - item: 1L Milk
             amount: 2
             cost-per-item: 2.0
           - item: Carton of Eggs
             amount: 1
             cost-per-item: 4.5

         appointments:
           - name: Haircut Appointment
             date: 24.04.22
             start-time: 9:45
             end-time: 10:15
           - name: Doctor Appointment
             date: 13.05.22
             start-time: 3:15
             end-time: 4:15

   .. tab-item:: JSON
      
      .. code:: json

         {
            "shopping-list": [
               {
                  "item": "1L Milk",
                  "amount": 2,
                  "cost-per-item": 2
               },
               {
                  "item": "Carton of Eggs",
                  "amount": 1,
                  "cost-per-item": 4.5
               }
            ],
            "appointments": [
               {
                  "name": "Haircut Appointment",
                  "date": "24.04.22",
                  "start-time": 585,
                  "end-time": 615
               },
               {
                  "name": "Doctor Appointment",
                  "date": "13.05.22",
                  "start-time": 195,
                  "end-time": 255
               }
            ]
         }

In this example, our top level object is of type ``Map``, which contains
two keys ``shopping-list`` and ``appointments``. The value of both keys
are of type ``List``, where each *item* in each list contains a ``Map``.

Language Specific Syntax
========================

Some data-serialization languages support alternative syntax for
representing the same thing, for example in YAML you can represent maps
and lists using curly braces ``{}`` and square brackets ``[]``
respectively, where objects are separated by commas ``,`` instead. This
can be useful for when you don't necessarily want to separate objects by
lines and indentation:

.. code:: yaml

   curly-brace-map: {
     "key-1": "value-1",
     "key-2": "value-2"
   }

   square-bracket-list: [ 
     item-1,
     item-2,
     item-3
   ]

   single-line-map: { "key-1": "value-1", "key-2": "value-2" }

   single-line-list: [ item-1, item-2, item-3 ]

   empty-map: {}

   empty-list: []

YAML also provides additional systems like **anchors**, which allow for
easily re-using data within a config and is useful for when you might
want to write the same thing multiple times in a config:

.. code:: yaml

   some-list-of-data: &the-data-anchor
     - item-1
     - item-2

   somewhere-where-data-is-reused: *the-data-anchor

When parsed by the YAML language addon, the value of
``somewhere-where-the-data-is-reused`` will be the same as the list
defined under ``some-list-of-data``.
