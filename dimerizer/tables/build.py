from scipy.special import erfcinv
from scipy.special import erfc
import math

def btab(outdir,rcoulomb,ew_rtol,usepme,scut=0.04,dx=0.002):
   """
   Build short range interactions tables.
   INPUT:
      outdir   =   output directory. Tables will be among input files
      rcoulomb =   short-range cutoff for both coulomb and LJ
      ew_rtol  =   weight ratio between coulomb short and long range
      usepme   =   [True/False] toggle for tables compatible with PME-User
      scut     =   short distance cutoff of the interaction
      dx       =   table resolution. Don't change on whim.
   """
   
   beta=erfcinv(ew_rtol)/rcoulomb
   npoints = int((rcoulomb+1)/dx +1)
   names_half=["table_INT1_NONDIM.xvg","table_INT2_NONDIM.xvg",
	       "table_NONDIM_INT1.xvg","table_NONDIM_INT2.xvg"]

   names_full=["table_INTF_INTF.xvg","table_NONDIM_NONDIM.xvg",
               "table_INTF_NONDIM.xvg","table_NONDIM_INTF.xvg"]
	       

   names_double=["table_INT1_INT1.xvg","table_INT2_INT2.xvg"]
   
   fhalved=[]
   ffull=[]
   fdoubled=[]
   
   for st in names_half:
      fhalved.append(open(outdir+"/"+st,"w"))
   
   for st in names_full:
      ffull.append(open(outdir+"/"+st,"w"))
      
   for st in names_double:
      fdoubled.append(open(outdir+"/"+st,"w"))
   
   fpair =  open(outdir+"/tablep.xvg","w")
   
   fgen = open(outdir+"/table.xvg","w")
   
     
   for i in xrange(npoints):
      cx = float(i*dx)
      ln= "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,0,0,0,0,0,0)
      if cx < scut:
         fpair.write(ln)
	 fgen.write(ln)
	 for f in ffull:
	    f.write(ln)
	   
	 for f in fhalved:
	    f.write(ln)
	 
	 for f in fdoubled:
	    f.write(ln)
	 
         continue
     
     
      fdr = 1./cx
      fpdr = 1./(cx*cx)
      gdr = -1./(cx**6)
      gpdr =-6.0/(cx**7)
      hdr = 1./(cx**12)
      hpdr =12.0/(cx**13)
      lnpair = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,fdr,fpdr,gdr,gpdr,hdr,hpdr)
      
      if usepme:
         fdr = (erfc(beta*cx)-1.0)/cx
	 term1 = 2*cx*beta*math.exp(-(beta*cx)**2) / math.sqrt(math.pi)
	 fpdr= (term1 + erfc(beta*cx)-1.0)/cx**2
	 lnempty = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,-fdr,-fpdr,0,0,0,0)
	 lnfull = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,0,0,gdr,gpdr,hdr,hpdr)
	 lndouble = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,fdr,fpdr,gdr/2,gpdr/2,hdr/2,hpdr/2)
	 lnhalf = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,0,0,gdr/2,gpdr/2,hdr/2,hpdr/2)
      else:
         lnempty= "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,0,0,0,0,0,0)
	 lnfull = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,fdr,fpdr,gdr,gpdr,hdr,hpdr)
	 lndouble = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,2*fdr,2*fpdr,gdr/2,gpdr/2,hdr/2,hpdr/2)
	 lnhalf = "%12.10e   %12.10e %12.10e   %12.10e %12.10e   %12.10e %12.10e\n" % (cx,fdr,fpdr,gdr/2,gpdr/2,hdr/2,hpdr/2)
	  	       
   
   
      fpair.write(lnpair)
      fgen.write(lnempty)
      for f in ffull:
         f.write(lnfull)
	   
      for f in fhalved:
         f.write(lnhalf)
	 
      for f in fdoubled:
         f.write(lndouble)
