def writeClassical(mdpclean,outdir,mdpf,nondimer,rcoulomb,ew_rtol,pme):
   """
   Gromacs MDP file for the classical replica.
   
   The classical replica has its own settings that differ from 
   those of the other delocalized replicas. A Dimer simulation with 
   a classical replica will thus have two .mdp files, one for the classical replica 
   and a different one for all the others.
   
   Arguments:
   mdpclean: List of the input .mdp file purged of the settings that will be overwritten.
   outdir: String containing the o utput directory
   mdpf: String. Contains the input .mdp filename, is manipulated to provide basename.0.mdp as output filename 
         as is usual convention for replica exchange in Gromacs.
   allatoms: Flag, True/False. If true the whole system is dimerized (i.e. there's no explicit solvent)
   
   """
   nms=mdpf.split(".")
   nnm = nms[0:len(nms)-1]
   nnm = reduce(lambda x,y : x+"."+y, nnm)
   nnm = outdir+"mdp.0.mdp"
   
   f = open(nnm,"w+")
   for ln in mdpclean:
      f.write(ln+"\n")
   
   str1=""
   str2=""
   str3=""
   str4="User"
   if pme:
      str4="PME-User"
      
   if nondimer:
      str1="NONDIM"
      str2="NONDIM NONDIM INTF NONDIM"
      str3="NONINT NONDIM"
   
      
   fstr="""
   ; lines added by DIMERIZER
   integrator=md
   nstcalcenergy=1
   vdw_type=user
   coulombtype=%s  ; can be either User or PME-User. Don't change here unless you also change tables.
   rcoulomb= %s
   ew_rtol= %s
   cutoff-scheme=group
   energygrps=NONINT INTF %s
   energygrp_table=INTF INTF %s
   energygrp-excl=NONINT NONINT NONINT INTF %s
   """ % (str4,str(rcoulomb),str(ew_rtol),str1,str2,str3)
   f.write(fstr)


def writeDimer(mdpclean,outdir,mdpf,nondimer,rcoulomb,ew_rtol,pme):
   """
   Gromacs MDP file for the delocalized replicas.
   
   This .mdp file is used for all the non-classical Dimer replicas. Only the 
   classical replica has a different mdp file.
   
   Arguments:
   mdpclean: List of the input .mdp file purged of the settings that will be overwritten.
   outdir: String containing the o utput directory
   mdpf: String. Contains the input .mdp filename, is manipulated to provide basename.1.mdp as output filename 
         as is usual convention for replica exchange in Gromacs.
   allatoms: Flag, True/False. If true the whole system is dimerized (i.e. there's no explicit solvent)
   
   """
   nms=mdpf.split(".")
   nnm = nms[0:len(nms)-1]
   nnm = reduce(lambda x,y : x+"."+y, nnm)
   nnm = outdir+"mdp.1.mdp"

   f = open(nnm,"w+")
   for ln in mdpclean:
      f.write(ln+"\n")
      
   str1=""
   str2=""
   str3=""
   str4="User"
   if pme:
      str4="PME-User"

   if nondimer:
      str1="NONDIM"
      str2="NONDIM NONDIM INT1 NONDIM INT2 NONDIM"
      str3="NONINT NONDIM"
      
   fstr="""
   ; lines added by DIMERIZER
   integrator=md
   nstcalcenergy=1
   vdw_type=user
   coulombtype=%s  ; can be either User or PME-User. Don't change here unless you also change tables.
   rcoulomb= %s
   ew_rtol= %s
   cutoff-scheme=group
   energygrps=INT1 INT2 NONINT %s
   energygrp_table=INT1 INT1 INT2 INT2 %s
   energygrp-excl=INT1 INT2 NONINT INT1 NONINT INT2 NONINT NONINT %s
   """ % (str4,str(rcoulomb),str(ew_rtol),str1,str2,str3)

   f.write(fstr)


