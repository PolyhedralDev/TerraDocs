=====================
Bukkit World Creation
=====================

.. note::

    This guide is intended for the **Bukkit** version of Terra.
    
    :doc:`Other Platform Installations <index>` :octicon:`chevron-right`

.. warning::
    We will be replacing the server's default world with a new Terra world.

    Because we are working with changes to worlds **ensure that you have made the necessary backups** before making any destructive changes!
    

We will be replacing the server's default world with a new one that uses Terra as its generator.

If you would like to use a world manager like Multiverse Core to create a world instead of manually setting it as
outlined here, please refer to :doc:`Setting a Generator Through a World Manager<worldmanager-bukkit-world-creation>`

Procedure
---------

1. Ensure your server is not running.

2. If you missed it above, please make a backup of any relevant world folders in your server directory.

3. Configure your server's world to use the new config as a generator:

.. card::

  #. Navigate to the ``bukkit.yml`` file which is also contained within your server directory, and open it with any text editor.

  #. Assign your new generator to the default world by **adding the following lines to the end of the file**:

  .. code-block:: yaml
    :caption: bukkit.yml

    worlds:
      LEVEL_NAME:
        generator: Terra:PACK_ID

  .. attention:: These lines are **not** present by default, you have to add them yourself!

4. Replace ``LEVEL_NAME`` with the server's configured ``level-name``. (This can be found in the ``server.properties`` file
   under the '``level-name``' key. By default, ``level-name`` is set to ``world``.)

.. card::

  Here is an example using the default ``world`` ``level-name``:

  .. code-block:: yaml
    :caption: bukkit.yml

    worlds:
      world:
        generator: Terra:PACK_ID

5. Replace ``PACK_ID`` with an installed config pack's ID. The ID for the default pack that comes pre-installed with Terra
   is ``OVERWORLD``, so if you have not installed any other config packs, replace ``PACK_ID`` with ``OVERWORLD``.

.. card::

  Here is the example above, using the default ``OVERWORLD`` config pack:

  .. code-block:: yaml
    :caption: bukkit.yml

    worlds:
      world:
        generator: Terra:OVERWORLD

6. Either delete the existing world folder (the name of this folder is covered above) in your server directory, or
   rename it to something else (for example ``world_backup``).

7. Boot your server back up.

.. note::

    Your server should re-generate the world folder during startup.

8. Join your server and check if your new world is using Terra world generation.

If you followed the steps correctly without any errors, then you have successfully set up a server with Terra!

Setting up Another World
------------------------

If you have already done this process before and wish to set up another **existing** world (such as the Nether or End) with
a new generator, you can simply add the world under the ``worlds`` key like so:

.. code-block:: yaml
  :caption: bukkit.yml
  :emphasize-lines: 4-5
   
   worlds:
     existing_world_name: 
       generator: Terra:EXAMPLE_PACK_1
     another_world_name:
       generator: Terra:EXAMPLE_PACK_2

.. tip::
  We highly recommend listing worlds you have set up for custom generation via a world manager here as well, in the event that the
  world manager fails. Typically the world manager will be the only thing responsible for assigning generators, but during failure
  the server will default to this config, and then vanilla generation if not specified.

  Using the bukkit config as a fallback will prevent the server defaulting to vanilla generation if failure occurs (which will cause
  chunk breaks and is very annoying to fix).

.. warning::
  This will only set the generator for worlds that already exist on the server, if a world listed here has not been created,
  Bukkit will not create a new world. For creating new worlds that are not the default Overworld, Nether, or End worlds, you
  will have to use a world management plugin.

  We do not recommend switching generators on a world that is already in use, you should only set the generator here as a fallback, or if
  you are setting up the generator for a world that has already been created on the server but has not been generated. For the latter case,
  you should clear the world data after setting the generator here before starting the server up.

Troubleshooting
---------------
If you run into issues during the world set up process, be sure to check you have followed each step correctly.
Check for any errors in your server console/logs and try to interpret what the issue might be.

If you are unable to set up a world successfully, and have attempted to fix any issues yourself,
please feel free to :doc:`ask for help </contact>` and provide any relevant information and most importantly the before mentioned logs!

