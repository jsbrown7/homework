#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


with open(sys.argv[1], 'r') as fp:
	foundori = False # creating a flag 
	seq = '' # empty variable to grow sequence
	for line in fp.readlines():
		line = line.rstrip()
		if 'ORIGIN' in line:
			foundori = True
			continue # means "go to the next line"
		if foundori: 
			parts = line.split()
			for i in range(1,len(parts)):
				seq += parts[i]

prev = 0
for match in re.finditer(sys.argv[2], seq):
	fraglength = match.start() - prev
	print(fraglength)
	prev = match.start()
		
	

"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
#DONE