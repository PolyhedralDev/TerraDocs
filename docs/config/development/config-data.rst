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
define a single object.

Integers
--------

To put this information to use, let's create create a new config file in
YAML. For our type let's use the ``Integer`` type.

Integers represent whole numbers and as such, are
written as whole numbers like so:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         42

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         42

We have now created a config that defines an ``Integer``, which represents the number ``42``.

Floats
------

Another numerical type that is slightly different from integers is a
``Float``. The difference between integers and floats is that floats can
represent numbers that contain decimals:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         3.14159

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         3.14159

In many cases, we need to distinguish between integers and floats, as it
may not be logical to have numbers with decimals for whatever we're
configuring, having two separate types allows for preventing these
situations. Typically config parameters that require integers will not
accept a float, but parameters that require a float will accept
integers.

Booleans
--------

The type ``Boolean`` defines data that can be in one of two states. This
is almost always used for cases were you want something to be either
*true* or *false* and is written as such:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         true

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         false

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         true

      .. code-block:: json
         :caption: config.json
         :linenos:

         false

Strings
-------

We can also represent data like text using a type called ``String``:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         This is a config of type string.

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         "This is a config of type string."

Strings are useful for specifying the names of things, and are used
everywhere - for example we would need need to use strings to specify
what block IDs we want to use for the blocks in a biome.

In some cases you may want to specify a ``String`` where it might be
interpreted as another type like ``Boolean``. To explicitly specify an
object is a ``String``, you can wrap it quotes like so:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         "true"

   .. tab-item:: JSON

      .. code-block:: JSON
         :caption: config.json
         :linenos:

         "true"

      .. note::

         In JSON, strings are always explicitly wrapped in quotes.

Maps
----

By themselves, integers, floats, and strings aren't too useful, until we
start assigning labels to them. We can do that using a type called a
``Map``.

- A map is a *collection of objects*.
- Each object in the collection is called a **value**.
- Each **value** is identified by another object called a **key**.

Here we will make a new config with type ``Map``, and both the
key and value are of type ``String``:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         this is a key: this is a value

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "this is a key": "this is a value"
         } 

Since maps are collections of objects, we can list multiple key value
pairs within the map like so:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         string: Here is some text.
         pi: 3.14159
         meaning-of-life: 42

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "string": "Here is some text.",
            "pi": 3.14159,
            "meaning-of-life": 42
         }

This is useful because as explained above, configs only contain one main object.
By using maps, we are capable of defining multiple objects within a map,
as well as being able to identify each of those objects with keys.

Each key within the same map must be unique, the following is invalid:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         duplicated key: value A
         duplicated key: value B

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "duplicated key": "value A",
            "duplicated key": "value B"
         } 

.. _map-ordering:

Ordering 
........

The ordering of key-value pairs inside a map is not significant, and as
such you are free to order them however you'd like.

These two configs are both equivalent:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         a: 1234
         
         b: Some text
         
         c: true

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         b: Some text
         
         c: true
         
         a: 1234

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "a": 1234,
            "b": "Some text",
            "c": true
         }
      
      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "b": "Some text",
            "c": true,
            "a": 1234
         }
      
Lists
-----

In addition to maps, we can also use a type called a ``List`` to
define a collection of objects. Lists differ from maps in that each
**item** (the term for an object in a list) is not assigned a unique key, but
is instead identified by its position in the list. Because of this,
*the order in which you define each object is significant*, unlike maps.

Here is a config with type ``List``, which contains multiple ``String``\ s:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         - A string
         - Another string
         - The final string

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         [
            "A string",
            "Another string",
            "The final string"
         ]

Nesting Objects
===============

Because values in maps and items in lists can be of any type, it's
possible to nest maps in maps, lists in lists, lists in maps, and so on.

.. tip::

    Defining something inside something else is commonly referred to as 'nesting'.

.. tab-set::

   .. tab-item:: YAML

      When setting the value of a map, typically it will just fit on the
      same line as the key, for example the ``Float`` 42 can just be written
      in-line with the key, after the colon like so:

      .. code-block:: yaml

          key: 42

      Types that can span multiple lines, such as maps and lists won't fit
      on a single line. For example you may want the following map which spans
      multiple lines to be a value within another map:

      .. code-block:: yaml

          foo: a
          bar: b

      To nest this map as a value of a key, say ``baz``, in another map, it can be
      defined under the key with additional indentation like so:

      .. code-block:: yaml

          baz:
            foo: a
            bar: b

      Indentation / indenting text refers to having some consistent number of spaces before
      each line in text. In YAML, the recommended number of spaces to indent is 2 as shown above.

      Lists can be nested similarly like so:

      .. code-block:: yaml

          my-list:
            - item 1
            - item 2

      Multiple levels of indentation can be used, for example here is the prior map further
      nested under (as the value for the key) ``qux``:

      .. code-block:: yaml

          qux:
            baz:
              foo: a
              bar: b

      Each map can be visualized by drawing boxes like so:

      .. image:: /img/config/development/nested-maps.png

   .. tab-item:: JSON

      Example of a ``Map`` defined in a ``Map``:

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "parent-key": {
               "child-key": "value",
               "sibling-key": "another value"
            }
         }

      Example of a ``List`` defined in a ``Map``: 

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "my-list": [
              "item 1",
              "item 2"
            ]
         }

Illegally defining two values for one key
-----------------------------------------

A common mistake in YAML is to accidentally assign two different
values to the same key.

For example the following is invalid:

.. code-block:: yaml

   key: foo
     baz: bar

This is invalid is because there are two competing values being
assigned to ``key``, which are ``foo`` and the map containing ``baz: bar``.

Deleting one of the values would make this valid YAML:

.. code-block:: yaml

    key:
      baz: bar

Or

.. code-block:: yaml

    key: foo

A config might end up in this invalid state for many reasons.

A key may have been deleted or omitted which could be remedied by re-adding it like so:

.. code-block:: yaml
    
    key: foo
    missing:
      baz: bar

Indentation may have been changed by accident, for example removing indentation 
would make it valid like so:

.. code-block:: yaml
    
    key: foo
    baz: bar

Combining Everything
====================

We can combine these different types to represent complex data
structures, here is an example representing a shopping list, and some
appointments using everything we have covered thus far:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

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
      
      .. code-block:: json
         :caption: config.json
         :linenos:

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

In this example, the config is of type ``Map``, which contains
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

.. code-block:: yaml
   :caption: config.yml
   :linenos:

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

YAML Anchors
------------

YAML also provides additional systems like **anchors**, which allow for
easily re-using data within a config and is useful for when you might
want to write the same thing multiple times in a config:

.. code-block:: yaml
   :caption: config.yml
   :linenos:

   some-list-of-data: &the-data-anchor
     - item-1
     - item-2

   somewhere-where-data-is-reused: *the-data-anchor

When parsed by the YAML language addon, the value of
``somewhere-where-the-data-is-reused`` will be the same as the list
defined under ``some-list-of-data``.
