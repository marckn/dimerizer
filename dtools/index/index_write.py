def writeClassical(basedir,natoms,totatoms):
   """
   Index file for the classical replica.
   
   The classical replica has two energy groups plus eventually solvent:
   INTF, NONINT, SOL. The interaction is fully evaluated in the INTF group 
   which is the collection of virtual sites representing the center of mass of each dimer.
   
   """
   f= open(basedir+"index.0.ndx","w+")
   f.write("[ system ]\n")
   for i in xrange(0,3*natoms):
      f.write(str(i+1)+" ")
   
   ibreak=0
   if natoms != totatoms:
      f.write("\n")
      for i in xrange(3*natoms,2*natoms+totatoms):
         f.write(str(i+1)+" ")
	 ibreak=ibreak+1
	 if ibreak==100:
	    ibreak=0
	    f.write("\n")
	 
   f.write("\n\n")
   
   f.write("[ NONINT ]\n")
   for i in xrange(0,2*natoms):
      f.write(str(i+1)+" ")
   
   f.write("\n\n")   
   f.write("[ INTF ]\n")
   for i in xrange(2*natoms,3*natoms):
      f.write(str(i+1)+" ")
   
   f.write("\n")
   
   if natoms != totatoms:
      ibreak=0
      f.write("\n\n")
      f.write("[ SOL ]\n")
      for i in xrange(3*natoms,2*natoms+totatoms):
         f.write(str(i+1)+" ")
	 ibreak=ibreak+1
	 if ibreak==100:
	    ibreak=0
	    f.write("\n")
   
 
      f.write("\n")
      
   f.close()
   
def writeDimer(basedir,natoms,totatoms,nrep=1):
   """
   Index file for the delocalized replicas.
   
   The non-classical dimer replicas have halved interaction on each 
   dimer bead and the virtual sites are non-interacting. There are thus 
   three energy groups plus solvent: INT1, INT2, NONINT, SOL.
   Two distinct energy groups are required for each bead because the non-bonded 
   interaction between the two groups has to be switched off.
   """
   f = open(basedir+"index."+str(nrep)+".ndx","w+")
   f.write("[ system ]\n")
   for i in xrange(0,3*natoms):
      f.write(str(i+1)+" ")

   if natoms != totatoms:
      ibreak=0
      f.write("\n")
      for i in xrange(3*natoms,2*natoms+totatoms):
         f.write(str(i+1)+" ")
	 ibreak=ibreak+1
	 if ibreak==100:
	    ibreak=0
	    f.write("\n")

	 
   f.write("\n\n")
   
   f.write("[ INT1 ]\n")
   for i in xrange(0,natoms):
      f.write(str(i+1)+" ")
      
   f.write("\n\n")
   
   f.write("[ INT2 ]\n")
   for i in xrange(natoms,2*natoms):
      f.write(str(i+1)+" ")
      
   f.write("\n\n")
   
   f.write("[ NONINT ]\n")
   for i in xrange(2*natoms,3*natoms):
      f.write(str(i+1)+" ")
   
   f.write("\n")

   if natoms != totatoms:
      ibreak=0
      f.write("\n\n")
      f.write("[ SOL ]\n")
      for i in xrange(3*natoms,2*natoms+totatoms):
         f.write(str(i+1)+" ")
       	 ibreak=ibreak+1
	 if ibreak==100:
	    ibreak=0
	    f.write("\n")

   
      f.write("\n")

   f.close()


def writeNoVsites(basedir,natoms,totatoms):
   """
   Following the consideration that if the dimer is strongly localized 
   the results are indistinguishable from a classical simulation one can build 
   a replica exchange set-up without classical replica. In such case only two groups (INT1,INT2) plus solvent (SOL) 
   are required because virtual sites are not defined.
   """
   f= open(basedir+"index.ndx","w+")
   f.write("[ system ]\n")
   for i in xrange(0,2*natoms):
      f.write(str(i+1)+" ")

   if natoms != totatoms:
      ibreak=0
      f.write("\n")
      for i in xrange(3*natoms,2*natoms+totatoms):
         f.write(str(i+1)+" ")
       	 ibreak=ibreak+1
	 if ibreak==100:
	    ibreak=0
	    f.write("\n")


   f.write("\n\n")
   
   f.write("[ INT1 ]\n")
   for i in xrange(0,natoms):
      f.write(str(i+1)+" ")
      
   f.write("\n\n")
   
   f.write("[ INT2 ]\n")
   for i in xrange(natoms,2*natoms):
      f.write(str(i+1)+" ")

   f.write("\n")
   if natoms != totatoms:
      ibreak=0
      f.write("\n\n")
      f.write("[ SOL ]\n")
      for i in xrange(3*natoms,2*natoms+totatoms):
         f.write(str(i+1)+" ")
 	 ibreak=ibreak+1
	 if ibreak==100:
	    ibreak=0
	    f.write("\n")


   f.write("\n")

   f.close()