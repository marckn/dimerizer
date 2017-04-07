"""
Modify a forcefield file and write the modified one in outdir.
  
linvolved is a list of involved line for each topology section. 
Some arbitrary matching has to be done and that's why 
kind is passed. kind is the type of forcefield file. It recognizes:
"atomtypes", "cmap", "others", the last one used also as fallback.
"""   
