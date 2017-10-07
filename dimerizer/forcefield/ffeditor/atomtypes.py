import dimerizer.forcefield.basic_parsing_tools as parser
import dimerizer.forcefield.basic_manip as manip

def edit(fname,outfile,dtags):
   """
   Read the atomtype file and insert the necessary tags
   """
   
   flist = parser.filetolist(fname)
   
   # temporary section to conform to find_line format
   tmpsec=("atoms",1*flist)
   
   for ctg in dtags:
      tfnd=manip.find_lines(tmpsec,[ctg])
      if len(tfnd) == 0:
         raise ValueError("Tag ",ctg," not found in forcefield atomtypes file")
      else:
         stradd="{0:7s} {1:10f}".format(ctg+"_B",float(tfnd[0][1][1]))
	 flist.append(stradd)
	 
	 stradd="{0:7s} {1:10f}".format(ctg+"_V",0.0)
	 flist.append(stradd)
	 

   fho = open(outfile,"w+")
   for ln in flist:
      fho.write(ln+"\n")
      
   fho.close()
