#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods in 13text.py

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc = 0

for i in range(len(dna)):
	if   dna[i] == 'G': gc += 1 #dna[i] means dna at position i in the range
	elif dna[i] == 'C': gc += 1
fgc = gc/len(dna)
print(f'{fgc:.2f}') # f-string format (Format 3)
print('%.2f' % (fgc)) # printf-style formatting (Format 1)
print('{:.2f}'.format(fgc)) # str.format() format (Format 2)

"""
python3 21gc.py
0.42
0.42
0.42
"""
# DONE