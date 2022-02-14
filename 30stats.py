#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

data = [] # [] defines an empty list
for i in sys.argv[1:]: #[1:] allows you to start at the second value (skip the 0th value)
	# we do this step to allow us to type into the command line
	data.append(float(i)) # float allows you to change to a number and not a string
						  # if you dont include 'float' or 'int' then it will give an...
						  # error saying that you cannot mix integers and strings
						  # because the list would be a string of values and not
						  # actual integers or numbers

# code for count (the amount of data points)

print('Count:', len(data))

# code for min and max

min = data[0] # define variable min as the beginning of the data set
max = data[0] # define variable max as the beginning of the data set
for i in data[1:]: # [1:] means to skip the 0th value and to start at 1 and go to the end
	if i < min: # if the data at position i is less than min, then assign that new...
		min = i # lesser value to min
	if i > max: # if the data at position i is more than max, then assign that new...
		max = i # higher value to max
print('Minimum:', min)
print('Maximum:', max)

# code for mean

sum = 0 # define empty variable to add to
for i in data:
	sum += i # add each value at position i in data to sum
print('Mean:', f'{sum/len(data):.3f}') # f-string format to editing so that the...
# decimal goes to 3 decimal places (or ._f where the blank can be whatever number)...
# of decimal places you want 

# code for standard deviation

stdev = 0

for i in data: 
	stdev += (i - (sum/len(data))) ** 2 # code for the sum in the equation of std dev
print('Std. dev:', f'{(stdev/len(data)) ** (1/2):.3f}')

# code for median

data.sort()

if len(data) % 2 == 1:
	print('Median:', f'{data[len(data) // 2]:.3f}')
else:
	v1 = data[len(data) // 2]
	v2 = data[len(data) // 2 - 1]
	print('Median:', (v1 + v2)/2)





"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
# DONE