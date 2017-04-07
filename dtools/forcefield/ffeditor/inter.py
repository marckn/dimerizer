import dtools.forcefield.basic_parsing_tools as parser
import dtools.forcefield.write_func as wr
from dtools.forcefield import basic_manip as manip

def editfile(fname,fout,tags,linvolved,alldihedrals,readingkey,vsites):
   flist = parser.filetolist(fname)
   fhand= open(fout,"w+")
   keys=parser.get_keywords(flist)
   
   keys = list(set(keys))
   
   mdsec=[]
   for key in keys:
      csect = parser.get_section(flist,key)
      csec=[]
      
      if key == "dihedraltypes":
         for cc in csect:
            ncc=1*cc
	    for lnt in alldihedrals[0][1]:
	       ncc = manip.explX_line(ncc,lnt)
	       
	    for lnt in alldihedrals[0][1]:
	       ncc=manip.killInvolvedWildcards(ncc,lnt)
	    
	    csec.append(ncc) 
      else:
         csec=csect
      
      if key == "atomtypes":
         fproc=readingkey[key][1]
	 nsec = fproc(csec[0],tags,vsites)
	 
	 mdsec.append(nsec)
      
      for cs in linvolved:
         if cs[0] in readingkey[key][0]:
            fproc=readingkey[key][1]
	    
	    nsec=[]
	    for curr in csec:
	       ns = fproc(curr,cs[1],vsites)   
	       nsec.append(ns)
	    
	    mdsec.append(nsec)	    
	    break
   
   
   
   for sec in mdsec:    
      wr.sec_to_file(fhand,sec)
         



# linvolved: list of tuples (type,entry_list)
#readingkey: dictionary for 
#   ff keywords -> ([topology keywords], funciton_to_process)

#keys: list of ff keywords
#csec is a list of tuples (section_name, list)
