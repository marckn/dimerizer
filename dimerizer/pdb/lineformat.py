import re
# pdb whacky vintage format
def editline(line, offset, coffset=(0,0,0)):
   """
   Edits a line in a .pdb file respecting the PDB standard
   
   PDB has specific positions for each stored variable. This is taken into consideration 
   when editing (or adding) a line in a .pdb file. All is required is 
   to take a pdb line and create one (or two) new line(s) where 
   the atom index and x-coordinate are shifted by some offset passed as arguments
   -------------------------------------------------------------------------------------
   Arguments:
   line: String, a line of a .pdb file to be edited
   
   offset: Integer. The offset the atom index is shifted.
   
   coffset: Integer 3-ple. The offset of the coordinate shift in each direction. Only the X direction is implemented.
   
   """
   atmidx=re.findall(r"\b\d+\b",line)[0]   
   
   atmidx = int(atmidx)+int(offset)
   
   atmidx=str(atmidx)
   entryp=11- len(atmidx)  # no need to pad with 0 because we only sum
   
   lline=list(line)
   
   for i in xrange(0,len(atmidx)):
      lline[entryp+i]=atmidx[i]   
      
      
   # applying coordinates offset
   atm=re.findall(r" -{0,1}\d+\.\d* ",line)[0]
   atm=float(atm)+coffset[0]
   atms = "%.3f" % atm
   atms = list(atms)
   entryp= 38 - len(atms)
   for i in xrange(0,len(atms)):
      lline[entryp+i]=atms[i]  

   lmod="".join(lline)
   
   return lmod
