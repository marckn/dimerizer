"""
Collect informations from topology files.

This module recovers the following informations from an input topology file:
   
   * The atom tags involved in the simulation and in the dimerization
   
   * The dihedral interactions.
   
This is meant to be a module with all the functionality necessary to query a topology file 
and get the tag combinations to be matched with the forcefield interaction tables. Only 
these lines will be adapted to a dimerized simulation.

"""
