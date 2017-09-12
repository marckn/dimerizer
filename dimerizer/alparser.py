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
	 
   
def atomlist_backparser(lst):
   """
   Given a list of atom indices obtain a plumed shortened notation in serials notation
   """
   
   serials=sorted(lst)
   serials=map(lambda x : int(x)+1, serials)
   
   intervals=[]
   
   i0=None
   icurr=None
   for j,v in enumerate(serials):
      if j == 0:
         i0 = v
	 icurr=v
         continue
      
      if int(icurr) == int(v)-1:
         icurr=v
      else:
         intervals.append((i0,icurr))
	 i0=v
	 icurr=v

   intervals.append((i0,icurr))	 
	 
   stout=""
   for ii in intervals:
      if ii[0] == ii[1]:
         stout = stout + str(ii[0]) + ","
      else:
         stout = stout + str(ii[0])+"-"+str(ii[1])+","

   lst=list(stout)
   lst=lst[0:-1]
   stout="".join(lst)
   return stout
	 	    
   
