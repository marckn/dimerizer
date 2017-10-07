from dimerizer.forcefield import basic_parsing_tools as parser
from dimerizer.forcefield import basic_manip as manip
import line_util as line
import math
def intmod(sec,ilist,ntags,list_halve,atomtypes=False):
   """
   Manupulate a section of a topology file adding the dimerized interactions.
   
   sec is a section tuple (keyword,data), ilist is the list of the 
   entries to modify (the entry is specified as a list of N tags).
   Returns a new section tuple with the modified data.
   
   ntags is the number of columns representing the atom tags and 
   list_halve is a list containing the column indices of the values to halve 
   where appropriate in the dimerized lines. 
   This function is meant to be invoked by wrappers for each section that need to be modified
   """

   # get values
   
   for en in ilist:
      ff = manip.find_lines(sec,en)
      
	
      if len(ff) == 0:
         continue

      ff=map(lambda x: x[1], ff)
      ltadd=line.dimerize_line(ff,ntags,list_halve,atomtypes)
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


def pairmod(sec,secatlist,ilist):
   """
   Wrapper for nonbonded pair interactions. This is treated differently from the other interactions 
   because not all of the entries are in the 1-4 section of ffnonbonded. So, we need also to build them 
   with lj combination rules eps = sqrt(eps1ep2) and sigma = (sig1+sig2)/2
   
   """
   for en in ilist:
      ff = manip.find_lines(sec,en)
      if len(ff) == 0:
         ff = manip.find_lines(sec,list(reversed(en)))
	 
         if len(ff) == 0:
	    """t
	    build your 1-4 pair from forcefield params, 
	    format of ff: [(1471, ['NH1', 'O', '1', '0.262815121852', '0.648182492821'])]
	    first index (1471 ie) can be ignored
	    """
	    atdata1= manip.find_lines(secatlist,[en[0]])
	    atdata2= manip.find_lines(secatlist,[en[1]])
	    if len(atdata1) ==0 or len(atdata2) ==0:
	       continue
	    
	    sig1=float(atdata1[0][1][5])
	    eps1=float(atdata1[0][1][6])
	    sig2=float(atdata2[0][1][5])
	    eps2=float(atdata2[0][1][6])
	    
	    epsf=math.sqrt(eps1*eps2)
	    sigf=(sig1+sig2)/2
	    ldata=[en[0],en[1],'1',sigf,epsf]
	    ff.append((-1,ldata))
	    
      if len(ff) == 0:
         continue

      ff=map(lambda x: x[1], ff)
      ltadd=line.dimerize_line(ff,2,[4],False,True)
      sec = manip.append_lines(sec,ltadd)
      
      
   return sec 


def atomtypesmod(sec,ilist):
   """
   Wrapper for nonbonded atomtypes interactions...
   """
   return intmod(sec,ilist,1,[],atomtypes=True) 
