"""
A collection of plumed inputs for a minimalistic Dimer simulation.

Plumed is used here to introduce the Dimer interaction in Gromacs.

This is obtained with a linear restraint on the Dimer collective variable (CV). The Dimer CV 
is the binding energy of the Dimer and should be available in a future release of Plumed (if not, check out my 
Plumed fork on github).

Note that these templates are intended to be rather skinny in order to avoid misunderstandings. You should set your desired 
output in the PRINT section, remembering that in the classical replica you can compute properties on the virtual sites. 
If you don't want to needlessly use more replicas than required, Metadynamics on the Dimer CV is strongly advised.

One can easily enhance the sampling only on a part of the system (i.e. a loop in a protein) by defining two Dimer CVs: 
one dimerizing the atoms in the part that should be enhanced and one dimerizing the remaining part of the system (solvent is never dimerized). 

"""

__all__=['templates']
