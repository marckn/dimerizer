import topol_read
import outputs

class dimerizer:
   """
   From a parsed topology file build dimerized versions.
   """
   def __init__(self,parser, natoms, atomlist,basename,pme, nrep=1):
      self.parser = parser
      self.natoms=natoms
      self.basename=basename
      self.replicas = nrep
      self.atlist=atomlist
      self.usepme=pme
      
      
   def buildClassical(self):
      """
      Produce a .top file for the dimer classical replica.
      
      From the parser obtain the lists of the relevant sections, extend and write them on a file 
      with the outputs module.
      """
      nms=self.basename.split(".")
      out_file = nms[0:len(nms)-1]
      out_file = reduce(lambda x,y : x+"."+y, out_file)
      out_file = out_file+".0.top"
            
      atoms = self.parser.getKeyword("atoms")
      
      bonds = self.parser.getKeyword("bonds")
      
      pairs = self.parser.getKeyword("pairs")
      
      angles = self.parser.getKeyword("angles")
      
      dihedrals = self.parser.getKeyword("(dihedrals|impropers)")
      
      cmap = self.parser.getKeyword("cmap")
      
      outputs.classical(out_file,self.parser.rbuff,atoms,bonds,pairs,angles,dihedrals,cmap,self.natoms,self.atlist)
      
   
   def buildDimer(self, nreplicas=None):
      """
      Produce a .top file for the dimer delocalized replicas.
      
      From the parser obtain the lists of the relevant sections, extend and write them on a file 
      with the outputs module.
      """
      if not nreplicas is None:
         nms=self.basename.split(".")
         out_file = nms[0:len(nms)-1]
         out_file = reduce(lambda x,y : x+"."+y, out_file)
         out_file = out_file+"."+str(nreplicas)+".top"
      else:
         out_file=self.basename
	 
	 
      atoms = self.parser.getKeyword("atoms")
      
      bonds = self.parser.getKeyword("bonds")
      
      pairs = self.parser.getKeyword("pairs")
            
      angles = self.parser.getKeyword("angles")
      
      dihedrals = self.parser.getKeyword("(dihedrals|impropers)")

      cmap = self.parser.getKeyword("cmap")
      
      outputs.dimer(out_file,self.parser.rbuff,atoms,bonds,pairs,angles,dihedrals,cmap,self.natoms,self.atlist,self.usepme)
