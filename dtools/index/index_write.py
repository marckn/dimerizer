def writeln(f,iterator,ibr=50):
   """
   Write a list on a file f on multiple lines.
   """
   ibreak=0
   for i in iterator:
      f.write(str(i+1)+" ")
      ibreak=ibreak+1
      if ibreak == ibr:
         ibreak=0
         f.write("\n")
	 
   f.write("\n")

def writeClassical(basedir,natoms,totatoms,atomlist):
   """
   Index file for the classical replica.
   
   The classical replica has two energy groups plus eventually solvent:
   INTF, NONINT, SOL. The interaction is fully evaluated in the INTF group 
   which is the collection of virtual sites representing the center of mass of each dimer.
   
   """
   f= open(basedir+"index.0.ndx","w+")
   f.write("[ system ]\n")
   
   ndimers = len(atomlist)
   
   writeln(f,xrange(0,totatoms+2*ndimers))
      
   f.write("\n\n")
   
   f.write("[ NONINT ]\n")
   writeln(f,atomlist) # atomlist is a list of indices and writeln converts it to serials
   writeln(f,range(natoms,natoms+ndimers))
   
   f.write("\n\n")   
   f.write("[ INTF ]\n")
   writeln(f,range(natoms+ndimers,natoms+2*ndimers))
   
   f.write("\n")
   
   if natoms != totatoms or ndimers != natoms:
      f.write("\n\n")
      f.write("[ NONDIM ]\n")
      sc = set(range(0,natoms))
      snon = sc - set(atomlist)
      writeln(f, list(snon))
      writeln(f,xrange(natoms+2*ndimers,2*ndimers+totatoms))
 
      f.write("\n")
      
   f.close()
   
def writeDimer(basedir,natoms,totatoms,atomlist,nrep=1):
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
   
   ndimers = len(atomlist)
   writeln(f,xrange(0,totatoms+2*ndimers))
    
   f.write("\n\n")
   
   f.write("[ INT1 ]\n")
   writeln(f,atomlist)
      
   f.write("\n\n")
   
   f.write("[ INT2 ]\n")
   writeln(f,xrange(natoms,natoms+ndimers))
      
   f.write("\n\n")
   
   f.write("[ NONINT ]\n")
   writeln(f,xrange(natoms+ndimers,natoms+2*ndimers))
   
   f.write("\n")

   if natoms != totatoms or ndimers != natoms:
      ibreak=0
      f.write("\n\n")
      f.write("[ NONDIM ]\n")
      sc = set(range(0,natoms))
      snon = sc - set(atomlist)
      writeln(f, list(snon))
      writeln(f,xrange(natoms+2*ndimers,2*ndimers+totatoms))
   
      f.write("\n")

   f.close()


def writeNoVsites(basedir,natoms,totatoms,atomlist):
   """
   Following the consideration that if the dimer is strongly localized 
   the results are indistinguishable from a classical simulation one can build 
   a replica exchange set-up without classical replica. In such case only two groups (INT1,INT2) plus solvent (SOL) 
   are required because virtual sites are not defined.
   """
   f= open(basedir+"index.ndx","w+")
   f.write("[ system ]\n")
   
   ndimers = len(atomlist)
   
   writeln(f,xrange(0,totatoms+ndimers))

   f.write("\n\n")
   
   f.write("[ INT1 ]\n")
   writeln(f,atomlist)
      
   f.write("\n\n")
   
   f.write("[ INT2 ]\n")
   writeln(f,xrange(natoms,natoms+ndimers))

   f.write("\n")
   if natoms != totatoms or ndimers != natoms:
      f.write("\n\n")
      f.write("[ NONDIM ]\n")
      sc = set(range(0,natoms))
      snon = sc - set(atomlist)
      writeln(f, list(snon))
      writeln(f,xrange(natoms+ndimers,ndimers+totatoms))

   f.write("\n")

   f.close()
