import re

class parse_topol:
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
	    
      # rbuff is a list containing the .top file
           


   
   def getKeyword(self,kword):
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
