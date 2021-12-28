platform.getEventManager()
        .getHandler(FunctionalEventHandler.class)
        .register(addon, ConfigPackPreLoadEvent.class)
        .then(event -> {
            logger.info("We're loading a config pack!");

            ConfigPack pack = event.getPack();
            CheckedRegistry<Structure> structureRegistry = pack.getOrCreateRegistry(Structure.class);
        });