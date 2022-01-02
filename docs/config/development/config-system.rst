=================
The Config System
=================

In this section we will cover:

-  How Terra defines how configs must be structured.

-  How these structured configs are interpreted and utilized by Terra.

-  How we can write configs that abide by these prescribed structures.

Templates
=========

Most configurations follow what we will call a **template**. Templates
can be thought of as *special versions of maps* which specify rules on
how the contained key-value pairs must be structured. Many different
templates are defined by Terra and can each be regarded as their own
types, just like strings and integers.

Parameters
----------

One of the main components of any given template is It's specification
of **parameters**. Parameters are what makes our data useful, as just
about all world generation behavior in Terra is determined by
parameters.

The specification of a parameter inside a template involves:

-  What the name of the parameter is (which is also how it is referenced
   inside a template).

-  Whether the parameter is optional or required.

-  What the types can the parameter be set to.

To set parameters within a template, we use the *key* to denote **which
parameter** we want to set, and the *value* to **what the parameter
should be set to**. For example, here are a couple parameters specified
within a Terra config pack manifest that provides some basic information
about the pack:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: pack.yml
         :linenos:

         id: COOL_CONFIG_PACK
         version: 1.0.0
         author: Anon Y. Mous
   
   .. tab-item:: JSON

      .. code-block:: json
         :caption: pack.json
         :linenos:

         {
            "id": "COOL_CONFIG_PACK",
            "version": "1.0.0",
            "author": "Anon Y. Mous"
         }

Parameters may also be nested under multiple maps within a template. For
example in the below config, the top level object may abide by a
template and specify a parameter that is nested, which we can see has
the value ``a parameter value``.

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: config.yml
         :linenos:

         a:
           nested:
             parameter: a parameter value

   .. tab-item:: JSON

      .. code-block:: json
         :caption: config.json
         :linenos:

         {
            "a": {
               "nested": {
                  "parameter": "a parameter value"
               }
            }
         }

When referring to parameters within templates, we use a combination of
the parent key(s) separated by dots ``.`` to identify the desired
parameter. Using the above config, we would refer to the specified
parameter as ``a.nested.parameter``.

Some parameter conventions to keep in mind:

-  The parent key object(s) of a parameter will always be of type
   string, where all characters are lowercase, and dashes ``-`` are used
   in place of spaces.

-  The *type* of the *value object* is considered the *parameter's
   type*.

Working With Templates
----------------------

For the sake of explanation, let's invent a new template to work with
called ``AnimalTemplate``. The ``AnimalTemplate`` type specifies:

-  A required parameter called ``color`` that must be of type ``string``

-  A required parameter called ``legs`` that must be of type
   ``integer``.

We can then write a new config using our new type assuming our top level
object is of type ``AnimalTemplate``:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: koala.yml
         :linenos:

         color: grey
         legs: 4
   
   .. tab-item:: JSON

      .. code-block:: json
         :caption: koala.json
         :linenos:

         {
            "color": "grey"
            "legs": 4
         }

Because ``AnimalTemplate`` contains these parameter specifications, if
we write a config that does not abide by them, then Terra will fail to
load the config. For example, the following config would not load
because 1. ``color`` has not been specified and is a required parameter,
and 2. ``legs`` is not of the required type integer:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: koala.yml
         :linenos:

         legs: two
   
   .. tab-item:: JSON

      .. code-block:: json
         :caption: koala.json
         :linenos:

         {
            "legs": "two"
         }

If we were to *document* ``AnimalTemplate``, it may look like this:

.. card:: **AnimalTemplate**
   
   *Defines the attributes of an animal.*

   `REQUIRED`

   :bdg-primary:`color` ``String``
      The color of the animal.

   :bdg-primary:`legs` ``Integer``
      How many legs the animal has.

Great, now that we have a template to describe an animal, let's create a
new template that describes a zoo of animals:

.. card:: **ZooTemplate**

   *Defines a zoo of animals.*

   `REQUIRED`

   :bdg-primary:`animals` ``Map[String:AnimalTemplate]``
      A collection of animals.

   `OPTIONAL`

   :bdg-primary:`description` ``String``
      A description of the zoo and It's animals.

The interesting thing to note here with ``ZooTemplate`` is we have now
treated ``AnimalTemplate`` as the required value type of the ``animals``
parameter. This ability to utilize templates like any other type allows
for highly complex config specs, and is one of the key features of
Terra's config system.

We can now use ``AnimalTemplate``\ s within our new ``ZooTemplate`` and
create a config able to be read and interpreted by the config loader
like so:

