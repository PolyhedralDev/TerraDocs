public class ExampleEntryPoint implements AddonInitializer {
    @Inject
    private Logger logger;

    @Inject
    private Platform platform;

    @Inject
    private BaseAddon addon;

    @Override
    public void initialize() {
        logger.info("Hello, World!");

        RegistryKey key = addon.key("EXAMPLE_STRUCTURE");

        ExampleStructure theStructure = new ExampleStructure(platform, key);

        platform.getEventManager()
                .getHandler(FunctionalEventHandler.class)
                .register(addon, ConfigPackPreLoadEvent.class)
                .then(event -> {
                    logger.info("We're loading a config pack!");
                });
    }
}