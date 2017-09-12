import dimerizer.forcefield.basic_parsing_tools as parser
import basic_func as basic

def collect_tags(fname, atomlist):
   """
   Collect the dimerized atomtypes.
   
   fname is a topology filename, atomlist is 
   the list of atom INDICES (0 to N-1)
   
   Returns:
   tuple with two elements: 
   1) a list of tags with idx-tag correspondance 
   2) the list of dimerized tags without repetitions
   """
   
   lfile=parser.filetolist(fname)
   asec = parser.get_section(lfile,"atoms")[0]
   
   tags=[]
   dtags=[]
   
   for ln in asec[1]:
      prs=parser.parse_line(ln)
      if prs[0] != "Data":
         continue

      serial= int(prs[1][0])
      tag   = prs[1][1]
      tags.append(tag)
      
      if serial-1 in atomlist:
         dtags.append(tag)
	 
      
   dtags = list(set(dtags))
   return (tags,dtags)
   
   
def lines_involved(fname,tags, atlist):
   """
   For each interaction line return the tags involved by the dimerization.
   
   Return a list of tuples, each tuple contains:
   1 - the kind of interaction (angle, dihedral, ...)
   2 - the list of tag combinations
   
   Input:
   the topology filename
   the idx - tag correspondance
   the list of atoms to be dimerized
   """
   
   lfile=parser.filetolist(fname)
   
   sec_bonds=parser.get_section(lfile,"bonds")
   sec_pairs=parser.get_section(lfile,"pairs")
   sec_angles=parser.get_section(lfile,"angles")
   sec_dihedrals=parser.get_section(lfile,"(dihedrals|impropers)")
   sec_cmap=parser.get_section(lfile,"cmap")
   
   
   rval=[]
   l1 = basic.ffentries(sec_bonds,tags,atlist,2)
   if not l1 is None:
      rval.append(l1)
      
   l2 = basic.ffentries(sec_pairs,tags,atlist,2)
   if not l2 is None:
      rval.append(l2)
   
   l3 = basic.ffentries(sec_angles,tags,atlist,3)
   if not l3 is None:
      rval.append(l3)
   
   l4 = basic.ffentries(sec_dihedrals,tags,atlist,4)
   if not l4 is None:
      rval.append(l4)
   
   l5 = basic.ffentries(sec_cmap,tags,atlist,5)
   if not l5 is None:
      rval.append(l5)
   
   return rval
   

def dihedral_lines(fname,tags):
   """
   For each dihedral interaction line return the tags.
   
   Return a list of tuples, each tuple contains:
   1 - the kind of interaction (angle, dihedral, ...) - for conformity
   2 - the list of tag combinations
   
   Input:
   the topology filename
   the idx - tag correspondance
   """
   
   lfile=parser.filetolist(fname)
   
   sec_dihedrals=parser.get_section(lfile,"(dihedrals|impropers)")

   rval=[]
   l4 = basic.ffentries(sec_dihedrals,tags,range(0,len(tags)),4)
   if not l4 is None:
      rval.append(l4)
   
   return rval      
      
