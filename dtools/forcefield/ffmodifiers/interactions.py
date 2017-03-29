from dtools.forcefield import basic_parsing_tools as parser
from dtools.forcefield import basic_manip as manip
import line_util as line
def intmod(sec,ilist,ntags,list_halve):
   """
   Manupulate a section of a topology file adding the dimerized interactions.
   
   sec is a section tuple (keyword,data), ilist is the list of the 
   entries to modify (the entry is specified as a list of two tags).
   Returns a new section tuple with the modified data.
   
   ntags is the number of columns representing the atom tags and 
   list_halve is a list containing the column indices of the values to halve 
   where appropriate in the dimerized lines. 
   This function is meant to be invoked by wrappers for each section that needs to be modified
   """

   # get values
   for en in ilist:
      ff = manip.find_line(sec,en)[1]
      ltadd=line.dimerize_line(ff,ntags,list_halve)
      sec = manip.append_lines(sec,ltadd)
      
   return sec


def bondmod(sec,ilist):
   """
   Wrapper for bonds interactions. See intmod.
   """
   return intmod(sec,ilist,2,[4])
   

def anglemod(sec,ilist):
   """
   Wrapper for angle interactions. See intmod.
   """
   return intmod(sec,ilist,3,[5,7])
   

def constraintmod(sec,ilist):
   """
   Wrapper for constraints. See intmod.
   """
   return intmod(sec,ilist,2,[])

def dihedralmod(sec,ilist):
   """
   Wrapper for dihedral interactions. See intmod.
   """
   return intmod(sec,ilist,4,[6])


def pairmod(sec,ilist):
   """
   Wrapper for nonbonded pair interactions. See intmod.
   """
   return intmod(sec,ilist,2,[])   # NO HALVING HERE


def atomtypesmod(sec,ilist):
   """
   Wrapper for nonbonded atomtypes interactions...
   """
   return intmod(sec,ilist,1,[6])   # NEED ANOTHER ONE
