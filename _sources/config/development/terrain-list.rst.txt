===========================
List of Terrain Expressions
===========================

Below is a list of terrain expressions you can try out and use for your world generation.

If you haven't already, please read the
:doc:`Terrain From Scratch </config/development/pack-from-scratch/terrain>` &
:doc:`Creating A Pack From Scratch </config/development/pack-from-scratch/introduction>`

The terrain expressions shown below can be found in the default overworld pack that comes prepacked with Terra, which
can be viewed through `GitHub <https://github.com/PolyhedralDev/TerraOverworldConfig/>`__.

Plain
=====

.. code-block:: yaml
    :caption: eq_plain.yml
    :linenos:

    # Basic relatively flat terrain.

    vars: &variables
      base: 64
      height: 10

    terrain:
      sampler:
        type: EXPRESSION
        dimensions: 3
        variables: *variables
        expression: -y + base

      sampler-2d:
        dimensions: 2
        type: EXPRESSION
        variables: *variables
        expression: (simplex(x, z)+1)/2 * height
        samplers:
          simplex:
            dimensions: 2
            type: FBM
            octaves: 4
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.0075

Desert
======

.. code-block:: yaml
    :caption: eq_desert.yml
    :linenos:

    # Flat low elevation desert terrain

    vars: &variables
      base: 64 # Base terrain y level
      groundHeight: 5 # Block height of base noise

      duneHeight: 10 # Block height of dunes
      duneSpacing: 20 # Higher number = more spacing between dunes
      duneFrequency: 0.7 # Overall dune frequency
      duneRotationRange: pi/3 # How much dune cells are randomly rotated, 0 = anisotrophic, pi = isotrophic

    terrain:
      sampler:
        dimensions: 3
        type: EXPRESSION
        variables: *variables
        expression: -y + base

      sampler-2d:
        dimensions: 2
        type: EXPRESSION
        variables: *variables
        expression: |
          duneHeight * dunes(x*duneFrequency, z*duneFrequency) * ((duneHeightVariation(x,z)/4)+0.75)
          + groundHeight * (ground(x, z)+1)/2
        samplers:
          duneHeightVariation:
            dimensions: 2
            type: FBM
            octaves: 2
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.02
          dunes: # Dune height map [0, 1]
            dimensions: 2
            type: DOMAIN_WARP
            amplitude: 5
            warp:
              type: OPEN_SIMPLEX_2
              frequency: 0.04
            sampler:
              type: DOMAIN_WARP
              amplitude: 15
              warp:
                type: OPEN_SIMPLEX_2
                frequency: 0.02
                salt: 1
              sampler: # Absolute sine wave domain rotated via CELL_VALUE, cell edges are hidden by DISTANCE_2_DIV
                type: EXPRESSION
                variables: *variables
                expression: |
                  -mask(x, z) * (-|sin((
                     x*sin(rotation(x,z)*duneRotationRange)
                    +z*cos(rotation(x,z)*duneRotationRange))/duneSpacing)|+1)
                samplers:
                  height: &cell
                    dimensions: 2
                    type: CELLULAR
                    frequency: 0.01
                  rotation:
                    <<: *cell
                    return: CellValue
                  mask:
                    <<: *cell
                    return: Distance2Div

          ground:
            dimensions: 2
            type: FBM
            sampler:
              type: OPEN_SIMPLEX_2
              frequency: 0.005

Mountains
=========

.. code-block:: yaml
   :caption: eq_mountains.yml
   :linenos:

   # Basic peaked mountains.

   vars: &variables
     base: 80
     height: 150

   terrain:
     sampler:
       dimensions: 3
       type: EXPRESSION
       variables: *variables
       expression: -y + base
       samplers:
     sampler-2d:
       dimensions: 2
       type: EXPRESSION
       expression: (noise(x, z)+1)/2 * height
       variables: *variables
       samplers:
         noise:
           dimensions: 2
           type: DOMAIN_WARP
           amplitude: 5
           warp:
             type: OPEN_SIMPLEX_2
             frequency: 0.03
           sampler:
             type: FBM
             octaves: 4
             sampler:
               type: LINEAR
               min: -1
               max: 0.2
               sampler:
                 type: CELLULAR
                 frequency: 0.008

Overhangs
=========

.. code-block:: yaml
   :caption: eq_overhangs.yml
   :linenos:

   # Shattered hills

   vars: &variables
     base: 80
     height: 35
     shatterHeight: 78

   terrain:
     sampler:
       dimensions: 3
       type: EXPRESSION
       variables: *variables
       expression: -y + base + (simplex(x, z)+1)/2 * height + |shatter(x/3, y, z/3)*shatterHeight|
       samplers:
         shatter:
           type: CLAMP
           min: -1
           max: 1
           dimensions: 3
           sampler:
             type: FBM
             dimensions: 3
             octaves: 4
             sampler:
               type: OPEN_SIMPLEX_2
               frequency: 0.025
         simplex:
           dimensions: 2
           type: FBM
           octaves: 4
           sampler:
             type: OPEN_SIMPLEX_2
             frequency: 0.0075

.. tip::
  You can check out even more terrain samplers from the default Overworld config pack, which can
  be viewed through `Github <https://github.com/PolyhedralDev/TerraOverworldConfig/>`__.