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

5. Replace ``PACK_ID`` with an installed config pack's ID. The ID for the default pack that comes pre-installed with Terra
   is ``OVERWORLD``, so if you have not installed any other config packs, replace ``PACK_ID`` with ``OVERWORLD``.

6. Either delete the existing world folder (the name of this folder is covered above) in your server directory, or
   rename it to something else (for example ``world_backup``).

7. Boot your server back up.

.. note::

    Your server should re-generate the world folder during startup.

8. Join your server and check if your new world is using Terra world generation.

If you followed the steps correctly without any errors, then you have successfully set up a server with Terra!

Setting up Another World
------------------------

If you have already done this process before and wish to set up another existing world (such as the Nether or End) with
a new generator, you can simply add the world under the ``worlds`` key like so:

.. code-block:: yaml
  :caption: bukkit.yml
  :emphasize-lines: 4-5
   
   worlds:
     existing_world_name: 
       generator: Terra:EXAMPLE_PACK_1
     <NEW WORLD NAME>: 
       generator: <NEW GENERATOR ID>

Here is an example with two worlds configured:

.. code-block:: yaml
  :caption: bukkit.yml

   worlds:
     world: 
       generator: Terra:OVERWORLD
     world_nether: 
       generator: Terra:NETHER

Troubleshooting
---------------
If you run into issues during the world set up process, be sure to check you have followed each step correctly.
Check for any errors in your server console/logs and try to interpret what the issue might be.

If you are unable to set up a world successfully, and have attempted to fix any issues yourself,
please feel free to shoot us a message on our Discord server and provide any relevant information and most importantly the before mentioned logs!

