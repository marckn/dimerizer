# dimerizer
---
This is a tool to convert a standard Gromacs input to a dimerized one. 
[Gromacs](http://www.gromacs.org/) is a popular tool for proteins simulation.
This script allows to run Gromacs simulations with [Dimer Metadynamics](http://pubs.acs.org/doi/abs/10.1021/acs.jctc.6b00691), 
a replica exchange method recently introduced to enhance the sampling of a probability distribution.
This scripts takes a standard Gromacs input, that consists of:  
* A simulation settings file (.mdp)
* An initial configuration file (.pdb)
* A topology file (.top)
* A forcefield folder, here we have tested charmm22* and charmm36 but any charmm forcefield *should* work.  

The result are modified files for the dimer replicas. See the examples folder for a quickstart, and 
the doc folder for the inner workings of the script. A paper will be shortly published to explain in details 
how this is done and show some benchmark and new tests of Dimer Metadynamics.


This is a python2.7 code, to install it remember to use the correct pip version (i.e. pip2.7).

# Auxiliary scripts

There are also two support scripts that help setting up and controlling 
the simulation. 

## plread

plread scans through plumed.*.dat files in search for the keyword given as 
argument and then allows to edit the value in each of the file with a single command.

## tune_replicas

tune_replicas is a script that given the parameters of the first replica will create a number 
of replicas with parameters so that the exchange probabilities are close to the target value.
