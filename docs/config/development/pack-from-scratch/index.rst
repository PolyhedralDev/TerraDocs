============================
Creating a Pack from Scratch
============================

This guide will outline the process of creating a new Terra config
pack from the beginning. If you haven't already, please read the
:doc:`Config Development Introduction </config/development/introduction>`
for more information before continuing.

If you're stuck or need an example, you can find reference config packs for this guide on the
`GitHub repo <https://github.com/PolyhedralDev/TerraPackFromScratch/>`_\.

.. card::

    If you wish to **modify an existing pack** rather than creating your
    own from scratch, please refer to the :doc:`/config/development/modifying-existing-pack`
    guide instead.

.. attention::

    This guide is written for Terra version 6.0.+ and will not be applicable to prior versions!

Setting up a New Pack
=====================

`PROCEDURE`

1. Create your config pack directory
------------------------------------

.. card::

    Navigate to your :ref:`packs directory <packs-directory>` and create a new folder inside, the
    name of this folder is up to you to decide. The pack directory will contain all
    your :doc:`config files </config/development/config-files>`.

2. Create a pack manifest 
-------------------------

.. card::

    To make a **pack manifest**, :ref:`create a new config file <create-config-file>` within 
    your pack directory with the file name ``pack.yml``.
    
    Pack manifests define pack-wide information that is required for it to load correctly
    - such as who made it, what version the pack is, and what dependencies such as addons
    and Minecraft versions are required for it to function.

3. Set the pack ID and version 
------------------------------

.. card::

    Open your pack manifest in your :ref:`editor of choice <editor>`.

    Within your editor, add the following **parameters** to your pack manifest:

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:

        id: YOUR_PACK_ID

        version: 0.1.0

    A parameter can also be thought of as 'config options' - for a more complete explanation of how these work
    you can refer to the :doc:`Config System </config/development/config-system>` page.

    You're free to change these parameters to whatever you'd like, with some restrictions:

    * The pack ``id`` must only contain alphanumeric characters (A-Z, 0-9) and dashes or underscores (no spaces).
    
    * Pack ``id``\s conventionally use all uppercase letters, however this is not a strict requirement.

    * The pack ``version`` must use the format ``X.Y.Z``, according to the `SemVer <https://semver.org/>`__ spec.

    *Optionally*, you can also specify yourself as the author of your pack with the ``author`` parameter:

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 5

        id: YOUR_PACK_ID

        version: 0.1.0

        author: YOUR_USERNAME # Optional

.. tip::

    As explained :ref:`here <map-ordering>`, the order in which parameters are specified does not matter, so
    you are free to define each parameter in whatever order you'd like. In addition, extra blank lines between
    parameters is ignored, the follow examples are all equivalent:

    .. tab-set::

        .. tab-item:: Example 1

            .. code-block:: yaml
                :caption: pack.yml
                :linenos:

                id: YOUR_PACK_ID

                version: 0.1.0

        .. tab-item:: Example 2

            .. code-block:: yaml
                :caption: pack.yml
                :linenos:

                id: YOUR_PACK_ID
                version: 0.1.0

        .. tab-item:: Example 3

            .. code-block:: yaml
                :caption: pack.yml
                :linenos:

                version: 0.1.0
                id: YOUR_PACK_ID


4. Specify a config file format 
-------------------------------

.. card::
    
    Terra requires you to specify the file format of config files, as outlined on the
    :doc:`Config Files </config/development/config-files>` page. To do so, we will need to include an
    addon in our pack manifest that has the functionality to parse config files.

    In this guide we will be using YAML for our config files, as support for YAML is included by default
    via the ``language-yaml`` core addon. We can include this via the pack manifest ``addons`` parameter like so:

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 5,6

        id: YOUR_PACK_ID

        version: 0.1.0

        addons:
          language-yaml: 0.1.+

    Addons defined under the ``addons`` parameter are specified as :ref:`key-value pairs <key-value-pair>` where the key
    specifies the addon name, and the value specifies the required addon version(s).

    .. note::

        All config files within a config pack must use a file format supported by the language addons specified
        within the pack manifest. The pack manifest itself differs in that it must use a file format supported by
        any *installed* language addons, though it should be written using a format it specifies.

5. Specify the chunk generator
------------------------------

.. card::

    Chunk generators tell Terra how to generate the base blocks of a chunk (before any decoration is applied) and are
    implemented via addons.

    For this guide, we will use the ``NOISE_3D`` generator which is implemented by the ``chunk-generator-noise-3d``
    core addon. We can utilize this by adding ``chunk-generator-noise-3d`` to the ``addons`` parameter like so:

    .. code-block:: yaml
        :caption: pack.yml
        :emphasize-lines: 3

        addons:
          language-yaml: 0.1.+
          chunk-generator-noise-3d: 0.1.+

    .. note::

        This will be the assumed process you'll follow when prompted to include an addon!

    Now that we have a generator available, we can tell the pack to use it via the ``generator`` parameter like so:

    .. code-block:: yaml
        :caption: pack.yml
        :linenos:
        :emphasize-lines: 9

        id: YOUR_PACK_ID

        version: 0.1.0

        addons:
          language-yaml: 0.1.+
          chunk-generator-noise-3d: 0.1.+

        generator: NOISE_3D

    The ``NOISE_3D`` generator also requires being able to define two more additional things called *samplers*,
    and *palettes*. To be able to define these we can add the following addons to our pack manifest like so:

    .. code-block:: yaml
        :caption: pack.yml
        :emphasize-lines: 4,5

        addons:
          language-yaml: 0.1.+
          chunk-generator-noise-3d: 0.1.+
          config-noise-function: 0.1.+
          palette-block-shortcut: 0.1.+

