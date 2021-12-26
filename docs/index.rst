===================
Terra Documentation
===================

.. attention::

    This documentation site is under construction! Some things may not work currently, we're working to get it up
    and running properly. Want to help? Check out the GitHub Repo for instructions on contributing:

    .. button-link:: https://github.com/PolyhedralDev/TerraDocs
        :color: primary
        :outline:

        :octicon:`mark-github` TerraDocs

Terra is a modern world generation modding platform, primarily for Minecraft. Terra allows complete customization of
world generation with an advanced API, tightly integrated with a powerful configuration system.


Terra consists of several parts:
 - A voxel world generation API with emphasis on configuration and extensibility
 - Several platform implementations, the layer between the API and the platform it's running on.
 - An addon loader, which allows addons to interface with the Terra API in a platform-agnostic setting
 - Several "core addons," which implement the "default" configurations of Terra. These addons can be thought of as the config "standard library"


.. toctree::
    :maxdepth: 3
    :titlesonly:

    install/index
    config/index
    api/index