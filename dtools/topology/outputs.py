import dimer_extenders as de

def inject_modtop(f,lns):
   """
   Utility function that writes a list lns to a file f.
   """
   for ln in lns:
      f.write(ln+"\n")
      
def addVirtualSites(at,nat):
   """
   Adds the [ virtual_sites2 ] section to a topology file.
   
   The topology file is passed as argument (at), it is a list. 
   The number of atoms (nat) is all that is needed to build the [ virtual_sites2 ] section.
   
   """
   at.append("; virtual sites for the center of mass of the dimers")
   at.append("[ virtual_sites2 ]")
   for i in xrange(1,nat+1): 
      site = i+2*nat
      a1 = i
      a2 = i + nat
      at.append("  "+str(site)+"  "+str(a1)+"  "+str(a2)+"  1  0.5") 

def addHeader(f):
   """
   A message informing the user of the Dimer paper he should cite.
   
   """
   f.write("""
   ;This file has been edited by the Dimerizer tool for the Dimer enhanced sampling method.
   ;Please cite the Dimer paper: J. Chem. Theory Comput. 13, 425 (2017).
   
   """)
   

def dimer(out_file, olist,atoms, bonds, pairs, angles, dihedrals, cmap, natoms, extendlist=de.ExtendedList, vsites=True):
   f = open(out_file,'w+')
   """
   From a standard Gromacs topology create the dimer .top file
   
   Each section to be modified is processed with the dimer_extenders module (entering as a function named 'extendlist' that 
   points to the right function of the module). In the case of the [ pairs ] section, if 
   a classical replica is being built, the list is doubled to take into account that the provided pairs table 
   contains a halved interaction potential.
   
   The second half of this function creates the new .top file. This file is obtained with insertions from the original .top file, so 
   that only the necessary parts are modified. To do this one needs to insert the modified sections in place of the old ones and this is done by 
   writing the new file line by line and keeping track of the line numbering in order to find the correspondence with each section. 
   To do this, each section is stored in a list called "shiftex" made by elements containing the list of the lines to be written 
   for that modified section, its beginning and end points in the original file and a flag used to avoid multiple insertions. 
   For convenience this list is sorted so that the entry point of each section is in increasing order.
   """
   
   addHeader(f)
   if extendlist.__name__ == "ClassicalExtList":
      ext_atoms = de.atomsExtendedList(atoms, natoms,vsites,True)
   else:
      ext_atoms = de.atomsExtendedList(atoms, natoms,vsites,False)
   
   if vsites:
      addVirtualSites(ext_atoms,natoms)
   
   ext_bonds = extendlist(bonds,natoms,2)
   ext_pairs = extendlist(pairs,natoms,2)
   if extendlist.__name__ == "ClassicalExtList":
      ext_pairs[0] = ext_pairs[0] + ext_pairs[0]   # with VSITES tablep is halved
      
   ext_angles = extendlist(angles,natoms,3)
   ext_dihedrals = extendlist(dihedrals,natoms,4)
   
   ext_cmap = extendlist(cmap,natoms,5)
   
   shiftex=[]
   
   
   shiftex.append([ext_atoms,atoms[1][0],False])
   
   
   for ee1,ee2 in zip(ext_bonds,bonds[1]):
      shiftex.append([ee1,ee2,False])
         
   for ee1,ee2 in zip(ext_pairs,pairs[1]):
      shiftex.append([ee1,ee2,False])
      
   for ee1,ee2 in zip(ext_angles,angles[1]):
      shiftex.append([ee1,ee2,False])
      
   for ee1,ee2 in zip(ext_dihedrals,dihedrals[1]):
      shiftex.append([ee1,ee2,False])
 
   for ee1,ee2 in zip(ext_cmap,cmap[1]):
      shiftex.append([ee1,ee2,False])
 
   shiftex.sort(key=lambda x: x[1][0])  
   
   
   for (i,ln) in enumerate(olist):
      inj=False
      for els in shiftex:
         if i>els[1][0] and i < els[1][1]:
	    inj=True
	    if els[2] is False:
	       els[2]=True
	       inject_modtop(f,els[0])
	    
	    break
      
      if inj is False:
         f.write(ln+"\n")

   f.close()	 
   	 
def classical(out_file, olist,atoms, bonds, pairs, angles, dihedrals, cmap, natoms):
   """
   From a standard Gromacs topology create the dimer .top file for the classical replica.
    
   This is handled by the previous function "dimer" with de.ClassicalExtList passed as argument.
   """
   dimer(out_file, olist,atoms, bonds, pairs, angles, dihedrals, cmap, natoms,extendlist=de.ClassicalExtList, vsites=True)
	 
	          