6. Create your first biome
--------------------------

.. card::

    1. Add the ``config-biome`` addon as a dependency, using versions ``0.1.+``. This will allow us to create new
    biomes via the ``BIOME`` :ref:`config type <config-types>` which is provided by the addon. 

    2. :ref:`Create a new config file <create-config-file>`, this can be named anything but for this guide we will
    use the name ``first_biome.yml``.

    3. With ``first_biome.yml`` open in your editor, set the :ref:`config type <config-types>` via the ``type``
    parameter, and config ``id`` like so:

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:

        id: FIRST_BIOME

        type: BIOME
        

    4. Set the ``vanilla`` parameter to a vanilla biome ID. We will use ``minecraft:plains`` in the example but you 
    could use any valid vanilla biome ID you want.
    

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 5

        id: FIRST_BIOME

        type: BIOME

        vanilla: minecraft:plains

    Terra uses the ``vanilla`` parameter to determine how things like mob spawning and grass color is handled, however this is
    may differ based on the platform you're on.

7. Add the generator parameters to your new biome 
-------------------------------------------------

These parameters will determine how the ``NOISE_3D`` generator generates terrain within our biome:

.. card:: ``terrain.sampler`` - Shapes the terrain within the biome.

    For now, we will use the following config for ``terrain.sampler``:

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 7-10

        id: FIRST_BIOME

        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: LINEAR_HEIGHTMAP
            base: 64

    How exactly this works will be explained in a later guide but just know that this will produce flat terrain at the Y-level
    specified by the ``base`` parameter (for which we will use y=64).

.. card:: ``palette`` - Defines the blocks that make up the terrain in the biome.

    The ``palette`` parameter accepts a ``List`` of singular key-value pairs, where the key represents a ``palette`` config and the
    value is an ``Integer`` that determines the upper Y level the palette will apply to until the next lower palette.

    For example, with the following config, ``Palette C`` would be used for terrain below y10, ``Palette B`` would be used
    between y11 and y30, and terrain above y31 would use ``Palette A``:

    .. code-block:: yaml

        palette:                 
          - Palette A: 319 # From y319 downwards until next palette down (at y30)
          - Palette B: 30  # From y30 downwards until next palette down (at y10)
          - Palette C: 10  # From y10 downwards

    The ``palette-block-shortcut`` addon allows us to easily define single block palettes using the format ``BLOCK:<block id>``.
    For our biome config, we will use ``minecraft:stone``, and use ``319`` to specify that terrain from y319 downwards will consist of ``minecraft:stone``.

    .. code-block:: yaml
        :caption: first_biome.yml
        :linenos:
        :emphasize-lines: 12-13

        id: FIRST_BIOME

        type: BIOME

        vanilla: minecraft:plains

        terrain:
          sampler:
            type: LINEAR_HEIGHTMAP
            base: 64
        
        palette:
          - BLOCK:minecraft:stone: 319    
        
8. Define a biome provider 
--------------------------

For our pack to load, and for ``FIRST_BIOME`` to generate, we will need to define a **biome provider**.
Biome providers tell Terra how to place biomes in a world.

We can define a provider under the ``biomes`` parameter, but first we will need to add a provider to our pack for use.
For this guide, we will be using the ``SINGLE`` biome provider, which will require adding the ``biome-provider-single`` core addon
(versions ``0.1.+``).

After you have added ``biome-provider-single``, you can add the ``biomes`` parameter to your pack manifest like so:

.. code-block:: yaml
    :caption: pack.yml
    :linenos:
    :emphasize-lines: 14-16

    id: YOUR_PACK_ID

    version: 0.1.0

    addons:
      language-yaml: 0.1.+
      chunk-generator-noise-3d: 0.1.+
      config-noise-function: 0.1.+
      palette-block-shortcut: 0.1.+
      biome-provider-single: 0.1.+

    generator: NOISE_3D

    biomes:
      type: SINGLE
      biome: FIRST_BIOME

You can see that the ``biome`` parameter of the ``SINGLE`` provider is set to the ``id`` defined in your first biome config.
This will make ``FIRST_BIOME`` generate everywhere in worlds using your pack.

9. Load up your pack
--------------------

At this stage, your pack should now be capable of generating a world! You can load up your pack by starting your
development client / server which contains the pack you have just defined. You can confirm that your pack has loaded
if the pack id (as specified in the pack manifest) appears when using the ``/packs`` command, or in your console 
when starting the server / client up.

If for whatever reason your pack does not load, an error message will show up in console explaining why the pack
has failed to load, please read through any of these errors and try to interpret what you may have done wrong,
and follow through the previous steps again carefully.

If you still are unable to load the pack, feel free to provide any relevant errors in our `Discord server <https://discord.com/invite/PXUEbbF>`_.

Conclusion
==========

Once you have verified your pack has loaded correctly, you can now generate a world with your new pack!

Reference configurations for this introduction can be found on GitHub
`here <https://github.com/PolyhedralDev/TerraPackFromScratch/tree/master/1-setting-up>`_.
