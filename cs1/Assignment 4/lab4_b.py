from random import *

# B.1
def random_size(lower_int, upper_int):
	'''This function takes two arguments and both must be non-negative even 
	integers where the first argument must be smaller than the second, and returns
	a random even integrer which is between the lower number and the upper number.'''
	assert lower_int >= 0 and upper_int > 0
	assert lower_int % 2 == 0 and upper_int % 2 == 0
	assert lower_int < upper_int

	# * You don't need a loop to solve this problem. 
	#   Hint divide and multiply by 2.
	while True:
		random_number = randint(lower_int, upper_int)
		if random_number % 2 == 0:
			break

	assert random_number % 2 == 0
	return random_number	
	
# B.2
def random_position(max_x, max_y):
	'''This function takes as its arguments two integers and both are >= 0.
	It will return a random (x, y) pair, with both x >= 0 and y >= 0
	and with x <= max_x and y <= max_y.'''
	assert max_x >= 0 and max_y >= 0
	
	random_x = randint(0, max_x)
	random_y = randint(0, max_y)
	
	return random_x, random_y

# B.3
def random_color():
	'''The function will generate random color values in the format
	recognized by the Tkinter graphics package.'''
	sequence = 'abcdef0123456789'
	color = '#'
	
	for i in range(6):
		color += choice(sequence)
		
	return color
		
	
	
# B.4
# * Make Dictionary lowercase
def count_values(dictionary):
	'''The function takes a single dictionary as an argument and returns
	a count of the number of distinct values it contains.'''
	values = []
	count = 0
	
	for key in dictionary:
		if dictionary[key] not in values:
			values.append(dictionary[key])
			count += 1
	# * You can just return len(values_seen) here
	return count

# B.5
def remove_value(Dictionary, remove_value):
	'''Takes a dictionary and an arbritary item which could be
	a value in the dictionary. It removes all key/value pairs from
	the dictionary which have that value.'''
	keys = []
	
	for key in Dictionary:
		if Dictionary[key] == remove_value:
			keys.append(key)
	for key in keys:
		del Dictionary[key]

# B.6
def split_dict(Dictionary):
	'''This function takes as its argument a dictionary which uses strings 
	as keys and returns a tuple of two dictionaries whose key/value pairs 
	are from the original dictionary: the keys that start with the letters
	'a-m' and the keys that start with the letters 'n-z'.'''
	# * Make lowercase
	Dictionary1 = {}
	Dictionary2 = {}

	for key in Dictionary:
		# * Use key.upper so that you don't have to write the lowecase part
		if key[0] >= 'A' and key[0] < 'N' or key[0] >= 'a' and key[0] < 'n':
			Dictionary1[key] = Dictionary[key]
		elif key[0] >= 'N' and key[0] <= 'Z' or key[0] >= 'a' and key[0] < 'z':
			Dictionary2[key] = Dictionary[key]

	return Dictionary1, Dictionary2
# B.7
def count_duplicates(Dictionary):
	'''The function takes a dictionary as an  argument and returns the
	number of values that appear two or more times.'''
	values = []
	values_repeated = []
	count = 0

	for key in Dictionary:
		if Dictionary[key] not in values:
			values.append(Dictionary[key])
		else:
			if Dictionary[key] not in values_repeated:
				values_repeated.append(Dictionary[key])
				count += 1
	# * You can also just return len(values_repeated) here.
	return count	
