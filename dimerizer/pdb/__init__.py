"""
This package parses, modifies and writes pdb files

The standard Gromacs .pdb input file is mandatory and this package 
produces a dimerized version of the file. Dimerized version means that 
each non-solvent atom appears as a structure consisting of two beads and 
one (optional but suggested) virtual site representing its center of mass.
An atom in the .pdb, say:

ATOM      1  CH3 ACE     1       9.730   9.760  12.670  1.00  0.00

becomes:

ATOM      1     CH3 ACE     1       9.730   9.760  12.670  1.00  0.00

...

ATOM      1+N   CH3 ACE     1       9.731   9.760  12.670  1.00  0.00

...


ATOM      1+2N  CH3 ACE     1       9.732   9.760  12.670  1.00  0.00


where N is the number of atoms to be dimerized as given as first argument when launching the dimerizer script. 
These atoms should be placed in the first lines of the input .pdb file and generally can be considered as "solute".
The coordinates are slightly shifted because otherwise Gromacs complains about overlapping atoms. If virtual sites are not 
used the last line will not be added.

"""

__all__=["pdb_read","pdb_write","lineformat"]
