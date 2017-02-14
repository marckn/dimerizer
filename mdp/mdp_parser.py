import re
def parseandkill(fn_in):
   rexp = r".*(vdw_type|vdw\-type|coulombtype|cutoff\-scheme|energygrps|integrator|\
               |energygrp_table|rcoulomb\-switch|rvdw\-switch|ntscalcenergy).*"
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
