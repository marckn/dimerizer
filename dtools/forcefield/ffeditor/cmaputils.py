import re
def parse(flist):
   """
   Parse a cmap file considering its different layout.
   
   Output: list of tuples, each tuple is (string, list)
   the string is the line of the tags in the cmap file, 
   the list contains the lines of each numerical data for that tag 
   removed of the \ terminal.
   
   """
   taglst= re.compile("\D ")
   
   retval=[]
   intag=False
   tags=""
   data=[]
   for ln in flist:
      if ln == "":
         continue
	 
      if not taglst.match(ln) is None:
         if intag:
	    retval.append(tags,data)
	    tags=ln
	    data=[]
	 else:
	    intag=True
	    ll=list(ln)
	    if ll[-1] == "\\":
	       ll = ll[:-1]
	       
	    ls = str(ll)
	    data.append(ls)
	       
	       
   retval.append(tags,data)
   return retval

def findentry(cmapdata,taglist):
   """
   Given a list of 5 tags find the corresponding entry in cmap.
   
   Return a tuple (l1,l2).
   l1 is the list of the numerical entries in the tag section
   l2 is the data of that entry
   If no entry is found return None. This *should* raise an error.
   """
   
   for cen in cmapdata:
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
   
   nlinetag= str(ntag)+" "+str(refdata[0])+"\\"
   flist.append("\n"+nlinetag+"\n")
   for i,dataline in enumerate(refdata[1]):
      addl = str(dataline)
      if i != len(refdata[1])-1:
         addl=addl+"\\"
      
      flist.append(addl+"\n")


