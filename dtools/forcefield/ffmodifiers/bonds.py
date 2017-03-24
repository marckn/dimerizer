from .. import basic_parsing_tools as parser
from .. import basic_manip as manip
import line_util as line
def bondmod(sec,blist):
   """
   Manupulate the bond section of a topology file adding the dimerized interactions.
   
   sec is a section tuple (keyword,data), blist is the list of the 
   entries to modify (the entry is specified as a list of two tags).
   Returns a new section tuple with the modified data.
   """

   # get values
   for en in blist:
      ff = manip.find_line(sec,en)[1]
      ltadd=line.dimerize_line(ff,2)   
      sec = manip.append_lines(sec,ltadd)
      
   return sec
