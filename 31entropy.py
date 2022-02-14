#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

# code to input data into the command line

data = []
for i in sys.argv[1:]:
	data.append(float(i))

H = 0 # creating an empty variable to add values to calculate entropy

for i in data: # loop for each value in data (in the command line)
	H += i*(math.log2(i)) #add each value
	
print(f'{-H:.3f}') # print -H because entropy equation is -sum

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
# DONE