# michael-meetings.py
# by Christine P'ng

# input: 
#	list of names as text file
#	x number of output configurations

# output: 
#	x lists of names re-ordered each time in separate text files

# algorithm:
#	1. list names in desired order (because it's an even number, pairs should be placed at even start-points)
#	2. Based on x, determine what step-size y to iterate by (in this case 2) -- add extra lists as necessary
#	3. Generate x lists, step through start-point by y
#	4. Randomize order of x lists

#!/bin/python3
import random

def michaelmeetings( classlist, numberoflists ):

	# set up name list
	with open(classlist) as f:
		names = f.readlines()
		
	names = [x.strip('\n') for x in names]
	
	# calculate step size
	stepsize = round(len(names)/numberoflists)
	startpoints = list(range(0, len(names), stepsize))
	
	random.shuffle(startpoints)

	# if there are fewer startpoints selected than numberoflists, add additional ones
	if (len(startpoints) < numberoflists):
		missingcount = numberoflists - len(startpoints)
		while (missingcount > 0):
			# randomly select even number
			additionalstart = random.randrange(0, len(startpoints) + 1, 2) 
			missingcount -= 1
			startpoints.append(additionalstart)
			additionalstart = additionalstart + stepsize

	# generate ordered lists & output
	weekcount = 1 

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

# add test cases

