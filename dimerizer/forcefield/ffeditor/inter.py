import dimerizer.forcefield.basic_parsing_tools as parser
import dimerizer.forcefield.write_func as wr
from dimerizer.forcefield import basic_manip as manip

def editfile(fname,fout,tags,linvolved,alldihedrals,readingkey,vsites):
   """
   Given a forcefield file and the atomic tags obtained from the topology file make a new forcefield file 
   with the dimerized interactions.
   
   The function scrolls through the sections of the forcefield file as 
   defined in readingkey. 
   
   fname: the forcefield file to be used
   
   fout: the new forcefield file
   
   tags: the atom tags involved in the dimerization
   
   linvolved: all the tags involved in the dimerization for each section of the topology file.
      linvolved is a list where each element is a tuple (string,lines). String is the name of the 
      topology section and lines is a list of interactions that have to be dimerized.
      
   readingkey: is a dictionary containing the correspondance of the forcefield sections to the topology sections.
   Each entry in the dictionary is a tuple with: the name of the topology section, and the function used to edit the 
   interaction lines in the forcefield files. 
   
   vsites: is a flag that specifies whether virtual sites need to be added or not.
   
   alldihedrals: every dihedral interaction in the topology has to be considered here, irrespective of the fact that it 
   is being dimerized or not. This is used because the dihedral interactions defined in the forcefield with one or more 
   wildcards "X" (ie X TAG1 TAG2 X) have to be made explicit because X cannot be extended to the new _B and _V tags.
   """
   flist = parser.filetolist(fname)
   try:
      fhand= open(fout,"w+")
   except:
      print "\t ... "+str(fname)+" not present"
      return
   
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
