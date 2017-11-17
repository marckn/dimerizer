import re

def ExtendedList(interactions, natoms,atlist, nadding=2, doubleit=False,copyclassical=False):
   """
   Extends a section of the topology file with the interactions pointing to the right beads for 
   a dimer delocalized replica.
   
   A list of interactions is passed as argument, together with the number of atoms to be dimerized and the 
   number of atom indices in the interactions list (i.e. [ bonds ] has two atom indices, [ angle ] three...).
   In this function the original list is kept as in the dimerzied topology that would still hold for the first bead of each dimer. 
   Then the list is extended with another copy of the original list where the indices have been translated by natoms to account for the 
   interactions on the second bead of each dimer.
   
   doubleit is used to double a non-dimerized interaction line. This is because the pair interaction tables 
   in gromacs is unique and thus we need to pass it halved and take it into account in topology.
   
   copyclassical will add interaction lines for the alternate virtual site as if it were the classical replica. This is required 
   in order to shift the nonbonded interactions to the center of the dimers.
   
   """
   
   finlist=[]
   
      
   for els in interactions[0]:
      extlist=[]
      deltalist=[]
      for el in els:
         extlist.append(el)
         idxs = re.findall(r'\b\d+\b',el) # list containing all ints
         remlist=idxs[nadding:]
	 
	 isdimerized=False
	 alldimerized=True
	 

	 for idx in idxs[0:nadding]:
	    if int(idx)-1 in atlist:
	       isdimerized=True
	    else:
	       alldimerized=False
	       
	 if alldimerized:
	    if doubleit:
	       extlist.append(el)  #double bead_bead pair interaction
	    
	 if not isdimerized:
	    continue
	    
	    
	 addlist=""
         for idx in idxs[0:nadding]:
            idxp=int(idx)
	    if int(idx)-1 in atlist:
	       ipos = atlist.index(int(idx)-1)
	       idxp = int(ipos) + int(natoms)+1
	       
	    addlist= addlist+"  "+str(idxp)+"   "
      
         for v in remlist:
            addlist = addlist + " "+str(v)

         deltalist.append(addlist)
	 if doubleit and alldimerized:
	    deltalist.append(addlist)  
	    
         if copyclassical:
	    addlist=""
	    for idx in idxs[0:nadding]:
               idxp=int(idx)
	       if int(idx)-1 in atlist:
	          ipos = atlist.index(int(idx)-1)
	          idxp = int(ipos) + int(natoms)+len(atlist)+1
	       
	       addlist= addlist+"  "+str(idxp)+"   "
      
            for v in remlist:
               addlist = addlist + " "+str(v)

            deltalist.append(addlist)	    
	 
      extlist = extlist + deltalist
      finlist.append(extlist)
   
   return finlist
   
   
 
def atomsExtendedList(atoms,natoms,atomlist, classical=False,usepme=False):
   """
   From the original [ atoms ] section build the dimerzied one.
   
   The [ atoms ] section for a dimerized replica is built from the 
   standard gromacs topology file. Lines for each bead are added, if 
   virtual sites are used their atom type is determined by adding "_V" 
   to their corresponding beads type. 
   """
   atlist = atoms[0][0]   # only one [ atoms ] in a topology
   
   extlist=[]
   d2last=int(0)
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      
       
      if int(data[0])-1 in atomlist:
         data[1]=data[1]+"_B" 
         if classical or usepme:
            data[6]=str(0.0)
	 else:
	    data[6]= str(float(data[6])/2)
	
	
      
      d2last=int(data[2])
      nln="{0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {5:10s} {6:10s} {7:10s}".format(*data[0:8])
      
      for rel in data[8:]:
         nln=nln+"  "+str(rel)
      
      extlist.append(nln)
	 
 
   d22last=int(0)
   ioffset=int(1)
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      if not int(data[0])-1 in atomlist:
         continue
	 
      data[0] = str(ioffset+int(natoms))
      ioffset=ioffset+1
      data[1] = data[1]+"_B"
      if classical or usepme:
         data[6]=str(0.0)
      else:
	    data[6]= str(float(data[6])/2)
      
      data[2]=str(int(data[2])+d2last)
      d22last=int(data[2])
      nln="{0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {5:10s} {6:10s} {7:10s}".format(*data[0:8])
      
      for rel in data[8:]:
         nln=nln+"  "+str(rel)
      
      extlist.append(nln)
     
   
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      
      if not int(data[0])-1 in atomlist:
         continue
	 
      data[0] = str(ioffset+int(natoms))
      ioffset=ioffset+1
      if not usepme:
         data[1] = data[1]+"_V"
      else:
         data[1] = data[1]+"_F"
      
      if not classical and not usepme:
         data[6]=str(0.0)
	 
      data[2]=str(int(data[2])+d22last)
      data[7]=str(0.0)
      
      nln="{0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {5:10s} {6:10s} {7:10s}".format(*data[0:8])
      
      for rel in data[8:]:
         nln=nln+"  "+str(rel)
      
      extlist.append(nln)
      
      
   return extlist   
      

def ClassicalExtList(interactions, natoms,atlist, nadding=2, doubleit=False,copyclassical=False):
   """
   Builds a section of the topology file with the interactions pointing to the virtual sites of each dimer. 
   This is used for the classical replica.
   
   In the classical replica the interaction is only on the virtual sites of the dimers, this function 
   simply takes the standard gromacs topology and translates the atom indices by 2N to point to the respective virtual atoms.
   
   doubleit is used to double a non-dimerized interaction line and the virtual site pair interactions. This is because the pair interaction tables 
   in gromacs is unique and thus we need to pass it halved and take it into account in topology.
   
   copyclassical is a blind flag used for convenience.
   """   
   finlist=[]
      
      
   for els in interactions[0]:
      extlist=[]
      deltalist=[]
      for el in els:
         idxs = re.findall(r'\b\d+\b',el) # list containing all ints
         remlist=idxs[nadding:]
	 
	 isdimerized=False
	 for idx in idxs[0:nadding]:
	    if int(idx)-1 in atlist:
	       isdimerized=True
	       break
	 
	 if not isdimerized:
	    extlist.append(el)	    
	    continue
	    
	 addlist=""
         for idx in idxs[0:nadding]:
            idxp=int(idx)
	    if int(idx)-1 in atlist:
	       ipos = atlist.index(int(idx)-1)
	       idxp = int(ipos) + natoms + len(atlist)+1

	    addlist= addlist+"  "+str(idxp)+"   "
      
         for v in remlist:
            addlist = addlist + " "+str(v)

         deltalist.append(addlist)
	 
      extlist = extlist + deltalist
      finlist.append(extlist)
   
   return finlist
