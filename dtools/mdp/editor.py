import re
import mdp_parser
import mdp_writer

def editfile(mdpf,outdir,vsites,allatoms):
   """
   Interface to parse and write the modified mdp file accordingly.
   
   Arguments:
   mdpf: String. The file to parse. Will be used as basis for the name of the modified mdpfile.
   outdir: String. The directory for the output.
   vsites: Flag, True/False. Setup for configurations with virtual sites for the center of mass of the dimers?
   allatoms: Flag, True/False. If True it means that solvent is not present and there's no need to define its energy group.
   """
   fn_in = mdpf
   fn_out = outdir+"d"+mdpf
   
   mdpclean = mdp_parser.parseandkill(fn_in)
   
   if vsites:
      mdp_writer.writeClassical(mdpclean,outdir,mdpf,allatoms)
      mdp_writer.writeDimer(mdpclean,outdir,mdpf,allatoms)
   else:
      mdp_writer.writeNoVsites(mdpclean,outdir,mdpf,allatoms)
   