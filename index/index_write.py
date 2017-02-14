def writeClassical(basedir,natoms,totatoms):
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
