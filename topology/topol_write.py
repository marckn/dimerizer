import topol_read
import outputs

class dimerizer:
   def __init__(self,parser, natoms, basename, nrep=1):
      self.parser = parser
      self.natoms=natoms
      self.basename=basename
      self.replicas = nrep
      
      
   def buildClassical(self):
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
      
      outputs.classical(out_file,self.parser.rbuff,atoms,bonds,pairs,angles,dihedrals,cmap,self.natoms)
      
   
   def buildDimer(self, nreplicas=None, virtualsites=True):
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
      
      outputs.dimer(out_file,self.parser.rbuff,atoms,bonds,pairs,angles,dihedrals,cmap,self.natoms,vsites=virtualsites)
