import re

class parse_topol:
   """
   Read a topology file and provide access to its different sections
   
   The input topology file is stored in a list. A method in this class 
   returns a sublist containing the sections corresponding to the keyword given as argument. 
   For each section its position in the file is returned as well.
   
   """
   def __init__(self,fname):
      """
      Open and read the file passed as argument and store each line in a list.
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
	    
      # rbuff is a list containing the .top file
           


   
   def getKeyword(self,kword):
      """
      Return a section of the topology file identified by the keyword passed as argument.
      
      Regular expressions are used to identify comment lines, any section identifier, 
      the requested section (or sections) and whether we are still in a section or not.
      
      These regexps are used to remove unwanted parts of the files (comments, # directives, ...) and 
      delimit the desired sections. This is done while scanning the whole file. 
      The returned value is a tuple with the following format:
      
      (nfound,nindices)
      
         - nfound is a list where each element corresponds to the data (as a list) of a section with the requested keyword.
	 - nindices is a list that follows the ordering of nfound. Each element of nindices is a couple of values storing the position of the beginning and the 
	   end of the found section.
      """
      keyword_rexp=r"\s*\[\s*.*\]"
      kwo = re.compile(keyword_rexp)
      
      keyword_targ=r"\s*\[ "+kword+r" \]\s*"
      kwo_targ = re.compile(keyword_targ)
      
      keyword_comment=r";.*"
      kwo_comment = re.compile(keyword_comment)
      
      
      keyword_data=r"(.*\d+.*)+"
      if kword == "atoms":
         keyword_data=r".*\d+.*"
	 
      kwo_data=re.compile(keyword_data)
      
      nfound=[]
      indices=[]
      getsaving=False
      idx=-1
      for n,ln in enumerate(self.rbuff):
         
	 cmt = kwo_comment.match(ln)
	 if not cmt is None:  # ignore comments
	    continue
	 
	 mct=kwo_targ.match(ln)
	 if not mct is None:
	    idx = idx+1
	    getsaving=True   
            nfound.append([])
	    indices.append([])
	    indices[idx].append(n)
	    continue
	    	    
         if getsaving is True:
            isdata= kwo_data.match(ln)
	    if not isdata is None:
	       lst=nfound[idx]
	       lst.append(ln)
	    
	    else:
	       indices[idx].append(n)
	       if not mct is None:
	          idx = idx+1
		  nfound.append([])
		  indices.append([])
	      
	       else:
	          getsaving=False


      return (nfound,indices)
