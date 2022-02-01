#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
anti = ""

for i in range(len(dna)):
	if   dna[i] == 'A': anti += 'T'
	elif dna[i] == 'T': anti += 'A'
	elif dna[i] == 'C': anti += 'G'
	else:               anti += 'C'
print(anti[::-1]) #the [::-1] -> :: means implicitly that the beginning is the beginning
# and that you go backwards (-1)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
#Done