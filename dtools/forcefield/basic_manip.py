import basic_parsing_tools as parser

def find_line(sec,ident, action="Report"):
   """
   Remove or simply find a line from a section.
   
   The line is identified by the tag parameter list ident, 
   and the section is the tuple sec, defined as in get_section.
   
   If the line is found this function returns a tuple with 
   the index in datalist and a list of values.
   """
   
   datalist = sec[1]
   for i,el in enumerate(datalist):
      lvals = parser.parse_line(el)
      if lvals[0] != "Data":
         continue
      
      lvals=lvals[1]
      if len(ident) > len(lvals[1]):
         raise("Too many tags in the search query")
	 
      found=True
      for vquery,vline in zip(ident,lvals[0:len(ident)]):
         if vquery != vline:
	    found = False
	    break

      if not found:
         continue
	 
      if action=="Remove":
         datalist=datalist[0:i]+datalist[i+1:]
	 return (sec[0],datalist)
      else:
         return (i,lvals)
      
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

def remove_line(sec,ident):
   """
   Wrapper function. Removes a line from sec. 
   
   See find_line.
   """
   return find_line(sec,ident,"Remove")
