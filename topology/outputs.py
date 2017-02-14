import dimer_extenders as de

def inject_modtop(f,lns):
   for ln in lns:
      f.write(ln+"\n")
      
def addVirtualSites(at,nat):
   at.append("; virtual sites for the center of mass of the dimers")
   at.append("[ virtual_sites2 ]")
   for i in xrange(1,nat+1): 
      site = i+2*nat
      a1 = i
      a2 = i + nat
      at.append("  "+str(site)+"  "+str(a1)+"  "+str(a2)+"  1  0.5") 

def addHeader(f):
   f.write("""
   ;This file has been edited by the Dimerizer tool for the Dimer enhanced sampling method.
   ;Please cite the Dimer paper: JCTC ...
   
   """)
   

def dimer(out_file, olist,atoms, bonds, pairs, angles, dihedrals, cmap, natoms, extendlist=de.ExtendedList, vsites=True):
   f = open(out_file,'w+')
   
   addHeader(f)
   ext_atoms = de.atomsExtendedList(atoms, natoms,vsites)
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
   dimer(out_file, olist,atoms, bonds, pairs, angles, dihedrals, cmap, natoms,extendlist=de.ClassicalExtList, vsites=True)
	 
	          
