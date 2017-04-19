"""
Edits the Gromacs .mdp file.

A Gromacs .mdp file contains various informations about the simulation setup 
ranging from the Molecular Dynamics timestep to the thermostat parameters, 
output management and so on. A Dimer simulation in Gromacs requires some of these 
settings to be set in a particular way. This package reads a provided mdp files, 
removes the settings that need to be overridden and append the necessary modification at the 
and of the file.

The settings that are manipulated are the following:

*# vdw_type
   Van der Waals interactions are provided by user and so this changes to "User"

*# coulombtype
   Coulomb interaction is user-defined as well. By default this setting changes to PME-User. If 
   long range treatment of the Coulomb interaction is not required one can change this to User afterwards.
   
*# cutoff-scheme
   To use user-defined nonbonded interaction this must be set to group.

*# ntscalcenergy
   Replica exchange requires this parameter to be 1
   
*# integrator
   The Molecular Dynamics integrator. By default will be set to the standard 
   Gromacs "md" (Leapfrog algorithm).
   
*# energygrps
   The non-bonded interaction is not the same for the whole system and needs to be considered separately for 
   different subsystems. This is done by defining energy groups that are declared here according to what is needed. 
   See index package for more.
   
*# energygrp_table
   Non-bonded interactions are specified for each energy group by giving gromacs user-defined tables. The tables are listed here
   (read the list two by two, each pair builds a table_X_Y.xvg filename that Gromacs expects to see in the run directory)
   
*# energygrp-excl
   Non-bonded interactions can be ignored for some specified couples of energy groups. This is important when computing PME as it must be done 
   independently for each bead group (i.e. INT1,INT2)
   
"""
__all__=['editor','mdp_parser','mdp_writer']
