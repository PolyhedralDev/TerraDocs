===================
Bukkit Installation
===================

.. toctree::
    :hidden:

    bukkit-server-world-creation
    worldmanager-bukkit-world-creation

.. note::

   This guide is intended for the **Bukkit** version of Terra. :doc:`Other Platform Installations <index>` :octicon:`chevron-right`

   The Bukkit version of Terra supports server platforms such as Spigot, Paper and further forks such as Purpur or Pufferfish.   
   However we highly recommend using Paper, or one of its *sane* forks (Pufferfish, Purpur, etc.),
   with Terra, since Paper is the Bukkit platform we develop for and support. 
   
   Terra will **not** be fully functional with CraftBukkit/Spigot.

.. tip::

    If you have already installed Terra or already know how to install bukkit plugins, you can skip to the world creation
    guide at the bottom of this page.

Installation
------------

#. Download the latest stable Terra bukkit release hosted on SpigotMC `here <https://www.spigotmc.org/resources/terra.85151/>`_.
   You can find what version of Terra you should download for your version of Minecraft :doc:`here <versions>`.

#. Once you have downloaded the ``.jar`` file from SpigotMC, simply place the
   file into your `plugins` folder located inside your server directory.

#. Once the plugin has been installed restart your server

#. Verify Terra has loaded, the console/logs should mention Terra somewhere

   Now is also a good time to check for any errors/warnings.

World Creation
--------------

There are two main ways to manage worlds on a Bukkit server: using a world manager (which is a separate plugin that is designed to well.. manage worlds), or directly through Bukkit.

Please refer to the guide for your relevant setup:

:doc:`Setting a Generator Through Bukkit <bukkit-server-world-creation>` :octicon:`chevron-right`

:doc:`Setting a Generator Through a World Manager <worldmanager-bukkit-world-creation>` :octicon:`chevron-right`
