names_half=["table_INT1_INT1.xvg", "table_INT2_INT2.xvg","tablep.xvg",
             "table_INT1_SOL.xvg","table_INT2_SOL.xvg", "table_SOL_INT1.xvg","table_SOL_INT2.xvg"]
names_full=["table_INTF_INTF.xvg", "table_SOL_SOL.xvg", "table_SOL_INTF.xvg", "table_INTF_SOL.xvg"]
names_empty=["table.xvg"]


fempty=[]
fhalved=[]
ffull=[]

for st in names_half:
   fhalved.append(open(st,"w"))
   
for st in names_full:
   ffull.append(open(st,"w"))

for st in names_empty:
   fempty.append(open(st,"w"))


dx = 0.002
rc=10

npt = (int)(rc/dx +1)

for i in xrange(0,npt):
   cx = float(i*dx)
   
   ln= "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,0,0,0,0,0,0)
   for f in fempty:
      f.write(ln)
   

   fdr=float(0)
   fpdr=float(0)
   gdr=float(0)
   gpdr=float(0)
   hdr=float(0)
   hpdr=float(0)
   
   if cx >= 0.04:
      fdr =  1./cx
      fpdr = 1./(cx*cx)
      gdr = -1./(cx**6)
      gpdr =-6.0/(cx**7)
      hdr = 1./(cx**12)
      hpdr =12.0/(cx**13)
      
   nrow="%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,fdr,fpdr,gdr,gpdr,hdr,hpdr)
    
   nrowh="%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,fdr/2,fpdr/2,gdr/2,gpdr/2,hdr/2,hpdr/2)
   
  
  
   for g in fhalved:
      g.write(nrowh)
   
   for h in ffull:
      h.write(nrow)
     
