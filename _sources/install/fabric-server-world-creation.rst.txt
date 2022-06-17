============================
Fabric Server World Creation
============================

.. note::

    This guide is intended for the **Fabric** version of Terra.
    
    :doc:`Other Platform Installations <index>` :octicon:`chevron-right`

.. warning::
    We will be replacing the server's default world with a new Terra world.

    Because we are working with changes to worlds **ensure that you have made the necessary backups** before making any destructive changes!
    
    It is not possible to easily change the generator of an existing world.
    This is a good thing, as changing the generator of a world will produce broken chunk borders between old and new terrain!

Procedure
---------

1. Ensure your server is not running.

#. If you missed it above, please make a backup of any relevant world folders in your server directory.

#. Configure your server's world to use the new config as a generator:

.. card::

    #. Navigate to the ``server.properties`` file which is also contained within your server directory, and open it with any text editor.
    
    #. Assign your new generator to the default world by setting the ``level-type`` key to ``level-type=terra:<CONFIG_ID>/<CONFIG_ID>``
       (for the default pack this would be ``terra:overworld/overworld``). The pack ID must be all lowercase, e.g. for a pack called
       ``EXAMPLE``, you would use ``terra:example/example``.
   
    .. attention::

        If the ``level-type`` key doesn't exist, simply add it yourself to the end of the file.

4. Either delete the existing world folder in your server directory or rename it to something else (for example ``world_backup``).
   The name of your world can be found under the ``level-name`` key, which is also located in the ``server.properties`` file.
   The default world name is ``world``.

#. Boot your server back up.

.. note::

    Your server should re-generate the world folder during startup.

6. Join your server and check if your new world is using Terra world generation.

If you followed the steps correctly without any errors, then you have successfully set up a server with Terra!

.. note::

    Terra is a **pure server mod**. If you have Terra on a server, Vanilla clients can join the server. Terra
    does not need to be installed on clients unless playing with Terra in singleplayer.

Troubleshooting
---------------

If you run into issues during the world set up process, be sure to check you have followed each step correctly.
Check for any errors in your server logs and try to interpret what the issue might be.

If you are unable to set up a world successfully, and have attempted to fix any issues yourself,
please feel free to shoot us a message on our Discord server and provide any relevant information and most importantly the before mentioned logs!

