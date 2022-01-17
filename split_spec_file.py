# -*- coding: utf-8 -*-
"""
@author: P.Foulquier
"""

import numpy
import re

spec=['']
    
spec=open("spec_file.txt").read() #Read spec file
a=str(spec)

x = [_.start() for _ in re.finditer('#S', a)] #Locate the start of the scan name

y = [_.start() for _ in re.finditer('#D', a)] #Locate the end of the scan name

z = [_.start() for _ in re.finditer('#L', a)] #Locate the beginning of the scan data



i=0

while i<len(x)-1:
     w=open(a[x[i]:y[i]-1]+'.txt', 'w') 
     w.write(a[z[i]+2:x[i+1]-1])  #Create text file with name and type of scan
     w.close()
     i+=1
     print(i)
     
w=open(a[x[i]:y[i]-1]+'.txt', 'w') #Create the last scan file
w.write(a[z[i]+2:len(a)])
w.close()
