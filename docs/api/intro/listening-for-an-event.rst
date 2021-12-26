======================
Listening for an Event
======================

.. javadoc-import::
    com.dfsek.terra.api.event.events.config.pack.ConfigPackPreLoadEvent
    com.dfsek.terra.api.event.functional.FunctionalEventHandler
    com.dfsek.terra.api.event.EventManager
    com.dfsek.terra.api.addon.BaseAddon
    com.dfsek.terra.api.Platform
    com.dfsek.terra.api.event.functional.EventContext
    com.dfsek.terra.api.event.events.PackEvent

Listening for :doc:`../concepts/events` is essential for interfacing with the Terra API.

ConfigPackPreLoadEvent
======================

In this tutorial, we'll be listening for :javadoc:`ConfigPackPreLoadEvent`. As the name suggests, this event
is fired before the configuration files in a config pack are loaded. Addons may listen to this event to

- Register config loaders
- Register config types
- Register objects

For now, we'll just log a message to the console when the event is fired.


Listening for the Event
=======================

To listen for the event, we'll be using the :javadoc:`FunctionalEventHandler` API. To learn more about the Functional
Event Handler, read about it :ref:`here <functional-event-handler>`.

Injecting the Required Objects
------------------------------

To access the :javadoc:`EventManager`, which we'll use to access the Functional Event Handler, we need a
:javadoc:`Platform` instance. We'll also need our :javadoc:`BaseAddon` instance later, so let's inject that too:

.. literalinclude:: code/event/injects.java
    :language: java

.. note::
    If you need a refresher on dependency injection, you can read about it
    :doc:`here <../concepts/dependency-injection>`

Creating an Event Context
-------------------------

The :javadoc:`EventContext` is used for defining a handler for an event. The event context is a builder-like object
that you can use to configure properties of your handler. Let's create an event context for ConfigPackPreLoadEvent:

.. literalinclude:: code/event/context.java
    :language: java

If you recompile and install your addon again, you'll see that... nothing happens.

Event Scope
===========

Some events in Terra have *scope*. This means that they are only fired to addons that meet certain conditions.
:javadoc:`ConfigPackPreLoadEvent` is one of these events.

Pack Events
-----------
If you look at the class hierarchy of ConfigPackPreLoadEvent, you'll see it implements the :javadoc:`PackEvent`
interface. All events that implement this interface are *pack scoped*. This means that their handlers are only
fired if the addon that registered the handler is a dependency of the config pack.

So, how do you get your event handler to fire?

Pack Dependencies
-----------------

In the pack manifest (``pack.yml``) is an ``addons`` key. These addons are dependencies of the config pack. To recieve
events fired by this pack, simply add your addon and a version range to this map. Go ahead and modify the default pack
to add your addon as a dependency:

.. literalinclude:: code/event/pack.yml
    :language: yaml

Now when you run with your addon again, you should see a message logged to the console with the pack ID when the pack
loads!

.. image:: /img/api/intro/event/init.png

Global Event Handlers
---------------------

Another way is to mark your event handler as *global*. Using the :javadoc:`EventContext#global` method, you can
eliminate the pack scope from your event handler. This will cause your handler to be fired regardless of whether
the pack that fired it depends on your addon. Marking the handler as global would look like this:

.. literalinclude:: code/event/context-global.java
    :language: java

.. warning::

    It is generally a bad idea to mark handlers for scoped events as global! By marking a handler as global, you may
    introduce unexpected behavior, as it is expected that events only reach addons that are dependencies of the event
    source.


Conclusion
==========

You now have a pack-scoped event listener in your addon, which logs when the :javadoc:`ConfigPackPreLoadEvent` is
fired. Continue to learn how to register objects!

Our example addon at this stage looks like this:

.. literalinclude:: code/event/addon.java
    :language: java
