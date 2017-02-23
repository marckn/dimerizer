import pdb_read
import lineformat
import re

class dimerizer:
   """
   Takes a standard .pdb file as input and produces a dimerized version.
   """
   def __init__(self,oread,fout,natoms=None):
      """
      Determines some prerequisites for the editing of the PDB file.
   
      Before editing the lines of the input .pdb file some properties have to be determined.
      These are: 
   
      *the 'entrypoint', that is the position of the first line after the header. It 
      marks the beginning of the dimerization process.
   
      * The total atoms found in the input .pdb file, compared with the number of atoms that 
      will be dimerized (input parameter) 
      """
      self.fhand = open(fout,'w+')
      self.oread = oread
      
      for n,ln in enumerate(oread.rbuff):
         if oread.isatom(ln) is True:
	    self.entrypoint = n
	    break
	
      self.totatoms=0
      for n,ln in enumerate(oread.rbuff):
         if oread.isatom(ln) is True:
	    self.totatoms = self.totatoms + 1
	    
	    
      if natoms is None:
         self.natoms = self.totatoms
      else:
         self.natoms = natoms
      	    
      
		    
   def buildConfig(self,dovsites):
      """
      Writes a new pdb containing the dimerized configuration.
   
      This method supports an output dimer configuration with or without virtual sites (dovsites).
      The lines are added sequentially, starting from the unmodified first bead, then adding 
      lines for the second bead with indices shifted by N and X-coordinate by 0.002 and finally, 
      if requested, the virtual sites with indices shifted by 2N and placed at the center of mass of each dimer. 
      """
      self.fhand.write("REMARK    MODIFIED BY DIMERIZER.\n REMARK    CITE: JCTC...\n")
      
      basetocopy=[]

      atc=0
      restart=0
      
      for n,ln in enumerate(self.oread.rbuff):
         self.fhand.write(ln+"\n")
	 if n >= self.entrypoint:
	    basetocopy.append(ln)
	 if self.oread.isatom(ln):
	    atc = atc+1
	    
	 if atc == self.natoms:
	    restart=n+1
	    break
	    
      
      for el in basetocopy:
         if self.oread.isatom(el) is True:
	    el=lineformat.editline(el,self.natoms,(0.002,0,0))
	    
	 self.fhand.write(el+"\n")
	 
      if dovsites:
         offset=2*self.natoms
	 for el in basetocopy:
            if self.oread.isatom(el) is True:
	       el=lineformat.editline(el,2*self.natoms,(0.001,0,0))
      	 
	    self.fhand.write(el+"\n")
      
      else:
         offset=self.natoms	
	
      for n in range(restart,len(self.oread.rbuff)):
         ln = self.oread.rbuff[n]
	 if self.oread.isatom(ln) is True:
	    ln = lineformat.editline(ln,offset)
	 self.fhand.write(ln+"\n")
      
      self.fhand.close()
