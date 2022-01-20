#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
for i in range(0, len(dna), 3):
	#print(i)
	print(dna[i:i+3])
print('End of Codons')
# your code goes here

"""
python3 10codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
