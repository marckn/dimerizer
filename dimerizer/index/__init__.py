"""
Creates a Gromacs index file.

In Gromacs non-bonded interactions can be computed specifically for 
subsets of atoms and for each subset the shape of the interactions can be 
provided with a table. In the index file the atoms belonging to each energy 
group are specified. The format is simple:
------------------------------------------------------

[ GROUPNAME ]

atoms specified by their serial (a number from 1 to N)

------------------------------------------------------

A set can be substantially big, especially the one defining the 
solvent ([ SOL ]) and care must be taken not to write lines bigger than 
the gromacs readline buffer.

Dimerizer uses at most 5 energy groups: INT1,INT2,INTF,NONINT,SOL
"""
__all__=["index_write"]


