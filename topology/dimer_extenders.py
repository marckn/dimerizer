import re

def ExtendedList(bonds, natoms, nadding=2):
   
   finlist=[]
   
      
   for els in bonds[0]:
      extlist=[]
      deltalist=[]
      for el in els:
         extlist.append(el)
         idxs = re.findall(r'\b\d+\b',el) # list containing all ints
         subs=el.split(idxs[nadding-1],1)
	 addlist=""
         for idx in idxs[0:nadding]:
            idxp = int(idx) + int(natoms)
	    addlist= addlist+"  "+str(idxp)+"   "
      
         addlist = addlist+subs[1]

         deltalist.append(addlist)  
	 
      extlist = extlist + deltalist
      finlist.append(extlist)
   
   return finlist
   
   
 
def atomsExtendedList(atoms,natoms,vsites=True):
   atlist = atoms[0][0]   # only one [ atoms ] in a topology
   extlist=atlist*1
   
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      data[0] = int(data[0])+int(natoms)
      nln=""
      for v in data:
         nln= nln+str(v)+"   "
      
      extlist.append(nln)
   
   if not vsites:
      return extlist   
   
   for ln in atlist:
      data = re.findall(r' \S+',ln)
      data[0] = int(data[0])+int(2*natoms)
      data[1] = data[1]+"_V"
      data[7]=0
      nln=""
      for v in data:
         nln= nln+str(v)+"   "
      
      extlist.append(nln)
      
      
   return extlist   
      

def ClassicalExtList(bonds, natoms, nadding=2):
   
   finlist=[]
      
      
   for els in bonds[0]:
      extlist=[]
      deltalist=[]
      for el in els:
         idxs = re.findall(r'\b\d+\b',el) # list containing all ints
         subs=el.split(idxs[nadding-1],1)
	 addlist=""
         for idx in idxs[0:nadding]:
            idxp = int(idx) + int(2*natoms)
	    addlist= addlist+"  "+str(idxp)+"   "
      
         addlist = addlist+subs[1]

         deltalist.append(addlist)  
	 
      extlist = extlist + deltalist
      finlist.append(extlist)
   
   return finlist
