public class ExampleStructure implements Structure, Keyed<ExampleStructure> {
    private final Platform platform;
    private final RegistryKey key;

    public ExampleStructure(Platform platform, RegistryKey key) {
        this.platform = platform;
        this.key = key;
    }

    @Override
    public boolean generate(Vector3Int location, WritableWorld world, Random random, Rotation rotation) {
        // ... Generation logic
    }

    @Override
    public RegistryKey getRegistryKey() {
        return key;
    }
}