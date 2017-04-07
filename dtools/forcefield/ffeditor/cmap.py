import dtools.forcefield.basic_parsing_tools as parser
import dtools.forcefield.ffmodifiers.line_util as permute

import cmaputils
def edit(fname,outfile,linvolved,vsites):
   """
   Edit the cmap file.
   """
   
   cmlist=None
   for tp in linvolved:
      if tp[0]=="cmap":
         cmlist=tp[1]
	 break

   if cmlist is None:
      return
   
      
   flist = parser.filetolist(fname)
   cmpp = cmaputils.parse(flist)

   for entry in cmlist:
      fnd = cmaputils.findentry(cmpp,entry)
      if fnd is  None:
         raise("Cannot find CMAP entry")
      
      taglist=fnd[0]
      data=fnd[1]
      bentries=permute.dimer_lines("_B",taglist)
      for ltag in bentries:
         cmaputils.appendentry(flist,ltag,data, halve=True)
      
      if vsites:
         ventries=permute.dimer_lines("_V",taglist)
         for ltag in ventries:
	    cmaputils.appendentry(flist,ltag,data,halve=False)
      

   # print new file from flist
   fo = open(outfile,"w+")
   for ln in flist:
      fo.write(ln+"\n")
      
   fo.close()
