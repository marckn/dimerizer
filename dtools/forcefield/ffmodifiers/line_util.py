from itertools import permutations

def dimer_lines(dtype, ntags):
   """
   Returns all the possible distinguishable combinations for a dimer interaction line.
   
   dtype is the tag to be added, either _B or _V.
   """
   pbb=[tuple([dtype for i in range(0,ntags)])]
   
   for i in range(1,ntags):
      ptrm=[dtype for j in range(0,i)]
      ptrm= ptrm + ["" for j in range(i,ntags)]
      ptrm = list(permutations(ptrm))
      pbb=pbb+ptrm
   
   return list(set(pbb))

def getnewlines(values,tagmod,vtohalve=None,atomtypes=False,isvirtual=False):
   """
   For every tag combination in tagmod produce the new interaction lines
   """
   lnl=[]
   for val in values:
      nvalues=[]+val
      ln=""
      for i,val in enumerate(tagmod):
         nvalues[i]=nvalues[i]+val
   
      if isinstance(vtohalve,list):
         for vidx in vtohalve:
            nvalues[vidx]=float(nvalues[vidx])/2
	 
      if atomtypes:
         if isvirtual:
	    nvalues[2]=0  # zero mass
	    nvalues[4]="V"   
      
      for i,val in enumerate(nvalues):
         ln=ln+"{"+str(i)+":8s} "
	 
      
      nvalues = map(lambda x: str(x), nvalues)
       
      ln=ln.format(*nvalues)
      lnl.append(ln)
      
   return lnl
   
   
def dimerize_line(values, ntags, vtohalve,vsites,atomtypes=False):
   """
   From an interaction line determine all the necessary dimerized interactions. 
   If a list is passed, it is considered as a whole block (i.e. dihedral interactions with func=9)
      
   Values contains interaction data and ntags is the number of atom tags.
   vtohalve is a list with the indices of values that have teo be halved for the dimerized interactions 
   that require it.
   
   Returns a list containing (only) the new objects.
   """
   
   if not isinstance(values,list):
      raise("Must pass a list of value-lists")
   
   if not isinstance(values[0],list):
      values=[values]

   ltags=[]
   for vv in values:
      vc="".join(vv[0:ntags])
      ltags.append(vc)
   
   ltags=set(ltags)
   if len(list(ltags))>1:
      raise("Block must have the same tags")
   
   

   dimerized=[]
   
   
   bb = dimer_lines("_B",ntags)
   vv = dimer_lines("_V",ntags)
   
    
   for tm in bb:
      lines=getnewlines(values,tm,vtohalve,atomtypes,isvirtual=False)
      dimerized= dimerized+lines
   
   if vsites:
      for tm in vv:
         lines=getnewlines(values,tm,None,atomtypes,isvirtual=True)  
	 dimerized=dimerized+lines
      
   return dimerized

   	 
                  
