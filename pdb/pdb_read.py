import re

class parse_pdb:
   def __init__(self,fname):
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
      regexp=r'ATOM\b'
      ee=re.compile(regexp)
      if ee.match(line) is None:
         return False
      else:
         return True
