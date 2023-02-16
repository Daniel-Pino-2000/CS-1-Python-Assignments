# David Pena	

'''
lab3b.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math
from math import sin, cos, pi

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

# D.1
def update(L_System, L_System_string):
	'''This function generate the next version of the L-system string by
	applying the L-system rules to each character of the string and combining
	all the strings into one big string.'''
	string_update = ''
	
	for character in L_System_string:
		if character in L_System:
			string_update += L_System[character]
		else:
			string_update +=  character		
	return string_update

# D.2	
def iterate(lsys, n):
	'''This function returns the string which results from starting with the starting
	string for that lsys and updating n time'''
	starting_string = lsys['start']
	
	for i in range(n):
		starting_string =update(lsys, starting_string)
	return starting_string
# D.3
def lsystemToDrawingCommands(draw, s):
	'''The function returns the list of drawing commands needed to draw the
	figure corresponding to the L-system string'''
	commands_list = []
	for character in s:
		if character in draw:
			commands_list.append(draw[character])
	return commands_list

# D.4
def nextLocation(x, y, angle, cmd):
	'''This function generates the next location and direction of the turtle after that
	drawing command has executed and returns a tuple of three values, the next x coordinate
	of the turtle, the next y coordinate and the next angle'''
	string = cmd.split()
	x_coordinate = x
	y_coordinate = y
	return_angle = angle

	if string[0] == 'F':
		x_coordinate += (cos(angle*pi/180))
		y_coordinate += (sin(angle*pi/180))

	elif string[0] == 'L':
		return_angle += int(string[1])

	elif string[0] == 'R':
		return_angle -= int(string[1])
			
	return_angle %= 360

	return x_coordinate, y_coordinate, return_angle

# D.5
def bounds(cmds):
	'''This function takes one argument: a list of commands. It computes
	the bounding coordinates of the resulting drawing. The function returns
	a tuple of the (xmin, xmax, ymin, ymax) coordinates, where each coordinates
	is a float'''
	xmin, xmax, ymin, ymax = 0.0, 0.0, 0.0, 0.0
	return_angle = 0
	x_coordinates = 0
	y_coordinates = 0


	for cmd in cmds:
		x_coordinates, y_coordinates, return_angle = nextLocation(x_coordinates, y_coordinates, return_angle, cmd)
		if x_coordinates > xmax:
			xmax = x_coordinates
		elif x_coordinates < xmin:
			xmin = x_coordinates			
		if y_coordinates > ymax:
			ymax = y_coordinates			
		elif y_coordinates < ymin:
			ymin = y_coordinates

	return xmin, xmax, ymin, ymax
# D.6
def saveDrawing(filename, bounds, cmds):
	'''This function writes the information to the file corresponding to the
	given filename by first writing the bounds information on a single line
	and then by writing drawing commands to the file one per line'''
	file = open(filename, 'w')
	
	for element in bounds:
		file.write(str(element) + ' ')
	file.write('\n')

	for cmd in cmds:
		print(cmd)
		file.write('{0}\n'.format(cmd))
	
	file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
	'''Make a series of L-system drawings.'''
	print('Making drawings for %s...' % name)
	for i in range(imin, imax):
		l = iterate(lsys, i)
		cmds = lsystemToDrawingCommands(ldraw, l)
		b = bounds(cmds)
		saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
	makeDrawings('koch', koch, koch_draw, 0, 6)
	makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
	makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
# David Pena	

'''
lab3b.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math
from math import sin, cos, pi

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

# D.1
def update(L_System, L_System_string):
	'''This function generate the next version of the L-system string by
	applying the L-system rules to each character of the string and combining
	all the strings into one big string.'''
	string_update = ''
	
	for character in L_System_string:
		if character in L_System:
			string_update += L_System[character]
		else:
			string_update +=  character		
	return string_update

# D.2	
def iterate(lsys, n):
	'''This function returns the string which results from starting with the starting
	string for that lsys and updating n time'''
	starting_string = lsys['start']
	
	for i in range(n):
		starting_string =update(lsys, starting_string)
	return starting_string
# D.3
def lsystemToDrawingCommands(draw, s):
	'''The function returns the list of drawing commands needed to draw the
	figure corresponding to the L-system string'''
	commands_list = []
	for character in s:
		if character in draw:
			commands_list.append(draw[character])
	return commands_list

# D.4
def nextLocation(x, y, angle, cmd):
	'''This function generates the next location and direction of the turtle after that
	drawing command has executed and returns a tuple of three values, the next x coordinate
	of the turtle, the next y coordinate and the next angle'''
	string = cmd.split()
	x_coordinate = x
	y_coordinate = y
	return_angle = angle

	if string[0] == 'F':
		x_coordinate += cos(angle*pi/180)
		y_coordinate += sin(angle*pi/180)

	elif string[0] == 'L':
		return_angle += int(string[1])

	elif string[0] == 'R':
		return_angle -= int(string[1])
		
	return_angle %= 360

	return x_coordinate, y_coordinate, return_angle

# D.5
def bounds(cmds):
	'''This function takes one argument: a list of commands. It computes
	the bounding coordinates of the resulting drawing. The function returns
	a tuple of the (xmin, xmax, ymin, ymax) coordinates, where each coordinates
	is a float'''
	xmin, xmax, ymin, ymax = 0.0, 0.0, 0.0, 0.0
	return_angle = 0
	x_coordinates = 0
	y_coordinates = 0

	for cmd in cmds:
		print(cmd)
		x_coordinates, y_coordinates, return_angle = nextLocation(x_coordinates, y_coordinates, return_angle, cmd)
		if x_coordinates > xmax:
			xmax = x_coordinates
		elif x_coordinates < xmin:
			xmin = x_coordinates
		if y_coordinates > ymax:
			ymax = y_coordinates
		elif y_coordinates < ymin:
			ymin = y_coordinates

	return xmin, xmax, ymin, ymax
# D.6
def saveDrawing(filename, bounds, cmds):
	'''This function writes the information to the file corresponding to the
	given filename by first writing the bounds information on a single line
	and then by writing drawing commands to the file one per line'''
	file = open(filename, 'w')
	
	for element in bounds:
		file.write(str(element) + ' ')
	file.write('\n')

	for cmd in cmds:
		print(cmd)
		file.write('{0}\n'.format(cmd))
	
	file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
	'''Make a series of L-system drawings.'''
	print('Making drawings for %s...' % name)
	for i in range(imin, imax):
		l = iterate(lsys, i)
		cmds = lsystemToDrawingCommands(ldraw, l)
		b = bounds(cmds)
		saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
	makeDrawings('koch', koch, koch_draw, 0, 6)
	makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
	makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
