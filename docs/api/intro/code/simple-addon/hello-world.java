package com.example.addon;

import com.dfsek.terra.addons.manifest.api.AddonInitializer;
import com.dfsek.terra.api.inject.annotations.Inject;
import org.slf4j.Logger;

public class ExampleEntryPoint implements AddonInitializer {
    @Inject
    private Logger logger;

    @Override
    public void initialize() {
        logger.info("Hello, World!");
    }
}
