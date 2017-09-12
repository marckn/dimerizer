def sec_to_file(fhand,secdata):
   """
   Write a section to a file.
   
   secdata is the section content as returned from get_section(). 
   It can be a list.
   """
   
   if not isinstance(secdata,list):
      secdata=[secdata]
      
   for dd in secdata:
      fhand.write("[ "+dd[0]+" ]\n")
      for ln in dd[1]:
         fhand.write(ln+"\n")
	 
   
