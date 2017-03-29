import dtools.forcefield.collectfromtopology as collect
import dtools.forcefield.ffmodifiers.interactions as ffmod

def editfile(fname,linvolved,outdir, kind,vsites=True):
   """
   Modify a forcefield file and write the modified one in outdir.
   
   linvolved is a list of involved line for each topology section. 
   Some arbitrary matching has to be done and that's why 
   kind is passed. kind is the type of forcefield file. It recognizes:
   "atomtypes", "cmap", "others", the last one used also as fallback.
   """   
   
   if kind == "atomtypes":
      pass
   elif kind == "cmap":
      pass
   else:
      
   


def editdir(topfile,atlist,charmmdir,outdir,vsites):
   """
   Modify the forcefield accounting for the required topology.
   
   Input: the topology filename, the dimerized atom indices, 
   the forcefield directory and an output directory.
   """
   
   (tags,dtags) = collect.collect_tags(topfile,atlist)
   
   
   
   linvolved = collect.lines_involved(topfile,tags,atlist)
   
   editfile(charmm+"atomtypes.atp",linvolved,outdir+"atomtypes.atp","atomtypes",vsites)
   editfile(charmm+"cmap.itp",linvolved,outdir+"cmap.itp","cmap",vsites)
   editfile(charmm+"ffbonded.itp",linvolved,outdir+"ffbonded.itp","others",vsites)
   editfile(charmm+"ffnonbonded.itp",linvolved,outdir+"ffnonbonded.itp","others",vsites)
   editfile(charmm+"ffnabonded.itp",linvolved,outdir+"ffnabonded.itp","others",vsites)
   editfile(charmm+"ffnanonbonded.itp",linvolved,outdir+"ffnanonbonded.itp","others",vsites)
   
