import dtools.forcefield.collect.collectfromtopology as collect
import dtools.forcefield.ffeditor.atomtypes as ffat
import dtools.forcefield.ffeditor.cmap as ffcmap
import dtools.forcefield.ffeditor.inter as ffinter
import dtools.forcefield.ffmodifiers.interactions as ffmod

def editdir(topfile,atlist,charmmdir,outdir,vsites):
   """
   Modify the forcefield accounting for the required topology.
   
   Input: the topology filename, the dimerized atom indices, 
   the forcefield directory and an output directory.
   """
   
   (tags,dtags) = collect.collect_tags(topfile,atlist)
   
   linvolved = collect.lines_involved(topfile,tags,atlist)
   # linvolved is a list of tuples (type,entry_list)
   
   alldihedrals = collect.dihedral_lines(topfile,tags)
   
   
   ffat.edit(charmmdir+"//atomtypes.atp",outdir+"//atomtypes.atp",dtags,vsites)
   ffcmap.edit(charmmdir+"//cmap.itp",outdir+"//cmap.itp",linvolved,vsites)
   
   readingkey={
      "bondtypes"         : (["bonds"],ffmod.bondmod),
      "constrainttypes"   : (["constraints"],ffmod.constraintmod),
      "angletypes"        : (["angles"],ffmod.anglemod),
      "dihedraltypes"     : (["(dihedrals|impropers)"],ffmod.dihedralmod),
      "atomtypes"         : ([""],ffmod.atomtypesmod),
      "pairtypes"         : (["pairs"],ffmod.pairmod)
   }
   
   ddtags = map(lambda x : [x], dtags)
   ffinter.editfile(charmmdir+"//ffbonded.itp",outdir+"//ffbonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   ffinter.editfile(charmmdir+"//ffnonbonded.itp",outdir+"//ffnonbonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   ffinter.editfile(charmmdir+"//ffnabonded.itp",outdir+"//ffnabonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   ffinter.editfile(charmmdir+"//ffnanonbonded.itp",outdir+"//ffnanonbonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   
