"""
Modules that parse, modify and write topology files

Topology files are built starting from a standard Gromacs .top file given as input.
There are basically three operations to be made on the input .top file:

* The [ atoms ] section has to be extended to take in the new atoms added in the .pdb file that make up the dimers and 
  their virtual sites. The virtual sites have a different atomtype that shadows that of the beads of the respective dimers, 
  for instance:
  
  1        CT3      1    ACE    CH3      1      -0.27     12.011 
 
  becomes:
  
  1        CT3      1    ACE    CH3      1      -0.27     12.011 
  
  ...
  
  1+N      CT3      1    ACE    CH3      1      -0.27     12.011 
  
  ...
  
  1+2N     CT3_V    1    ACE    CH3      1      -0.27     0
  
  The virtual site has zero mass so that its degree of freedom is decoupled from the 
  thermostat (and also, Gromacs doesn't complain). The charge has not been modified as it is used 
  correctly with the choice of energy groups. If virtual sites are not used, the last line is not added.
  
* The virtual sites section [ virtual_sites2 ]:
   
   This section is added in the output topology files and defines the properties of each virtual site. A dimer is built 
   with two beads and the virtual site represents the center of mass, that is also the geometrical center of the dimer. This section has lines 
   like this one:
   
   i+2N  i  i+N  1  0.5
   
   1 and 0.5 are parameters that indicate Gromacs to do an average over the two previously given coordinates.
   The virtual site of index i+2N is constructed from the beads i and i+N. Guess what...if virtual sites are not used, this part is ignored.
   
* The interactions:

  The indices of the interactions in the input Gromacs file are used to build the new topology file. If a classical replica is requested 
  there are two topology files as output; the one referring to the classical replica ends as .0.top. The other refers to all the other 
  delocalized replicas and ends with .1.top. 
  
  In the classical replica the interaction is simply shifted to the virtual site: every index is translated by 2N. The pair interactions make use of 
  tablep.xvg, which is halved to take into account the halved potential on the beads. However, here the potential has to be considered fully and thus 
  the [ pairs ] interactions are doubled.

  In the delocalized replica topology each bead has an halved potential. Every original interaction is kept as it already points to the first bead of the dimers, 
  the same pattern of interactions is repeated in the modified topology with indices translated by N so that it points to the second bead as well.

## The forcefield has to be modified
  
The bonded halved potentials have been taken care of in the forcefield where the energy parameters for each interaction have been halved. The forcefield 
has also to contain the definitions for the virtual sites; this basically means that for every line defining properties or interaction terms of 
a specie there's another one for its virtual type counterpart. The bonded interactions for virtual types are **not** halved.
  
"""

__all__=["topol_read","topol_write","outputs","dimer_extenders"]
