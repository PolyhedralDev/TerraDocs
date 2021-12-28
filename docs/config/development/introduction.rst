===============================
Config Development Introduction
===============================

This section goes over some general information, and the basic setup
preceding actual config pack development, including a basic overview
of how Terra works and the process of setting up an appropriate
development workspace.

How Terra Works as a Platform
=============================

Terra is composed of several parts that facilitate world generation:

.. card::

    **A Voxel World Generation API**
        The base framework for world generation.

    **An Addon Loader**
        Allows for loading addons, which integrate the API to provide functionality.
        The majority of Terra's functionality comes from addons, as without them Terra
        wouldn't do much. This is similar to how mod loaders like Fabric and Forge won't
        do much without any mods installed.

    **Core Addons**
        A suite of addons that provides standard functionality to Terra.

    **Configuration Packs**
        A collection of configuration files that utilize the functionality provided
        by addons to define how worlds generate.

    **Platform Implementations**
        The layer between the platform (such as Bukkit or Fabric) and the API.
        Platform implementations typically package the API, addon loader, core
        addons, and a default configuration pack together to work as one cohesive
        unit.


As a config developer, you will primarily be utilizing addons via Terra's
configuration system to define how worlds generate. It is still a good idea to
have an understanding of how these components interact, as it will provide a richer
understanding of what is going on under the hood.

.. warning::

    Do not follow the rest of this guide on any live production environment.

1. Setting Up Your Test Environment
===================================

Before beginning development on a new pack, you will need a suitable server or
client to test with. We recommend using a `Fabric <https://fabricmc.net>`__
client to develop config packs on, however this choice is ultimately up to you.
You can refer to the :doc:`Getting Started </install/index>` page for instructions
on how to get Terra up and running on your desired platform.

Accessing Console
-----------------

Once you have Terra running on your platform of choice, you should ensure you have
access to your console. This will be dependent on the platform you're running Terra
on, as well as the launcher or wrapper you start it from. We won't be covering how
to find the console on every platform as that is outside the scope of this guide.

.. dropdown:: Mojang Minecraft Launcher
    :animate: fade-in

    1. Start the launcher and navigate to the settings page by clicking on this
    button in the bottom left:

    .. image:: /img/config/development/mojang-launcher/settings.png

    2. Enable displaying the output log on game startup here:

    .. image:: /img/config/development/mojang-launcher/open-output-log.png

    A window with the console log will now open when you start Minecraft.

.. dropdown:: MultiMC Launcher
    :animate: fade-in

    1. Open up the MultiMC settings window.

    2. Enable console log display on launch:

    .. image:: /img/config/development/multimc-launcher/settings-enable-console.png

    A window with the console log will now open when you start Minecraft.

.. _editor:

Picking an Editor
-----------------

When developing config packs, an editor will be the main tool you use, so It's
important that you use a suitable one for the job. You're free to use any editor
you're comfortable with, but we *highly* suggest using one with the following
features:

.. dropdown:: Syntax Highlighting
    :animate: fade-in

    Having syntax highlighting in an editor will make understanding and writing
    configs much easier, as you will be able to tell at a glance how things are
    structured. To emphasize this point, here is a comparison:

    .. grid:: 3
        :margin: auto

        .. grid-item-card:: 
            :text-align: center

            **Without Highlighting**
            ^^^
            .. image:: /img/config/development/editor/notepad-yaml.png
                
        .. grid-item-card:: 
            :text-align: center

            **With Highlighting**
            ^^^
            .. image:: /img/config/development/editor/vscode-yaml-highlighting.png

.. dropdown:: Built In File Explorer
    :animate: fade-in

    Using a text editor which lets you open entire folders as projects rather than
    just individual files will make pack development more streamlined and convenient.
    The ability to quickly swap between configs, view your pack hierarchy at a glance,
    and manage subdirectories within your text editor is a must if you want to get
    things done conveniently. This will save you plenty of time not having to manage
    an external file editor on top of your editor tabs and or instances.

    .. image:: /img/config/development/editor/file-explorer.png
        :scale: 75 %

Recommended Editors
...................

`VSCode <https://code.visualstudio.com>`__ :octicon:`chevron-right`

`IntelliJ IDEA Community Edition <https://www.jetbrains.com/idea/download/>`__ :octicon:`chevron-right`

2. Locating the Terra Directory
===============================

You will need to know where the Terra directory is located, as this will be where all the files
relevant to config development go:

.. tab-set::

    .. tab-item:: Fabric

        ``/config/Terra/``

    .. tab-item:: Bukkit

        ``/plugins/Terra/``

Within this directory are two subdirectories:

.. grid:: 2

    .. grid-item-card:: ``Terra/packs``

        Contains all your installed config packs. By default, Terra will come pre-installed
        with a config pack under the file name ``default.zip`` inside this directory.

    .. grid-item-card:: ``Terra/addons``

        Contains all your installed addons. Similarly to the default pack, Terra will also
        come pre-installed with a set of *Core Addons* as explained at the beginning of
        this page.

3. Beginning Config Development
===============================

From this point on, you have the option of either beginning a new pack from scratch, or
modifying an existing pack.

.. grid:: 2

    .. grid-item-card:: Creating a Pack From Scratch :octicon:`chevron-right`
        :class-title: sd-text-primary
        :link-type: doc
        :link: pack-from-scratch/index

        Starting from nothing is a great way to understand what every part of the process
        entails. You will learn how each part of config development connects together to
        construct a fully fledged world generator. If you want to make something totally
        unique and personalized for a server or personal project, or just want to learn
        how world generation works, we recommend following this guide.

    .. grid-item-card:: Modifying an Existing Pack :octicon:`chevron-right`
        :class-title: sd-text-primary
        :link-type: doc
        :link: modifying-existing-pack 

        Making changes to an existing pack is a more hands off approach where most of the
        heavy lifting has been done for you, great for if you just want to tweak a couple
        small details here and there. This guide won't explain as much as the 'from scratch'
        guide, so if you're having difficulties understanding how to make modifications, we
        recommend following that in addition to this guide.
