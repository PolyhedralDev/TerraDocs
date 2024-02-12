==================
Meta configuration
==================

Meta configuration is an optional part of Terra's config system that allows for
setting parameters based on configuration defined elsewhere in a config pack. This
is akin to having variables in a programming language.

Meta configuration is handy for being able to set a value in one place to be re-used in multiple places,
for creating your own parameters for ease of modification, and for organization.

Referencing
===========

A value can be referenced by the path to the file it's defined in, then a colon, then
the parent keys the value is defined under separated by a dot ``.``. File paths are relative
to the pack directory.

`<file path>:<parent keys>`

For example to reference the string ``example`` in the file ``config.yml``:

.. code-block:: yaml
    :caption: config.yml

    path:
      to:
        config:
          value: example

You would use ``config.yml:path.to.config.value``.

References by themselves will just be treated as plain strings, so there is additional
syntax required for meta configuration convered in the rest of this page:

MetaValue
=========

The most basic form of meta configuration is simply setting a parameter to a referenced value. To
do so, prefix a reference with a ``$`` to indicate it is a MetaValue and not a regular string.

For example:

.. code-block:: yaml

    thing: $config.yml:my.value

Sets ``thing`` to whatever ``my.value`` is defined as in the file ``config.yml``: 

.. code-block:: yaml
    :caption: config.yml

    my:
      value: something

This means that ``thing`` in the first config will be set to ``something`` which is defined
in a different file.

This works for most parameters, as long as they're meta configurable (most should be).

MetaList
========

You can merge list items from one list into another via the MetaList syntax. To do so,
include an item in the list which is a string starting with ``<<`` then a space, then
a reference to another list.

For example:

.. code-block:: yaml

    things:
      - ONE
      - << config.yml:another.list
      - FOUR

This will merge the items from a list defined in ``config.yml``:

.. code-block:: yaml
    :caption: config.yml

    another:
      list:
        - TWO
        - THREE

``things`` will contain items ``ONE``, ``TWO``, ``THREE``, ``FOUR`` in that specific order.
Since order matters in lists, the referenced list's items will be merged in at the position of the reference.
The same syntax works for sets, though order is not preserved.

Multiple lists can be merged into the same list in any order:

.. code-block:: yaml

    things:
      - ONE
      - << config.yml:lists.first
      - FOUR
      - << config.yml:lists.second
      - << config.yml:lists.third
      - NINE

MetaMap
=======

The MetaMap syntax allows for merging in / overriding key value pairs. This based on the
`proposed 'merge keys' YAML feature <https://yaml.org/type/merge.html>`_\ (which is
supported by the YAML parser Terra uses).

A special ``"<<"`` key defined in a map is used to indicate other maps to merge in, and
should be set to a list of references to other maps.

.. warning::

    This key must be quoted as to not be interpreted as a regular YAML merge key.

For example:

.. code-block:: yaml

    things:
      one: ONE
      "<<":
        - config.yml:another.map

Merges ``two`` and ``three`` from ``another.map`` defined in ``config.yml``:

.. code-block:: yaml
    :caption: config.yml

    another:
      map:
        two: TWO
        three: THREE

The first config would be equivalent to:

.. code-block:: yaml

    things:
      one: ONE
      two: TWO
      three: THREE

MetaMap Priority
----------------

If two or more values are assigned to the same key across the relevant maps, the value from the
last referenced map containing the key will be used, with the key (if any) from the map being merged into
(containing ``"<<"``) having the lowest priority.

For example given the two configs:

.. code-block:: yaml

    map:
      "<<":
        - config.yml:first
        - config.yml:second
        - config.yml:third
      key: Base

.. code-block:: yaml
    :caption: config.yml

    first:
      key: First
    second:
      key: Second
      extra: Extra value
    third:
      key: Third

The value assigned to ``map`` would be equivalent to:

.. code-block:: yaml

    map:
      key: Third
      extra: Extra value

Because:
  - ``key`` is defined in all maps, since ``config.yml:third`` is the last reference that contains ``key``, its value takes priority and is used.
  - ``extra`` is defined in ``config.yml:second`` and no other map defines it, so it is merged in.

MetaString
==========

The MetaString syntax allows for inserting referenced values into a string.
Parts of a string with the following format will be replaced with the value they reference:

`${<reference>}`

For example:

.. code-block:: yaml

    thing: ${config.yml:thing1}, ${config.yml:thing2}!

Inserts the strings from config.yml into ``thing``:

.. code-block:: yaml
    :caption: config.yml

    thing1: Hello
    thing2: World

``thing`` is now equivalent to the string ``Hello, World!``.

The referenced values must be strings, integers, floats, booleans, or meta configured to
evaluate to the former.

MetaNumber
==========

If a parameter expects some kind of number (a float or integer), an :doc:`/config/documentation/objects/Expression`
can be provided instead.

.. code-block:: yaml

    number: 3 * 2

``number`` would be evaluated as the number ``6``.

The MetaString syntax is first applied to the expression, meaning you can reference
values like so:

.. code-block:: yaml

    number: 2 * ${config.yml:multiplier}

Once the MetaString syntax is applied, the resulting string will then be parsed as an
expression then evaluated to produce the number the parameter is set to.

Parsing Order
=============

When meta configuration is used in conjunction with YAML syntax, YAML parsing is applied first, then any meta preprocessing, where
parameters are set to the resuling evaluation.

Given the following configs:

.. code-block:: yaml
   :caption: foo.yml

    to-merge: &anchor
      - bar.yml:map-a
      - bar.yml:map-b

    parameter:
      key-a: alpha
      "<<": *anchor

.. code-block:: yaml
   :caption: bar.yml

    map-a:
      key-b: bravo

    map-b:
      key-c: charlie

First the YAML anchor will be applied to ``parameter.<<``, resulting in:

.. code-block:: yaml
    :caption: foo.yml

    parameter:
      key-a: alpha
      "<<":
        - bar.yml:map-a
        - bar.yml:map-b

Then the MetaMap syntax will be applied for ``parameter``:

.. code-block:: yaml
    :caption: foo.yml

    parameter:
      key-a: alpha
      key-b: bravo
      key-c: charlie

