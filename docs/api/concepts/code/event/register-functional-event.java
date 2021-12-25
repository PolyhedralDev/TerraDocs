platform.getEventManager()                        // Get the event manager.
        .getHandler(FunctionalEventHandler.class) // Get the functional event handler.
        .register(addon, SomeEvent.class)         // Register a listener for SomeEvent, to our addon.
        .then(someEventInstance -> {              // Perform an action when the event is fired.
            logger.info("Handling Some Event!");
            logger.info("Event says: {}", someEventInstance.getSomething());
        })