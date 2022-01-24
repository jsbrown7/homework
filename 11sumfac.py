#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
x = 0 # this will be my running sum
f = 1 # this will be my factorial
q = 100

# your code goes here

for i in range(1,n+1):
	x += i
	f *= i
print(i, x, f, q)


"""
python3 11sumfac.py
5 15 120
"""
