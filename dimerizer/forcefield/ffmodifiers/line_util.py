from itertools import permutations

def dimer_lines(dtype, ntags):
   """
   Returns all the possible combinations for a dimer interaction line without repetitions.
   
   
   dtype is the tag to be added, either _B or _V.
   ntags is the list of tags to be processed
   
   An example is best to explain: 
   If ntags is a collection of three tags, TAG1 TAG2 TAG3 and dtype is _B, the resulting 
   list of tags is :
   
   TAG1_B TAG2 TAG3
   TAG1 TAG2_B TAG3
   TAG1 TAG2 TAG3_B
   TAG1_B TAG2_B TAG3
   TAG1_B TAG2 TAG3_B
   TAG1 TAG2_B TAG3_B
   TAG1_B TAG2_B TAG3_B
   
   """
   pbb=[tuple([dtype for i in range(0,ntags)])]
   
   for i in range(1,ntags):
      ptrm=[dtype for j in range(0,i)]
      ptrm= ptrm + ["" for j in range(i,ntags)]
      ptrm = list(permutations(ptrm))
      pbb=pbb+ptrm
   
   return list(set(pbb))

def getnewlines(values,tagmod,vtohalve=None,atomtypes=False,isvirtual=False,ispair=False,isaltvirtual=False,altvirtualzero=[]):
   """
   For every tag combination in tagmod produce the new interaction lines.
   
   tagmod is the list of tags to be used for the new interaction lines. 
   
   values is the list of lines to be used. Can be more than one in the case of 
   dihedral interactions with func=9.
   
   the bead-bead interactions are halved, vtohalve takes this into account by passing 
   a list of indices whose value has to be halved.
   
   This function handles also the [ atomtypes ] section of a forcefield, where 
   virtual atoms are considered accordingly.
   
   altvirtual specifies that the line is related to the alternate virtual sites for PME: interaction coefficients 
   have to be set to 0, the location of these coefficients is given with the altvirtualzero list.
   """
   lnl=[]
   for cval in values:
      nvalues=[]+cval
      ln=""
      allbeads=True
      onebead=False
      for i,val in enumerate(tagmod):
         nvalues[i]=nvalues[i]+val
	 if not val == "_B":
	    allbeads=False
	 else:
	    onebead=True
   
      divide_fac=1
      if onebead:
         divide_fac=2
	 
      if allbeads and ispair:
         divide_fac=4
            
      if isinstance(vtohalve,list):
         for vidx in vtohalve:
            nvalues[vidx]=float(nvalues[vidx])/divide_fac
	 
      if atomtypes:
         if isvirtual:
	    nvalues[2]=0  # zero mass
	    nvalues[4]="V"
	 if isaltvirtual:
	    nvalues[2]=0  # zero mass
	    nvalues[4]="V"
	    nvalues[5]=0   # zero LJ parameters
	    nvalues[6]=0
	       
      else:
         if isaltvirtual:
	    for i in altvirtualzero:
	       nvalues[i]=0.0
      
      for i,val in enumerate(nvalues):
         ln=ln+"{"+str(i)+":8s} "
	 
      
      nvalues = map(lambda x: str(x), nvalues)
       
      ln=ln.format(*nvalues)
      lnl.append(ln)
      
   return lnl
   
   
def dimerize_line(values, ntags, vtohalve,atomtypes=False,ispair=False, doaltvirtual=False, altvirtualzero=[]):
   """
   From an interaction line determine all the necessary dimerized interactions. 
   If a list is passed, it is considered as a whole block (i.e. dihedral interactions with func=9)
      
   Values contains interaction data and ntags is the number of atom tags.
   vtohalve is a list with the indices of values that have teo be halved for the dimerized interactions 
   that require it.
   
   doaltvirtual adds a line for the second virtual atom _F, used to deal with PME.
   
   Returns a list containing (only) the new objects.
   """
   
   if not isinstance(values,list):
      raise ValueError("Must pass a list of value-lists")
   
   if not isinstance(values[0],list):
      values=[values]

   ltags=[]
   for vv in values:
      vc="".join(vv[0:ntags])
      ltags.append(vc)
   
   ltags=set(ltags)
   if len(list(ltags))>1:
      raise ValueError("Block must have the same tags")
   
   

   dimerized=[]
   
   
   bb = dimer_lines("_B",ntags)
   vv = dimer_lines("_V",ntags)
   
    
   for tm in bb:
      lines=getnewlines(values,tm,vtohalve,atomtypes,False,ispair)
      dimerized= dimerized+lines
   
   
   for tm in vv:
      lines=getnewlines(values,tm,None,atomtypes,isvirtual=True)  
      dimerized=dimerized+lines
      
   if doaltvirtual:
      ff = dimer_lines("_F",ntags)
      for tm in ff:
         lines=getnewlines(values,tm,None,atomtypes,isaltvirtual=True,altvirtualzero=altvirtualzero)
	 dimerized=dimerized+lines
   
   
   
   return dimerized

   	 
                  
