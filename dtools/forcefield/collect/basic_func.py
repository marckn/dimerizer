import dtools.forcefield.basic_parsing_tools as parser

def serialtotags(tags,line):
   """
   From a list of serials return a list of idx
   """
   
   tlist=[]
   for s in line:
      idx=int(s)-1
      tlist.append(tags[idx])
      
   return tlist
   
def isinline(atlist,line):
   """
   Check whether an interaction line involves some of the dimerized atoms.
   
   The interaction line is given as a list of serials.
   
   Return True/False
   """
   
   for cidx in atlist:
      cser=int(cidx)+1
      if cser in line:
         return True

   return False



def ffentries(sections,tags,atlist,ntags):
   """
   For a given section produces the entries that are involved in the dimerization process.
   
   Returns: tuple with two elements
   1) The name of the section
   2) The list of found entries. Each element is a list of tags.
   
   Input:
   sections: a list of section, section is in the usual format (name,list)
   tags: the correspondance idx - tag, see the collect_tags function
   atlist: the atoms to be dimerized
   ntags: how many tags in a line.
   """
   
    lentries=[]
    for section in sections:
       for ln in section[1]:
         prs= parser.parse_line(ln)
         if prs[0] != "Data":
            continue
	 
         if not isinline(atlist,prs[0:ntags]):
            continue
          
         tt=serialtotags(tags,prs[0:ntags])
         lentries.append(tt)
      
   return (sections[0][0],lentries)
