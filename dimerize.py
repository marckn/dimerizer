import argparse


parser = argparse.ArgumentParser(description= """
From a standard Gromacs input obtain a Dimer set-up
""")

parser.add_argument('N',type=int, help='Number of atoms IN THE PROTEIN(S)')
requiredNamed = parser.add_argument_group('mandatory arguments:')
requiredNamed.add_argument('-c','--config',type=str, help='PDB file',required=True)
requiredNamed.add_argument('-p','--topology',type=str,help='Topology file',required=True)

parser.add_argument('-nvs','--novsites',help='Don\'t build the classical replica (and no virtual sites as well)', \
                     nargs='?', default=False)
		     
parser.add_argument('-pl','--plumed',type=float, nargs='+', help='Dimer strenghts for each replica')
parser.add_argument('-o','--outdir',help='Output directory (default .)', default='.')
parser.add_argument('-q','--q',help='Dimer spring power law (default 0.5)',type=float,default=0.5)
parser.add_argument('-t','--temperature',help='Temperature of the simulation (default 300K)',type=float,default=300)
parser.add_argument('-m','--mdp',help='Gromacs mdp file',type=str)
parser.add_argument('-d','--dimers',help='List of atoms to dimerize (numbers from 1 to N)',type=str,default="All")

args = parser.parse_args()



natoms  = args.N
pdbfile = args.config
topfile = args.topology
q = args.q
temp = args.temperature
mdpfile = args.mdp
if args.novsites is False:
   vsites    = True
else:
   vsites = False

dimsigmas = args.plumed
outdir    = args.outdir
outdir = outdir+"/"
atomlist=args.dimers
if atomlist == "All":
   atomlist="1-"+str(natoms)
   
from dtools.alparser import atomlist_parser as alp
atomlist=alp(atomlist)

if len(atomlist)>natoms:
   raise("Number of elements in atomlist larger than N")

# Arguments read. Building dimerized pdb.
import dtools.pdb.pdb_read
import dtools.pdb.pdb_write
pdbout = outdir+"dconfig.pdb"
ppdb = dtools.pdb.pdb_read.parse_pdb(pdbfile)
pdbf = dtools.pdb.pdb_write.dimerizer(ppdb,pdbout,atomlist,natoms)
pdbf.buildConfig(vsites)
totatoms=pdbf.totatoms
if len(atomlist)==totatoms:
   allatoms=True
else:
   allatoms=False
   
# Building topology file(s)
import dtools.topology.topol_read
import dtools.topology.topol_write
topout = outdir+"dtopology.top"
ptop = dtools.topology.topol_read.parse_topol(topfile)
ftop = dtools.topology.topol_write.dimerizer(ptop,natoms,atomlist,topout)
if vsites:
   ftop.buildClassical()
   ftop.buildDimer(1)
else:
   ftop.buildDimer(virtualsites=False)

# Building index file(s)
import dtools.index.index_write

if vsites:
   dtools.index.index_write.writeClassical(outdir,natoms,totatoms,atomlist)
   dtools.index.index_write.writeDimer(outdir,natoms,totatoms,atomlist)
else:
   dtools.index.index_write.writeNoVsites(outdir,natoms,totatoms,atomlist)


# Building plumed file(s)
if not dimsigmas is None:
   import dtools.plumed.templates
   dtools.plumed.templates.write(dimsigmas,natoms,atomlist,outdir,vsites,allatoms,q,temp)
   
if not mdpfile is None:
   import dtools.mdp.editor
   nondimer = not allatoms or len(atomlist) < natoms
   dtools.mdp.editor.editfile(mdpfile,outdir,vsites,nondimer)
