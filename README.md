# dimerizer
Tool to convert a standard Gromacs input to a dimerized one. 
There are also two support scripts that help setting up and controlling 
the simulation. One is plread, that scans through plumed.*.dat files 
in search for the keyword given as argument and then allows to edit 
the value in each of the file with a single command.

The other is tune_replicas, a script that given the lowest sigma 
will create a number of replicas with sigmas so that exchange 
probabilities are close to the target value.
