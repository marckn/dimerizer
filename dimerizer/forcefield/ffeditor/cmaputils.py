import re
def parse(flist):
   """
   Parse a cmap file considering its different layout.
   
   Output: list of tuples, each tuple is (string, list)
   the string is the line of the tags in the cmap file, 
   the list contains the lines of each numerical data for that tag 
   removed of the \ terminal.
   
   """
   taglst= re.compile("\D+ ")
   
   tagsec = re.compile("\[ ")
   
   retval=[]
   intag=False
   tags=""
   data=[]
   for ln in flist:
      if ln == "" or not tagsec.match(ln) is None:
         continue
	 
      if not taglst.match(ln) is None: # you're on a tag line
         if intag:
	    retval.append((tags,data))
	    tags=ln
	    data=[]
         else:
            intag=True
	    tags=ln
      
      else:	 
         ll=list(ln)
	 if ll[-1] == "\\":
	    ll = ll[:-1]
	       
	 ls = "".join(ll)
	 data.append(ls)
	       
   retval.append((tags,data))
   return retval

def findentry(cmapdata,taglist):
   """
   Given a list of 5 tags find the corresponding entry in cmap.
   
   Return a tuple (l1,l2).
   l1 is the list of the numerical entries in the tag section
   l2 is the data of that entry
   If no entry is found return None. This *should* raise an error.
   """
   for i,cen in enumerate(cmapdata):
      tagline=cen[0]
      dataline=cen[1]
      tvals = re.findall(r"\S+\b",tagline)
      ctags=tvals[0:5]
      same=True
      for le,cur in zip(taglist,ctags):
         if le != cur:
	    same=False
	    break
      
      if not same:
         same=True
	 for le,cur in zip(taglist,reversed(ctags)):
            if le != cur:
	       same=False
	       break
      
      
      if not same:
         continue
      
      return (tvals[5:],dataline)
   
   return None

def appendentry(flist,ntag,refdata,halve=False):
   """
   Append a new cmap entry to flist.
   
   ntag is the new set of tags to be used, 
   refdata is the output of findentry, 
   halve is a T/F flag that halves the energy values.
   """
   retlist=1*flist
   
   nlinetag=""
   for t in ntag:
      nlinetag=nlinetag+str(t)+" "
   
   for t in refdata[0]:
      nlinetag = nlinetag + str(t)+" ";
   
   nlinetag=list(nlinetag)
   nlinetag=nlinetag[:-1]
   nlinetag="".join(nlinetag)+"\\"
   
   retlist.append("\n"+nlinetag)
   for i,dataline in enumerate(refdata[1]):
      addl = str(dataline)
      if i != len(refdata[1])-1:
         addl=addl+"\\"
      
      retlist.append(addl)

   return retlist

