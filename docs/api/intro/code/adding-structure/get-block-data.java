public class ExampleStructure implements Structure {
    private final Platform platform;

    public ExampleStructure(Platform platform) {
        this.platform = platform;
    }

    @Override
    public boolean generate(Vector3Int location, WritableWorld world, Random random, Rotation rotation) {
        BlockState oakLog = platform.getWorldHandle().createBlockState("minecraft:oak_log[axis=y]");
        BlockState oakLeaves = platform.getWorldHandle().createBlockState("minecraft:oak_leaves[persistent=true]");

        return false;
    }
}
