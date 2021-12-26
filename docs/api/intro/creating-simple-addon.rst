=======================
Creating a Simple Addon
=======================

.. javadoc-import::
    org.slf4j.Logger


Now that you've set up your project, you're ready to make your first addon! This tutorial will walk you through
creating a simple "Hello, World!" addon with Terra using the Manifest Addon Loader.

Creating the Addon Manifest
===========================

First, you'll need to create the addon manifest. The addon manifest contains the data the Manifest Addon Loader
requires to load your addon. The manifest should be at the root of your JAR, named ``terra.addon.yml``.

.. literalinclude:: code/simple-addon/terra.addon.yml
    :language: yaml

.. note::
    The addon manifest should go in you project's *resources directory* (Usually ``src/main/resources``).

For your first addon, you can copy/paste this manifest and change it to your liking. Before changing any values, read
about what they do :ref:`here <addon-manifest>`.

Creating an Entry Point
=======================

The entry point is where the manifest loader will initialize your addon. Create a new Java class in your project
with the name defined in the ``entrypoints`` value in your manifest. If you didn't change the manifest, that would be
``com.example.addon.ExampleEntryPoint``. In your new class, implement ``AddonInitializer``:

.. literalinclude:: code/simple-addon/new-class.java
    :language: java


Adding Functionality to your Addon
==================================

You now have a Terra addon that Terra will be able to load and initialize! If you JAR and install your addon right now,
though, it won't do anything but that. That's because the entry point is empty. Let's add some functionality to this
addon!

Injecting a Logger
------------------

Let's make our addon log a message on initialization. To do that, we'll need a :javadoc:`Logger`. There are two ways
to access a Logger, we'll be accessing ours via :doc:`dependency injection <../concepts/dependency-injection>`:

.. literalinclude:: code/simple-addon/inject-logger.java
    :language: java

The ``logger`` field is now an injection target for a :javadoc:`Logger`. This means that before our addon initializes,
it'll receive a logger.

Using a Logger
--------------

Now we have a logger, but our addon still doesn't do anything. Let's use the logger to log a message to the console
when the addon initializes!

.. literalinclude:: code/simple-addon/hello-world.java
    :language: java

Compiling and Installing your Addon
===================================

Now you have an addon that logs something to the console on startup. How do you install it?

To install your addon, first you need to *compile* it, then *archive* it. The process is slightly different depending
on your build system:

.. tab-set::

    .. tab-item:: Gradle

        Run the ``:jar`` task. The JAR will be produced in ``build/libs``.

    .. tab-item:: Maven

        Run the ``package`` goal. The JAR will be produced in ``target``.

Once you have the JAR, put it in your Terra installation's ``addons`` folder. When you start Terra, you should
see a message logged to the console!

.. image:: /img/api/intro/simple-addon/init.png

Congratulations! You've successfully made your first Terra addon! To implement additional, more advanced functionality
in this example addon, continue with this introduction guide. If you're ready to start tinkering with the API on
your own, check out the :doc:`API Concepts<../concepts/index>` section.