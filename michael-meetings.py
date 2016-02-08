# michael-meetings.py
# by Christine P'ng

# input: 
#	list of names as text file
#	x number of output configurations

# output: 
#	x lists of names re-ordered each time in separate text files

# notes:
#	if pairs of people should kept together, list them in the same line in the text file input 
#	(to be modeled as a single person)

# algorithm:
#	1. randomize names
#	2. Based on x, determine what step-size y to iterate by
#	3. Generate x lists, step through start-point by y
#	4. Randomize order of x lists

#!/bin/python3
import random

def michaelmeetings( classlist, numberoflists ):

	# set up name list
	with open(classlist) as f:
		names = f.readlines()
		
	names = [x.strip('\n') for x in names]
	random.shuffle(names)

	# calculate step size (
	### this could be thrown off if there are many pairs
	stepsize = round(len(names)/numberoflists)
	startpoints = list(range(0, len(names), stepsize))
	
	# if there are fewer startpoints selected than numberoflists, add additional ones
	### this fix is sloppy -- wouldn't work well in more extreme cases
	if (len(startpoints) < numberoflists):
		missingcount = numberoflists - len(startpoints)
		while (missingcount > 0):
			additionalstart = 1 # chose this because the first start is 0, so if stepsize > 1, this is a unique start
			missingcount -= 1
			startpoints.append(additionalstart)
			additionalstart = additionalstart + stepsize
	
	random.shuffle(startpoints)

	# generate ordered lists & output
	weekcount = 1 # the number of startpoints should equal the numberoflists

	for start in startpoints:
		filename = "week" + str(weekcount) + "-name-list.txt"
		output = open(filename, 'w')

		# iterate through list
		position = start

		for i in range(0, len(names)):
			currentname = names[position]
			output.write(currentname + '\n')
			position += 1

			if position == len(names):
				position = 0

		output.close()
		weekcount += 1

	return

# function call
michaelmeetings("class-list.txt", 9)

# test cases
