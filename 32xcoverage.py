#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

input_data = []

for i in sys.argv[1:]:
	input_data.append(int(i))

genomesize = input_data[0] # genome size variable = first input of command line
readnum = input_data[1] # read number variable = second input of command line
readlen = input_data[2] # read length variable = third input of command line

coverage = [] # defining an empty list to determine genome coverage
for i in range(genomesize): # filling that empty list with the length of the genome
	coverage.append(0)

for i in range(readnum):
	r = random.randint(0, genomesize - readlen) # have to subtract the read length bc...
	# it will give you an error (because you run off the edge if you random number...
	# is generate toward the end of the genome length)
	for j in range(readlen):
		coverage[r + j] = coverage[r + j] + 1 # this defines a read as adding 1 to the...
		# position at r + i (which is the random position in the genome generated plus...
		# the readlen in order to hit all of the positions for the read length)

total = sum(coverage[readlen:-readlen])	
print(min(coverage[readlen:-readlen]), max(coverage[readlen:-readlen]), (f'{total/(genomesize - 2 * readlen):.5f}'))





'''
python3 32xcoverage.py 1000 100 100
5 20 10.82375
'''
# Done