import re
import mdp_parser
import mdp_writer

def editfile(mdpf,outdir,allatoms,rcoulomb,ew_rtol,pme):
   """
   Interface to parse and write the modified mdp file accordingly.
   
   Arguments:
   mdpf: String. The file to parse. Will be used as basis for the name of the modified mdpfile.
   outdir: String. The directory for the output.
   allatoms: Flag, True/False. If True it means that solvent is not present and there's no need to define its energy group.
   rcoulomb:  Float. As in Gromacs mpd, the short range coulomb cutoff
   ew-rtol:   Float. As in Gromacs mpd, the weight ratio between direct and reciprocal terms in PME
   pme:       Flag, True/False. Using PME or not? 
   """
   fn_in = mdpf
   
   mdpclean = mdp_parser.parseandkill(fn_in)
   
   
   mdp_writer.writeClassical(mdpclean,outdir,mdpf,allatoms,rcoulomb,ew_rtol,pme)
   mdp_writer.writeDimer(mdpclean,outdir,mdpf,allatoms,rcoulomb,ew_rtol,pme)
   
