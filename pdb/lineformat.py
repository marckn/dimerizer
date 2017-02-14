import re
# pdb whacky vintage format
def editline(line, offset, coffset=(0,0,0)):
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
