public class ExampleStructure implements Structure {
    private final Platform platform;

    public ExampleStructure(Platform platform) {
        this.platform = platform;
    }

    @Override
    public boolean generate(Vector3Int location, WritableWorld world, Random random, Rotation rotation) {
        BlockState oakLog = platform.getWorldHandle().createBlockState("minecraft:oak_log[axis=y]");
        BlockState oakLeaves = platform.getWorldHandle().createBlockState("minecraft:oak_leaves[persistent=true]");

        int height = random.nextInt(5, 8);                               // Trunk will be [5, 8) blocks tall.

        GeometryUtil.sphere(
                Vector3Int.of(location, 0, height, 0),                   // Generate leaves at the top of the tree
                3,                                                       // Leaves will be a sphere of radius 3.
                leafLocation -> {                                        // This consumer is invoked once per coordinate in the sphere.
                    world.setBlockState(leafLocation, oakLeaves);
                }
        );

        for (int y = 0; y < height; y++) {                               // Iterate over the height.
            Vector3Int trunkLocation = Vector3Int.of(location, 0, y, 0); // Generate a part of the trunk here.
            world.setBlockState(trunkLocation, oakLog);                  // Generate an oak log at the location.
        }

        return true;                                                     // Our structure generated correctly.
    }
}