#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

numppl = 25
calendar = 365
shared = 0
trials = 1000

for j in range(trials):
	bdays = []
	for i in range(calendar):
		bdays.append(0)
	for i in range(numppl):
		day = random.randint(0, calendar - 1)
		bdays[day] = bdays[day] + 1	
		
	collision = False # setting a flag (T/F)
	for val in bdays:
		if val > 1:
			shared += 1
			break # how to break a loop if you want to stop
print(shared / trials)

"""
print(shared / trials) # Same code using a flagged variable to break the loop

numppl = 23
calendar = 365
shared = 0
trials = 10000

for j in range(trials):
	bdays = []
	for i in range(calendar):
		bdays.append(0)
	for i in range(numppl):
		day = random.randint(0, calendar - 1)
		bdays[day] = bdays[day] + 1	
		
	collision = False # setting a flag (T/F)
	for val in bdays:
		if val > 1:
			collision = True
	if collision: # you can say if collision and not "if collision == True" because...
	# it is a boolean variable -> collision is either true or false
		shared += 1

print(shared / trials)
"""

"""
python3 33birthday.py
0.571
"""

# Done