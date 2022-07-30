===============
Getting Started
===============

.. toctree::
    :hidden:

    fabric
    forge
    quilt
    bukkit
    versions

Terra's platform-agnostic API allows us to seamlessly support many
Minecraft modding platforms. The currently supported platforms include 
`Fabric <https://fabricmc.net>`_, `Forge <https://files.minecraftforge.net/>`_, `Quilt <https://quiltmc.org/>`_, and the `Bukkit <https://dev.bukkit.org>`_
ecosystem. In regards to Bukkit, we officially support `Paper <https://papermc.io>`_\+
implementations only, including but not limited to `Pufferfish <https://github.com/pufferfish-gg/Pufferfish>`_
and `Purpur <https://purpurmc.org/>`_.

.. grid:: 2

    .. grid-item-card:: Fabric Server & Client :octicon:`chevron-right`
        :link: fabric
        :link-type: doc
        :class-title: sd-text-primary 

        Fabric is the base platform Terra is primarily developed for. Recommended for running Terra in a singleplayer environment, or on a small server
        with friends.

    .. grid-item-card:: Quilt Server & Client :octicon:`chevron-right`
        :link: quilt
        :link-type: doc
        :class-title: sd-text-primary 

        Quilt is recommended for running Terra in a singleplayer environment, or on a small server
        with friends.

    .. grid-item-card:: Forge Server & Client :octicon:`chevron-right`
        :link: forge
        :link-type: doc
        :class-title: sd-text-primary 

        Forge is recommended for running Terra in a singleplayer environment, or on a small server
        with friends. If you only wish to use Terra without other Forge specific mods, we recommend
        using Fabric instead.

    .. grid-item-card:: Bukkit Server :octicon:`chevron-right`
        :link: bukkit
        :link-type: doc
        :class-title: sd-text-primary 

        Recommended for large servers for lots of people. You'll probably want to use
        Bukkit, simply because of all the plugins available for large servers. We do not
        recommend using Bukkit for small servers, for that, use Fabric.

**All Present & Past Releases**

Want to know if Terra will run on your version of Minecraft? You can find a complete list of all
supported, unsupported, and legacy releases of Terra for all platforms :doc:`here <versions>`.

.. note::

    Lots of people get confused about what the difference is between Bukkit, Spigot, and Paper.

    **Bukkit** is an API, a way for developers to interface with and write plugins
    for the Minecraft server.

    **Spigot** is an *implementation* of the Bukkit API, It's a platform that allows the Minecraft
    server to load and run Bukkit plugins. Bukkit itself is no longer maintained by the Bukkit team,
    so now SpigotMC maintains both Bukkit (the API) and Spigot (the implementation).

    **Paper** is a *fork* of Spigot, a project based on Spigot that extends It's functionality. Paper
    adds many performance optimizations to the Minecraft server, and also extends the Bukkit API.

    **What does this have to do with Terra?**

    We refer to the entire Bukkit ecosystem (Bukkit API, Spigot, Paper and friends..) as *Bukkit*
    simply because Bukkit is the name of the API. **However** - Terra develops against and tests on
    Paper. We do this because Bukkit and Spigot simply do not expose the required API for Terra to
    be fully functional. Paper's extended API does. This means that while Terra will still *work*
    on Spigot, there will be (important) features missing.

    **TL;DR - Use Paper, or a fork of Paper.**