.. tab-set::

   .. tab-item:: YAML
      
      .. code-block:: yaml
         :caption: australian_zoo.yml
         :linenos:

         description: A zoo of Australian animals.
         animals:
           koala:
             color: grey
             legs: 4
           kangaroo:
             color: brown
             legs: 2

   .. tab-item:: JSON

      .. code-block:: json
         :caption: australian_zoo.json
         :linenos:

         {
            "description": "A zoo of Australian animals.",
            "animals": {
               "koala": {
                  "color": "grey",
                  "legs": 4
               },
               "kangaroo": {
                  "color": "brown",
                  "legs": 2
               }
            }
         }

.. _config-types:

Config Types
============

Now that we have covered what templates are, what they do, and how we
write configs according to them, we have run into an issue: how does
Terra know which template the config should use in the first place? For
top level objects, there isn't a template It's contained in to specify
the type, so what tells Terra to use ``ZooTemplate`` instead of any
other template?

Choosing Templates
==================

This is where the ``type`` parameter comes in handy. The ``type``
parameter is a standardized way of specifying the template a ``Map``
will follow, and is available for use in places where multiple templates
may be applicable.

Registries
----------

In order to tell Terra we want our config to use ``ZooTemplate``, we
must set the ``type`` to something called a **registry key**. Registry
keys allow us to use things in a **registry**.

A registry can be thought of as an internal ``Map`` that Terra uses to
store similar things. Because of this, we can also think of registry
keys as working the same way as ``Map`` keys. Many registries exist in
Terra and all have different purposes; **registry entries** can be
created both by Terra (typically using addons), and by configuration
files, depending on use.

In this instance, we will be working with the **config registry**. The
config registry contains a bunch of templates like our ``ZooTemplate``,
which are *registered* internally by Terra. The purpose of the config
registry is to allow us to specify a config's template using the
``type`` key.

Let's assume that ``ZooTemplate`` has been registered under the name /
registry key ``ZOO`` by Terra. Now what we can do is simply set the
``type`` parameter to ``ZOO`` in our config from above, signifying to
Terra that our config top level object will be of type ``ZooTemplate``:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: australian_zoo.yml
         :linenos:
         :emphasize-lines: 1
               
         type: ZOO
         description: A zoo of Australian animals.
         animals:
           koala:
            color: grey
            legs: 4
           kangaroo:
            color: brown
            legs: 2

   .. tab-item:: JSON

      .. code-block:: json
         :caption: australian_zoo.json
         :linenos:
         :emphasize-lines: 2

         {
            "type": "ZOO",
            "description": "A zoo of Australian animals.",
            "animals": {
               "koala": {
                  "color": "grey",
                  "legs": 4
               },
               "kangaroo": {
                  "color": "brown",
                  "legs": 2
               }
            }
         }

And with that, we have now *designed a new* **config type** that Terra
is capable of interpreting.

Registering Configs
...................

Great! Now we are able to easily create new zoos just by making new
config files for each one, but we have run into another issue: how would
each zoo be kept track of? How would we be able to reference specific
zoos in other configs? Perhaps we could put all of our zoo configs
inside a single ``Map`` and keep everything inside one config file, and
use the key name to refer to each individual zoo - but that could get
cumbersome. What if we wanted to make hundreds of zoos, how would we
keep them all organized?

To solve this issue, we can make use of registries. Let's introduce a
new registry called the **zoo registry**. As a config developer, you
won't need to worry about creating registries, as they are provided by
addons and the API, so we can assume the zoo registry is created by one
of our installed addons. New registry entries inside our new zoo
registry can be made by simply creating ``ZOO`` configs, and we can let
Terra handle the registration of each config automatically.

To do this we will also need a way of choosing a *registry key* for each
zoo we want to make. We want control over the registry key, so what we
can do is introduce a new parameter in ``ZooTemplate`` called ``id``.
What ``id`` does is simply sets the *registry key* of configs when they
are automatically registered by Terra, allowing us to access all of our
``ZOO`` configs from anywhere via the *zoo registry*.

And with this, here is what our final config looks like:

.. tab-set::

   .. tab-item:: YAML

      .. code-block:: yaml
         :caption: australian_zoo.yml
         :linenos:
         :emphasize-lines: 1

         id: AUSTRALIAN_ZOO               
         type: ZOO
         description: A zoo of Australian animals.
         animals:
           koala:
            color: grey
            legs: 4
           kangaroo:
            color: brown
            legs: 2

   .. tab-item:: JSON

      .. code-block:: json
         :caption: australian_zoo.json
         :linenos:
         :emphasize-lines: 2

         {
            "id": "AUSTRALIAN_ZOO",
            "type": "ZOO",
            "description": "A zoo of Australian animals.",
            "animals": {
               "koala": {
                  "color": "grey",
                  "legs": 4
               },
               "kangaroo": {
                  "color": "brown",
                  "legs": 2
               }
            }
         }

Now in any other config that requires a zoo, we can specify our
``AUSTRALIAN_ZOO`` and it will automatically be grabbed from the zoo
registry for use.
