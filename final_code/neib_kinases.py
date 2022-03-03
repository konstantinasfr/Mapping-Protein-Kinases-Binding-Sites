#!/usr/bin/env python3
import numpy as np
import sys
import re



positions1 = []
positions1_true = []
positions1_false = []
with open(sys.argv[1],'r') as f:
    for line in f:
      j = 2
      sentence = []
      while ( "." not in line.split()[j]):
        sentence.append(line.split()[j])
        j += 1

      positions1.append(re.sub("[^0-9]", "",sentence[-1]))

positions1 = [int(i) for i in positions1]

positions1_unique = np.unique(positions1)  
#print(positions1_unique)
pocket_len1 = len(positions1_unique)
#print(pocket_len1)

#print(max(positions1)) 
max1 = max(positions1) + round(pocket_len1*0.2)
#print(min(positions1))   
min1 = max(0,min(positions1) - round(pocket_len1*0.2))
#print(max1,min1)

#-------------------------------------------------------------

positions2 = []
positions2_true = []
positions2_false = []
with open(sys.argv[2],'r') as f:
    for line in f:
      j = 2
      sentence = []
      while ( "." not in line.split()[j]):
        sentence.append(line.split()[j])
        j += 1

      positions2.append(re.sub("[^0-9]", "",sentence[-1]))

positions2 = [int(i) for i in positions2]

positions2_unique = np.unique(positions2)   
#print(positions2_unique)
pocket_len2 = len(positions2_unique)    
#print(pocket_len2)

#print(max(positions2)) 
max2 = max(positions2) + round(pocket_len2*0.2)
#print(min(positions2))   
min2 = max(0,min(positions2) - round(pocket_len2*0.2))
#print(max2,min2)

if min(max1,max2) - max(min1,min2)<0:
    overlap = 0
else:
    overlap = 1    
    
print(overlap)
#   while line:
#       print("Line {}: {}".format(cnt, line.strip()))
#       line = fp.readline()
 #      cnt += 1
       
       
       
       

