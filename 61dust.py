#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185 as mcb
import sys

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Identifying High Entropy')
# required arguments
parser.add_argument('--seqfile', required=True, type=str,
	metavar='<str>', help='required file argument')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='required window argument')
parser.add_argument('--threshold', required=True, type=float,
	metavar='<float>', help='required threshold argument')
parser.add_argument('--masking', required=True, type=str,
	metavar='<str>', help='required floating point argument')
	
args = parser.parse_args() # redefining the variable
# when I worked with Josh, he told me that this was necessary for the program...
# to function properly
for entry in mcb.read_fasta(args.seqfile):
	name = entry[0]
	seq = entry[1].upper()
	
	window = args.window # defining the parser argument window into a variable
	threshold = args.threshold # defining the parser argument threshold into a variable
	masking = args.masking # defining the parser argument masking into a variable

	new_seq = list(seq) # defining a filled list 

	for i in range(len(seq) - window + 1):
		entropy = mcb.entropy_calc(seq[i:i+window], window)
		if entropy < threshold:
			if masking.upper() == 'N':
				new_seq[i:i+window] = ['N'] * window # changing the list of the seq...
				# to N or lowercase (below) if below the threshold
			else:
				new_seq[i:i+window] = list(seq[i:i+window].lower())

	print(f">{name}\n{''.join(new_seq)}") # printed out in a fasta format






