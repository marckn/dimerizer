import dimerizer.forcefield.collect.collectfromtopology as collect
import dimerizer.forcefield.ffeditor.atomtypes as ffat
import dimerizer.forcefield.ffeditor.cmap as ffcmap
import dimerizer.forcefield.ffeditor.inter as ffinter
import dimerizer.forcefield.ffmodifiers.interactions as ffmod

def editdir(topfile,atlist,charmmdir,outdir,vsites):
   """
   Modify the forcefield accounting for the required topology.
   
   Input: the topology filename, the dimerized atom indices, 
   the forcefield directory and an output directory.
   """
   
   print "Modifying forcefield..."
   (tags,dtags) = collect.collect_tags(topfile,atlist)
   
   linvolved = collect.lines_involved(topfile,tags,atlist)
   # linvolved is a list of tuples (type,entry_list)
   
   alldihedrals = collect.dihedral_lines(topfile,tags)
   tags=list(set(tags))
   
   print "\t ...atomtypes"
   ffat.edit(charmmdir+"//atomtypes.atp",outdir+"//atomtypes.atp",tags,vsites)
   print "\t ...cmap"
   ffcmap.edit(charmmdir+"//cmap.itp",outdir+"//cmap.itp",linvolved,vsites)
   
   readingkey={
      "bondtypes"         : (["bonds"],ffmod.bondmod),
      "constrainttypes"   : (["constraints"],ffmod.constraintmod),
      "angletypes"        : (["angles"],ffmod.anglemod),
      "dihedraltypes"     : (["(dihedrals|impropers)"],ffmod.dihedralmod),
      "atomtypes"         : ([""],ffmod.atomtypesmod),
      "pairtypes"         : (["pairs"],ffmod.pairmod)
   }
   
   ddtags = map(lambda x : [x], tags)
   print "\t ...ffbonded"
   ffinter.editfile(charmmdir+"//ffbonded.itp",outdir+"//ffbonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   print "\t ...ffnonbonded"
   ffinter.editfile(charmmdir+"//ffnonbonded.itp",outdir+"//ffnonbonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   print "\t ...ffnabonded"
   ffinter.editfile(charmmdir+"//ffnabonded.itp",outdir+"//ffnabonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   print "\t ...ffnanonbonded"
   ffinter.editfile(charmmdir+"//ffnanonbonded.itp",outdir+"//ffnanonbonded.itp",ddtags,linvolved,alldihedrals,readingkey,vsites)
   print "Done."
