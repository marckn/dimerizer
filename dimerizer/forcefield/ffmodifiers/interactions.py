from dimerizer.forcefield import basic_parsing_tools as parser
from dimerizer.forcefield import basic_manip as manip
import line_util as line
def intmod(sec,ilist,ntags,list_halve,vsites,atomtypes=False):
   """
   Manupulate a section of a topology file adding the dimerized interactions.
   
   sec is a section tuple (keyword,data), ilist is the list of the 
   entries to modify (the entry is specified as a list of N tags).
   Returns a new section tuple with the modified data.
   
   ntags is the number of columns representing the atom tags and 
   list_halve is a list containing the column indices of the values to halve 
   where appropriate in the dimerized lines. 
   This function is meant to be invoked by wrappers for each section that needs to be modified
   """

   # get values
   
   for en in ilist:
      ff = manip.find_lines(sec,en)
      	 
      if len(ff) == 0:
         continue

      ff=map(lambda x: x[1], ff)
      ltadd=line.dimerize_line(ff,ntags,list_halve,vsites,atomtypes)
      sec = manip.append_lines(sec,ltadd)
      
      
   return sec


def bondmod(sec,ilist,vsites):
   """
   Wrapper for bonds interactions. See intmod.
   """
   return intmod(sec,ilist,2,[4],vsites)
   

def anglemod(sec,ilist,vsites):
   """
   Wrapper for angle interactions. See intmod.
   """
   return intmod(sec,ilist,3,[5,7],vsites)
   

def constraintmod(sec,ilist,vsites):
   """
   Wrapper for constraints. See intmod.
   """
   return intmod(sec,ilist,2,[],vsites)

def dihedralmod(sec,ilist,vsites):
   """
   Wrapper for dihedral interactions. See intmod.
   """
   
   return intmod(sec,ilist,4,[6],vsites)


def pairmod(sec,ilist,vsites):
   """
   Wrapper for nonbonded pair interactions. See intmod.
   """
   return intmod(sec,ilist,2,[],vsites)   # NO HALVING HERE


def atomtypesmod(sec,ilist,vsites):
   """
   Wrapper for nonbonded atomtypes interactions...
   """
   return intmod(sec,ilist,1,[],vsites,atomtypes=True) 
