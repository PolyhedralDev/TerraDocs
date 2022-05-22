===========================
Worldmanager World Creation
===========================

Most world managers will have their own methods of setting / changing the generator for a world, however some may not
support the use of custom generators. Please refer to either the documentation or support for your preferred manager if
you're not sure whether custom generators are supported, or how to set up a world with said manager, before consulting
the Terra discord.

Since there are many different plugins with their own process we won't be covering all of them, however we do recommend
using `Multiverse Core <https://github.com/Multiverse/Multiverse-Core/wiki/>`_ if you are unsure which manager to use.


.. warning::

    Sometimes world managers will fail to correctly set the generator for a world when loading things up, which can lead
    to potentially damaging issues with your worlds such as broken chunk borders. 

    Because of this we recommend additionally configuring a world :doc:`directly through Bukkit <bukkit-server-world-creation>`
    once you have set it up through a world manager, to serve as a fail-safe in the event that a **world manager fails**.

Multiverse Core
---------------

To create a Terra world using Multiverse Core, add the following argument to the end of the
`Multiverse Create Command <https://github.com/Multiverse/Multiverse-Core/wiki/Command-Reference#create-command>`_:

``-g Terra:<PACK ID>``.

Here is an example command which will create a world with the name `example_world`, the `NORMAL` world environment, and
a Terra generator using the pack with ID `EXAMPLE`:

``/mv create example_world NORMAL -g Terra:EXAMPLE``


Troubleshooting
---------------
If you run into issues during the world set up process, be sure to check you have followed each step correctly.
Check for any errors in your server console/logs and try to interpret what the issue might be.

If you are unable to set up a world successfully, and have attempted to fix any issues yourself,
please feel free to shoot us a message on our Discord server and provide any relevant information and most importantly the before mentioned logs!

