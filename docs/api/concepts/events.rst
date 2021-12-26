======
Events
======

.. javadoc-import::
    com.dfsek.terra.api.event.functional.FunctionalEventHandler
    com.dfsek.terra.api.Platform
    com.dfsek.terra.api.event.EventManager
    java.lang.Class
    java.util.functions.Consumer
    com.dfsek.terra.api.addon.BaseAddon
    com.dfsek.terra.api.event.functional.EventContext

Interfacing with the Terra API is primarily done through events.

The Event Manager
=================

The base for working with events in Terra is the :javadoc:`EventManager`. The Event Manager contains methods to:

- Call events (``#callEvent``)
- Register event handlers (``#registerHandler``)
- Access event handlers (``#getHandler``)

Accessing the Event Manager
---------------------------

The Event Manager is accessed through the :javadoc:`Platform` instance:

.. literalinclude:: code/event/get-event-manager.java
    :language: java

.. note::
    To access the :javadoc:`Platform` instance in your addon, use :doc:`Dependency Injection <dependency-injection>`.

.. note::
    You'll generally want to register event listeners in your addon's entry point(s).

Event Handlers
==============
Event handlers provide API to register event listeners. Terra provides a single event handler by default, the
:javadoc:`FunctionalEventHandler`. Addons are able to register custom event handlers if they wish to use different
APIs to register events, for example, annotated methods.

Accessing an Event Handler
--------------------------

To access an event handler, simply pass its Class instance into :javadoc:`EventManager#getHandler(Class)`.

Here's an example for accessing the default :javadoc:`FunctionalEventHandler`:

.. literalinclude:: code/event/get-functional-event-handler.java
    :language: java

.. _functional-event-handler:

The Functional Event Handler
----------------------------

The Functional Event Handler is the default Event Handler provided by Terra. Most addons will want to use this event
handler. This handler provides a functional-style API for registering events using Java's `lambda expressions`_.

Registering a Listener
......................

When registering an event listener with the Functional Event Handler, invoke the
:javadoc:`FunctionalEventHandler#register(BaseAddon, Class)` method. This will return an instance of
:javadoc:`EventContext` which you can use to build your listener.

Adding an Action to the Listener
................................

To add actions to your event listener, append :javadoc:`EventContext#then(Consumer)` calls. these operations will
execute consecutively, with the consumer accepting the event instance.

Example
.......

.. literalinclude:: code/event/register-functional-event.java
    :language: java

This example registers a listener for ``SomeEvent``. When the event is called, the result of the event instance's
``#getSomething()`` is logged.



.. _lambda expressions: https://www.w3schools.com/java/java_lambda.asp
