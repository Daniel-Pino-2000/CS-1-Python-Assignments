#coding:utf-8

# B.1
def list_reverse(list):
	'''This function takes as input a list and returns the reverse 
	of the list without changing the original list'''
	list2 = list.copy()
	list2.reverse()
	return list2

# B.2	
def list_reverse2(input_list):
	'''This function takes as input a list and returns the reverse of the list without 
	changing the original list. The function uses the 'range' function and a 'for' loop
	but not the 'reverse' method of lists'''	
	list2 = []
	max_list = len(input_list) - 1
	for index in range(max_list, -1, -1):
		list2.append(input_list[index])
	return list2

# B.3
def file_info(file_name):
	'''This function takes as input a string representing the name of a text file
	and returns the number of lines, words and characters in the file as a tuple'''
	file = open(file_name, 'r')
	lines = 0
	words = 0
	characters = 0
	line = file.readline()
	while line != '':
		lines += 1
		characters += len(line)
		words += len(line.split())
		line = file.readline()
	file.close()
	return lines, words, characters

# B.4
def file_info2(file_name):
	'''This function takes as input a string representing the name of a text file
	and returns a dictionary containing the line count, word count and character count
	using the keys 'lines', 'words', 'characters'.'''	
	Info = {}
	Info['lines'], Info['words'], Info['characters'] = file_info(file_name)
	return Info
	
# B.5
def longest_line(file_name):
	'''The input of the function is the name of a text file and returns
	the length of the longest line of the file as well as the line itself'''
	file = open(file_name, 'r')
	line = file.readline()
	candidate = line
	len_candidate = len(candidate)
	while line != '':
		if len(line) > len_candidate:
			candidate = line
			len_candidate = len(candidate)
		line = file.readline()
	file.close()
	return len(candidate), candidate
				
# B.6
def sort_words(words):
	'''This function takes a string as argument, uses the 'split' method on the string and return a
	sorted list of words'''
	string = words.split()
	string.sort()
	return string
	
# B.7 
# * Primo aqui no dijiste como se evalua.
print(0b11011010)

# The largest eight-digit binary number is '0b11111111'

# C.2.1

# The code should has a single space on either side for the arithmetic 
# operators. The function needs a better name and the argument should has a space
# after each comma.

def sum_of_cubes(a, b, c):
	return a * a * a + b * b * b + c *c * c
	
# C.2.2

# Can�t see the boundaries of the function�s name . Between the comment sign and the
# first word should be a space, the comment isn�t correctly spelled and the last line
# is too long.

def sum_of_cubes(argumentA, argumentB, argumentC, argumentD):
	# return sum of cubes of argumentA, argumentB, argumentC and argumentD
	return argumentA * argumentA * argumentA \
	       + argumentB * argumentB *argumentB \
	       + argumentC * argumentC * argumentC \
	       + argumentD * argumentD * argumentD

# C.2.3

# The identation levels should be consistent and the functions must be separate
# by a blank line.

# 2 different kinds of style mistakes:
def sum_of_squares(x, y):
	return x * x + y * y

def sum_of_three_cubes(x, y, z):
	return x * x * x + y * y * y + z * z * z



