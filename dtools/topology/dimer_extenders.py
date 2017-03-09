import re

def ExtendedList(interactions, natoms, nadding=2):
   """
   Extends a section of the topology file with the interactions pointing to the right beads for 
   a dimer delocalized replica.
   
   A list of interactions is passed as argument, together with the number of atoms to be dimerized and the 
   number of atom indices in the interactions list (i.e. [ bonds ] has two atom indices, [ angle ] three...).
   In this function the original list is kept as in the dimerzied topology that would still hold for the first bead of each dimer. 
   Then the list is extended with another copy of the original list where the indices have been translated by natoms to account for the 
   interactions on the second bead of each dimer.
   """
   
   finlist=[]
   
      
   for els in interactions[0]:
      extlist=[]
      deltalist=[]
      for el in els:
         extlist.append(el)
         idxs = re.findall(r'\b\d+\b',el) # list containing all ints
         remlist=idxs[nadding:]
	 addlist=""
         for idx in idxs[0:nadding]:
            idxp = int(idx) + int(natoms)
	    addlist= addlist+"  "+str(idxp)+"   "
      
         for v in remlist:
            addlist = addlist + " "+str(v)

         deltalist.append(addlist)  
	 
      extlist = extlist + deltalist
      finlist.append(extlist)
   
   return finlist
   
   
 
def atomsExtendedList(atoms,natoms,vsites=True, classical=False):
   """
   From the original [ atoms ] section build the dimerzied one.
   
   The [ atoms ] section for a dimerized replica is built from the 
   standard gromacs topology file. Lines for each bead are added, if 
   virtual sites are used their atom type is determined by adding "_V" 
   to their corresponding beads type. 
   """
   atlist = atoms[0][0]   # only one [ atoms ] in a topology
   
   extlist=[]
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      if classical:
         data[6]=str(0.0)
	 
      nln="{0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {6:10s} {7:10s}".format(*data[0:8])
      
      for rel in data[8:]:
         nln=nln+"  "+str(rel)
      
      extlist.append(nln)
	 
      
   
   
   
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      data[0] = str(int(data[0])+int(natoms))
      if classical:
         data[6]=str(0.0)
      
      nln="{0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {6:10s} {7:10s}".format(*data[0:8])
      
      for rel in data[8:]:
         nln=nln+"  "+str(rel)
      
      extlist.append(nln)
   
   if not vsites:
      return extlist   
   
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      data[0] = str(int(data[0])+int(2*natoms))
      data[1] = data[1]+"_V"
      if not classical:
         data[6]=str(0.0)
	 
      data[7]=str(0.0)
      
      nln="{0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {6:10s} {7:10s}".format(*data[0:8])
      
      for rel in data[8:]:
         nln=nln+"  "+str(rel)
      
      extlist.append(nln)
      
      
   return extlist   
      

def ClassicalExtList(interactions, natoms, nadding=2):
   """
   Builds a section of the topology file with the interactions pointing to the virtual sites of each dimer. 
   This is used for the classical replica.
   
   In the classical replica the interaction is only on the virtual sites of the dimers, this function 
   simply takes the standard gromacs topology and translates the atom indices by 2N to point to the respective virtual atoms.
   """   
   finlist=[]
      
      
   for els in interactions[0]:
      extlist=[]
      deltalist=[]
      for el in els:
         idxs = re.findall(r'\b\d+\b',el) # list containing all ints
         remlist=idxs[nadding:]
	 addlist=""
         for idx in idxs[0:nadding]:
            idxp = int(idx) + int(2*natoms)
	    addlist= addlist+"  "+str(idxp)+"   "
      
         for v in remlist:
            addlist = addlist + " "+str(v)

         deltalist.append(addlist)  
	 
      extlist = extlist + deltalist
      finlist.append(extlist)
   
   return finlist
