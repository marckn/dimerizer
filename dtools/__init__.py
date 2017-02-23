"""
The package containing the i/o functionalities required by the 
dimerizer script. 

Dimerizer can deal with the following files:

* # pdb
  The configuration of the system provided in pdb format. 
  This file is read and the specified part of the system will be 
  dimerized. 

* # topology 
 The Gromacs topology file describing the 
 bonded and pair interactions between atoms. 

* # mdp 
 The Gromacs settings .mdp file. Some options have to be 
 activated/deactivated in order to set up a Dimer simulation.

* # index 
 Different energy groups are declared in the .mdp file and 
 the relative index files are created here.

* # plumed 
  The Plumed plugin is required for Metadynamics and to 
introduce the Dimer interaction in the system. A minimalistic file can be 
created with this package.

"""
