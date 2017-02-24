import re
import argparse

parser = argparse.ArgumentParser(description="""
Scan for plumed.x.dat files and return the values of a 
given keyword with the possibility to overwrite them
""")

parser.add_argument('keyword',type=str, help='Keyword to be looked for')
args=parser.parse_args()
key = args.keyword

#getting files
iidx=0
fhands=[]
keepgoing=True

while keepgoing:
   try:
      plstr = "plumed."+str(iidx)+".dat"
      f = open(plstr,'r')
      fhands.append((f,plstr))
      iidx = iidx + 1
   except IOError:
      keepgoing=False

print "found %d files" % len(fhands)
reg=r"\b"+str(key)+r"=\S+\b"
regL=r"\bLABEL=\S+\b"
regCV=r"\S+: "
ffound=[]
for ifile,ff in enumerate(fhands):
   fh = ff[0]
   lstf=[]
   raw=fh.read()
   ln=""
   for c in raw:
      if c!="\n":
         ln=ln+c
      else:
         lstf.append(ln)
	 ln=""
   
   felem=[]
   for lln in lstf:	 
      alloc = re.findall(reg,lln)
      allocl = re.findall(regL,lln)
      allocCV = re.findall(regCV,lln)
      
      if len(allocl)>0:
         lab = allocl[0].partition("=")[2]
      elif len(allocCV)>0:
         lst=str(allocCV[0])
	 lab = ''.join(list(lst)[:-2])
      else:
         lab="Undefined"
      
      if len(alloc)>0:
         vals = alloc[0].partition("=")[2]
	 felem.append((vals,lab,ifile,lstf))
   
      
   felem.sort(key=lambda x: x[1])
   ffound.append(felem)
   
   


# find all the different labels
labels=[]
for fc in ffound:
   for fnd in fc:
      labels.append(fnd[1])
      
labels = list(set(labels))
print "Found "+str(len(labels))+" labels..."

if len(labels) == 0:
   raise ValueError("Nonexistent or invalid label. This script does not support LISTS")

ich=0

if len(labels)==1:
   print "... using it!\n"
else:
   print "\n ...which one do you want to edit?\n"
   st=""
   for i in range(0,len(labels)):
      st=st+"%d)  %s \t\t" % (i,labels[i])
      if (i+1) % 4 ==0:
         st=st+"\n"
   
   print st
   
   ich = int(raw_input("\n"))

   
ftmod=[]
for fc in ffound:
   for els in fc:
      if els[1]==labels[ich]:
         ftmod.append((els[0],els[2],els[3]))
	 
print "Current values (replica) are:\n"
lno=""
for el in ftmod:
   lno=lno+str(el[0])+" "      

print lno

nvals= raw_input("\n Enter the new values:")
nvals=nvals+" "

nvll = re.findall(r"\S+ ",nvals)
if len(nvll) != len(ftmod):
   raise IOError("You did not insert the same number of elements")

for newval,cf in zip(nvll,ftmod):
   lstf=cf[2]
   fname=fhands[cf[1]][1]
   dimlab=labels[ich]
   fo = open(fname,"w+")
   rlineid = ".*("+str(dimlab)+r":|LABEL="+str(dimlab)+r").*"   
   rx=re.compile(rlineid)
   
   for ln in lstf:
      if not rx.match(ln) is None:
         reg=r"\b"+str(key)+r"=\S+ "
         repl=str(key)+"="+str(newval)	 
         ln=re.sub(reg,repl,ln)
   
      fo.write(ln+"\n")
	 

