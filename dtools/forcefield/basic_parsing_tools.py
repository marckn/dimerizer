import re

def parse_line(line_in):
   """
   Parse a line of a forcefield file.
   
   Returns a tuple (type,list) where 
   type can be either "Empty", "Special" or "Data" and 
   list is a list containing the columns.
   Comment lines as well as inline comments are ignored.
   """
   
   rx_comline = re.compile(r"\s*;")
   rx_special = re.compile(r"\s*#")
   
   if not rx_comline.match(line_in) is None:
      return ("Empty",[])
      
   if not rx_special.match(line_in) is None:
      return ("Special",[line_in])
      
   lin=line_in.split(';')[0]
   data=re.findall(r'\-{0,1}\S+\b',lin)
   
   if len(data) == 0:
      return ("Empty","")
   
   return ("Data",data)


def get_section(flist, secname):
   """
   Return a list with the lines corresponding to the specified section.
   
   The forcefield file is given through its list of lines.
   The returned structure is a list of tuples (section_name,list), 
   where section_name is a string and list is the list containing all the (unparsed) lines.
   """
   keyword_rexp=r"\s*\[\s*.*\]"
   kwo = re.compile(keyword_rexp)
      
   keyword_targ=r"\s*\[ "+secname+r" \]\s*"
   kwo_targ = re.compile(keyword_targ)
   
      
   found=[]
   
   insec=False
   cfound=[]
   for ln in flist:
      if not kwo.match(ln) is None:
         if insec:
	    found.append((secname,cfound))
	    cfound=[]
	    
	 insec=False
	
      if kwo_targ.match(ln) is None:
         if insec:
	    cfound.append(ln)
	    
      else:
         insec=True
	 cfound=[]

   if len(cfound)>0:
      found.append((secname,cfound))
      
   return found
   
def get_keywords(flist):
   """
   Return the list of [ keywords ] in a forcefield file list.
   """
   
   keyword_rexp=r"\s*\[\s*.*\]"
   kwo = re.compile(keyword_rexp)
   
   kfound=[]
   for ln in flist:
      if kwo.match(ln) is None:
         continue
	 
      lnn = ln.split(";")[0]
      lnn = lnn.split("]")[0]
      lnn = lnn.split("[")[1]
      lnn=list(lnn)
      lnn=lnn[1:-1]
      lnn="".join(lnn)
      kfound.append(lnn)
      
   return kfound

   
def filetolist(fname):
   """
   Read a file and return the list of lines
   """ 
   
   with open(fname,"r") as fi:
      rawdata=fi.read()
      
   rbuff=[]
   ln=""
   for c in rawdata:
      if c != "\n":
         ln=ln+c
      else:
         rbuff.append(ln)
         ln=""
   

   return rbuff   
     
       	 
      

            
