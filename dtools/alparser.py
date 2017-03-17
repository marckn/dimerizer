def atomlist_parser(setlist):
   """
   Parse setlist and returns a list of non-repeated atom indices.
   
   setlist is in the form number-number,...,number-number representing 
   some intervals. Each of these number is stored in a list and repetitions 
   are removed.
   
   """
   
   sints= setlist.split(",")
   al=[]
   for el in sints:
      intrv= el.split("-")
      if len(intrv) == 1:
         al = al + [int(intrv[0])-1]
      else:
         al = al + range(int(intrv[0])-1,int(intrv[1]))
      
      	 
   nonrep = set(al)
   
   return sorted(list(nonrep))      
	 
   
