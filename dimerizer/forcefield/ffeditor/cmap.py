import dimerizer.forcefield.basic_parsing_tools as parser
import dimerizer.forcefield.ffmodifiers.line_util as permute

import cmaputils
def edit(fname,outfile,linvolved):
   """
   Edit the cmap forcefield file. 
   
   The data format in the cmap file is different and is processed through these 
   dedicated functions.
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
         raise ValueError("Cannot find CMAP entry ")
      
      taglist=fnd[0]
      data=fnd[1]
            
      bentries=permute.dimer_lines("_B",5)
      for ltag in bentries:
         ntag=[]
         for t,suf in zip(entry,ltag):
            nl=str(t)+str(suf)
            ntag.append(nl)
	    
         flist=cmaputils.appendentry(flist,ntag,fnd, halve=True)
      
      
      ventries=permute.dimer_lines("_V",5)
      for ltag in ventries:
         ntag=[]
         for t,suf in zip(entry,ltag):
            nl=str(t)+str(suf)
            ntag.append(nl)
         
         flist=cmaputils.appendentry(flist,ntag,fnd,halve=False)
      

   # print new file from flist
   fo = open(outfile,"w+")
   for ln in flist:
      fo.write(ln+"\n")
      
   fo.close()
