import re
import mdp_parser
import mdp_writer

def editfile(mdpf,outdir,vsites,allatoms):
   fn_in = mdpf
   fn_out = outdir+"d"+mdpf
   
   mdpclean = mdp_parser.parseandkill(fn_in)
   
   if vsites:
      mdp_writer.writeClassical(mdpclean,outdir,mdpf,allatoms)
      mdp_writer.writeDimer(mdpclean,outdir,mdpf,allatoms)
   else:
      mdp_writer.writeNoVsites(mdpclean,outdir,mdpf,allatoms)
   
