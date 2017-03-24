import basic_parsing_tools as parser
import basic_manip as manip
import write_func as wr

lf = parser.filetolist("ffbonded.itp")
sec=parser.get_section(lf,"bondtypes")

vfound = manip.find_line(sec[0],["SS","FE"])
print vfound

sec[0]=manip.remove_line(sec[0],["SS","FE"])

fh = open("prova","w+")
wr.sec_to_file(fh,sec)
