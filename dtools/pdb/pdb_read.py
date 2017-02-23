import re

class parse_pdb:
   """
   A parser for PDB files.
   """
   def __init__(self,fname):
      """
      Reads a .pdb file and stores it in a list.
    
      Each line of a given .pdb file is stored as a string in a list.
      """
      with open(fname,'r') as f:
         self.raw = f.read()
      
      self.rbuff=[]
      ln=""
      for c in self.raw:
         if c != "\n":
            ln=ln+c
         else:
            self.rbuff.append(ln)
            ln=""
            
      # rbuff is a list containing the .pdb file
      
   def isatom(self,line):
      """
      Regular expression to identify the pdb lines containing informations about an atom.
   
      PDB format supplies various system informations such as box size, comments, headers. Those lines 
      are preserved in the output pdb file. The modifications involve only the lines describing each atom 
      (index, coordinates, tag, ...): these lines are identified with this function that can return either True or False.
      """
      regexp=r'ATOM\b'
      ee=re.compile(regexp)
      if ee.match(line) is None:
         return False
      else:
         return True
