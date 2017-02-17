def writeClassical(mdpclean,outdir,mdpf,allatoms):
   nms=mdpf.split(".")
   nnm = nms[0:len(nms)-1]
   nnm = reduce(lambda x,y : x+"."+y, nnm)
   nnm = outdir+nnm+".0.mdp"
   
   f = open(nnm,"w+")
   for ln in mdpclean:
      f.write(ln+"\n")
   
   str1=""
   str2=""
   str3=""
   if not allatoms:
      str1="SOL"
      str2="SOL SOL INTF SOL"
      str3="NONINT SOL"
   
      
   fstr="""
   ; lines added by DIMERIZER
   integrator=md-vv
   ntscalcenergy=1
   vdw_type=user
   coulombtype=PME-User
   cutoff-scheme=group
   energygrps=NONINT INTF %s
   energygrp_table=INTF INTF %s
   energygrp-excl=NONINT NONINT NONINT INTF %s
   """ % (str1,str2,str3)
   f.write(fstr)


def writeDimer(mdpclean,outdir,mdpf,allatoms):
   nms=mdpf.split(".")
   nnm = nms[0:len(nms)-1]
   nnm = reduce(lambda x,y : x+"."+y, nnm)
   nnm = outdir+nnm+".1.mdp"

   f = open(nnm,"w+")
   for ln in mdpclean:
      f.write(ln+"\n")
      
   str1=""
   str2=""
   str3=""
   if not allatoms:
      str1="SOL"
      str2="SOL SOL INT1 SOL INT2 SOL"
      str3="NONINT SOL"
      
   fstr="""
   ; lines added by DIMERIZER
   integrator=md-vv
   ntscalcenergy=1
   vdw_type=user
   coulombtype=PME-User
   cutoff-scheme=group
   energygrps=INT1 INT2 NONINT %s
   energygrp_table=INT1 INT1 INT2 INT2 %s
   energygrp-excl=INT1 INT2 NONINT INT1 NONINT INT2 %s
   """ % (str1,str2,str3)

   f.write(fstr)


def writeNoVsites(mdpclean,outdir,mdpf,allatoms):
   nnm = outdir+mdpf
   
   f = open(nnm,"w+")
   for ln in mdpclean:
      f.write(ln+"\n")
      
   str1=""
   str2=""
   if not allatoms:
      str1="SOL"
      str2="SOL SOL INT1 SOL INT2 SOL"


   fstr="""
   ; lines added by DIMERIZER
   integrator=md-vv
   ntscalcenergy=1
   vdw_type=user
   coulombtype=PME-User
   cutoff-scheme=group
   energygrps=INT1 INT2 %s
   energygrp_table=INT1 INT1 INT2 INT2 %s
   energygrp-excl=INT1 INT2"
   """ % (str1,str2)

   f.write(fstr)

