#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

# I worked on this with Josh so our code will be the same

def score(aa):
	if   aa == 'I': return 4.5
	elif aa == 'V': return 4.2
	elif aa == 'L': return 3.8
	elif aa == 'F': return 2.8
	elif aa == 'C': return 2.5
	elif aa == 'M': return 1.9
	elif aa == 'A': return 1.8
	elif aa == 'G': return -0.4
	elif aa == 'T': return -0.7
	elif aa == 'S': return -0.8
	elif aa == 'W': return -0.9
	elif aa == 'Y': return -1.3
	elif aa == 'P': return -1.6
	elif aa == 'H': return -3.2
	elif aa == 'E': return -3.5
	elif aa == 'Q': return -3.5
	elif aa == 'D': return -3.5
	elif aa == 'N': return -3.5
	elif aa == 'K': return -3.9
	elif aa == 'R': return -4.5
	return 0
"""
def kd_hydropathy1(seq):
	kd = 0
	for aa in seq:
		if   aa == 'I': kd += 4.5
		elif aa == 'V': kd += 4.2
		elif aa == 'L': kd += 3.8
		elif aa == 'F': kd += 2.8
		elif aa == 'C': kd += 2.5
		elif aa == 'M': kd += 1.9
		elif aa == 'A': kd += 1.8
		elif aa == 'G': kd += -0.4
		elif aa == 'T': kd += -0.7
		elif aa == 'S': kd += -0.8
		elif aa == 'W': kd += -0.9
		elif aa == 'Y': kd += -1.3
		elif aa == 'P': kd += -1.6
		elif aa == 'H': kd += -3.2
		elif aa == 'E': kd += -3.5
		elif aa == 'Q': kd += -3.5
		elif aa == 'D': kd += -3.5
		elif aa == 'N': kd += -3.5
		elif aa == 'K': kd += -3.9
		elif aa == 'R': kd += -4.5
	return kd
"""	
def check_pro(seq): # code to check if there is a proline
	if 'P' in seq:
		return True
	else:
		return False
		
def kd(seq, window = 0, threshold = 0, check_alpha = False): 
	total = 0
	for i in range(window):
		total += score(seq[i])
	for pos in range(len(seq) - (window - 1)):
		if pos > 0:
			total += score(seq[pos + window - 1]) - score(seq[pos - 1])
		avg = total / window
		if avg > threshold and (check_alpha == False or check_pro(seq[pos:pos+window]) == False):
			return True
			
	return False		
		
fp = open(sys.argv[1])
assert(len(sys.argv) == 2) # says that you can only have 2 things in the command line
# will give an error message if there are not exactly 2 arguments in the command line
line = fp.readline()

while line:
	if line [0] == '>':
		name = line.split(' | ')
		protein = name[0]
		protein = protein [1:] # renames and takes off the >
				
		data = ''
		line = fp.readline()
		while line:
			data += line[0:len(line) - 1]
			if data[len(data) - 1] == '*':
				data = data[0:len(data) - 1]
				break
			line = fp.readline()
		
		condition1 = kd(data[0:30], 8, 2.5, False)
		condition2 = kd(data[30:], 11, 2.0, True)
		if condition1 == True and condition2 == True:
			print(protein)
	line = fp.readline()
fp.close()
		

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
