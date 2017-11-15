import re
def parseandkill(fn_in):
   """
   Parse an input .mdp file and remove the lines that will be redefined.
   
   To avoid confusion and possible misunderstending due to comments and indentations a regular expression 
   is used to find every line containing the keyword that will be modified. These lines will not appear in the output file, 
   where a new redefinition of the removed settings will be appended at the end of the file.
   """
   
   rexp = r".*(vdw_type|vdw\-type|coulombtype|cutoff\-scheme|energygrps|integrator|\
               |energygrp_table|rcoulomb\-switch|rvdw\-switch|nstcalcenergy|energygrp\-excl|\
	       |rcoulomb|ew-rtol).*"
   reg = re.compile(rexp)
   
   lines=[]
   raw=""
   with open(fn_in,'r') as f:
         raw = f.read()
      
   ln=""
   for c in raw:
      if c != "\n":
         ln=ln+c
      else:
         if reg.match(ln) is None:
	    lines.append(ln)
	 
         ln=""

   
   return lines
