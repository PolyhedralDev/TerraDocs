=========
Type Keys
=========

.. javadoc-import::
    java.lang.Class
    com.dfsek.terra.api.util.reflection.TypeKey

Many places in the Terra API make use of generics and Java's :javadoc:`Class` class for type-safe reflective type
handling. This approach generally works quite well.

The Issue
=========

What if you want a registry that registers instances of ``SomeObject<SomeOtherThing>``? Due to `type erasure`_, this is
not immediately possible. You cannot access ``SomeObject<SomeOtherThing>.class``, as it simply does not exist at
runtime.

A naive solution is to simply use ``SomeObject.class``. This is not ideal for two reasons:

- It breaks type safety. ``SomeObject`` now has no generic type.
- It will overwrite or be overwritten by anything else that attempts to register any generic type of ``SomeObject``.

The Solution
============

Terra includes an abstract class called :javadoc:`TypeKey` to solve this problem. All APIs which accept a ``Class``
instance also accept a ``TypeKey``. To acquire a ``TypeKey`` instance for your type, simply create an inner class
which extends ``TypeKey`` with a generic type matching yours. In our ``SomeObject<SomeOtherThing>`` example, that would
look like:

.. literalinclude:: code/type-key/type-key.java
    :language: java

.. note::
    Notice that the ``TypeKey`` is ``static final``. This is to reduce boilerplate by moving the key declaration to
    the top of the class, and to reduce unneeded instantiation.

.. _type erasure: https://www.baeldung.com/java-type-erasure