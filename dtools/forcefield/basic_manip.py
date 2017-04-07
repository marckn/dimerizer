import basic_parsing_tools as parser

def find_lines(sec,ident,action="Report"):
   """
   Remove or simply find a line from a section.
   
   The line is identified by the tag parameter list ident, 
   and the section is the tuple sec, defined as in get_section.
   
   If the line is found this function returns a tuple with 
   the index in datalist and a list of values.
   """
   
   datalist = sec[1]
   retvals=[]
   irem=[]
      
   for i,el in enumerate(datalist):
      lvals = parser.parse_line(el)
      if lvals[0] != "Data":
         continue
      
      lvals=lvals[1]
      if len(ident) > len(lvals):
         raise("Too many tags in the search query")
	 
      found=True
      for vquery,vline in zip(ident,lvals[0:len(ident)]):
         if vline != "X" and vquery != vline:
	    found = False
	    break

      if not found:
         continue
	 
      irem.append(i)
      retvals.append((i,lvals))
	 
   if action == "Remove":
      for i in reversed(irem):
         datalist=datalist[0:i]+datalist[i+1:]
	 
      return (sec[0],datalist)
   else:
      return retvals
      
def append_lines(sec,ndata):
   """
   Appends new lines in a section and returns the new section. 
   
   sec is the usual section tuple, ndata is the list of 
   new lines
   """
   if not isinstance(ndata,list):
      ndata=[ndata]
   
   datalist=1*sec[1]
      
   for ndd in ndata:
      datalist.append(ndd)
   
   return (sec[0],datalist)

def remove_lines(sec,ident):
   """
   Wrapper function. Removes a line from sec. 
   
   See find_line.
   """
   return find_lines(sec,ident,"Remove")




def explX_line(sec,ident):
   """
   If tag referes to a ff line with wildcards add an explicit line.
   
   The line is identified by the tag parameter list ident, 
   and the section is the tuple sec, defined as in get_section.
   
   This function returns a section with the 
   added explicit line (if found).
   """
   datalist = sec[1]
   ltoadd=[]
   for i,el in enumerate(datalist):
      lvals = parser.parse_line(el)
      if lvals[0] != "Data":
         continue
      
      lvals=lvals[1]
      if len(ident) > len(lvals):
         raise("Too many tags in the search query")
	 
      
      found=True
      for vquery,vline in zip(ident,lvals[0:len(ident)]):
         if vline != "X" and vquery != vline:
	    found = False
	    break

      if not found:
         continue
      
      if not "X" in lvals[0:len(ident)]:
         continue
      	 
      ndata=ident + lvals[len(ident):]
      
      newl=""
      for i,val in enumerate(ndata):
         newl=newl+"{"+str(i)+":8s} "
	
      ndata = map(lambda x: str(x), ndata)
      newl=newl.format(*ndata) 
      ltoadd.append(newl)
      
   if len(ltoadd) > 0:
      return append_lines(sec,ltoadd)
   
   return sec

def killInvolvedWildcards(sec, ltag):
   """
   Scan through a section and remove every line containing a wildcard 
   that is related to a dimerized atom.
   """
   
   datalist=sec[1]
   sec2=1*sec
   
   for lst in datalist:
      lvals=parser.parse_line(lst)
      if lvals[0] != "Data":
         continue

      ltg=lvals[1]
      found=True
      for vquery,vline in zip(ltag,ltg[0:len(ltag)]):
         if vline != "X" and vquery != vline:
	    found = False
	    break
      
      
      if not found:
         continue
       
      line=lvals[1]
      if "X" in line[0:len(ltag)]:
         sec2=remove_lines(sec2,line[0:len(ltag)])
	 
   return sec2   
