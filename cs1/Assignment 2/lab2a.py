# David Pena
# Parts B and C

import random
# B.1
def complement(DNA_string):
	'''Takes a string of a DNA sequence and returns the complement of it. So T->A,
	A->T, C->G, and G->C'''
	string_changed = ''

	for letter in DNA_string:
		if letter == 'T':
			string_changed += 'A'
		elif letter == 'G':
			string_changed += 'C'
		elif letter == 'C':
			string_changed += 'G'
		elif letter == 'A':
			string_changed += 'T'
	return string_changed	

# B.2
def list_complement(DNA_list):
	'''Takes a list of individual DNA base pairs & modifies it to its complement.
	Does not return the complement.'''
	
	for index, letter in enumerate(DNA_list):
		if letter == 'T':
			DNA_list[index] = 'A'
		elif letter == 'G':
			DNA_list[index] = 'C'
		elif letter == 'C':
			DNA_list[index] = 'G'
		elif letter == 'A':
			DNA_list[index] = 'T'		
			
# B.3
def product(List_product):
	'''Takes a list of numbers and compute the product of the entire list 
	and return it.If the list is empty returns 1.''' 
	if len(List_product) == 0:
		return 1
	else:
		product = 1
		for number in List_product:
			product *= number
		return product	
		
# B.4
def factorial(Number_factorial):
	'''Takes a number, computes its factorial, and returns it.'''
	if Number_factorial == 0:
		return 1
	else:
		number_list = []
		return product(list(range(1, Number_factorial+1)))
				
# B.5
def dice (m, n):
	'''Takes two arguments: the number of sides (m) and the number of dice rolled
	(n), and returns the sum of all the random dice values'''
	sum_values = 0
	list_values = list(range(1, m+1))
	for i in range(n):
		sum_values += random.choice(list_values)
	return sum_values
		

# B.6
def remove_all (Integers, number):
	'''Removes the specified integer from the list of integers. Takes a list of
	integers and the number you wish to remove as an argument. Modifies the list 
	directly, so it does not return anything.'''
	
	while Integers.count(number) > 0:
		Integers.remove(number)
	
# B.7
def remove_all2 (Integers, number):
	'''Removes the specified integer from the list of integers. Takes a list of
	integers and the number you wish to remove as an argument. Modifies the list 
	directly, so it does not return anything. More efficient than remove_all'''
	
	repetitions = Integers.count(number)
	for i in range(repetitions):
		Integers.remove(number)

def remove_all3 (Integers, number):
	'''Removes the specified integer from the list of integers. Takes a list of
		integers and the number you wish to remove as an argument. Modifies the list
		directly, so it does not return anything. More efficient than remove_all'''
	
	while number in Integers:
		Integers.remove(number)

# B.8
def any_in(List_1, List_2):
	'''Takes two lists as arguments and returns a True value if any of the
	elements in the first list are equal to any of the elements in the second 
	list.'''
	
	for element in List_1:
		if element in List_2:
			return True
	return False

# C.1.A
'''The problem is that the programmer used the (=) that assign to 'a' the value of 0
instead of (==) to make a comparison'''

# C.1.B
''' The argument of the function has quotes and that will provoke a syntax error'''

# C.1.C 
''' The problem is that the (s) has quotes so Python will take it like a string
and the function will return (s-Caltech)'''

# C.1.D
'''The programmer can´t concatenate list to strings so he have to use the method append instead''' 

# C.1.E
'''The reverse method doesn´t return the reversed list. It reverses the
list 'in-place' and doesn´t return anything.The programmer should assign
the value after reversing the list'''

# C.1.F
'''The programmer is adding a list of letters not the letters of the string.
The way of doing this is using a for loop.'''

# C.2
# * It actually prints 30 because c was evaluated before a was assigned, 
#   so the result of b + a was already stored.
'''Prints 30 because aliasing does not happen with numbers or strings.'''

# C.3
'''When you return a reult you get that value as the result of the called function and
when you print you don´t get the value as the result, you just print it.'''

# C.4
'''The difference is that if you get the value interactively (raw_input) the argument 
of the function must be empty'''

# C.5
# * The way you would actually say this is that "this would not work because strings
#   in python are immutable". Immutable types cannot be mutated (changed), a new type
#   must be created with the desired change. Immutable types are very important because
#   they guarantee that the state of your program won't change and gives them other
#   important properties.
'''The function won´t work because it´s assigning the value on a string object.'''

# C.6 
# * The reason why it won't work is actually because the value from item *= 2 is
#   never stored back into the list lst.
'''It won´t work  because 'item' will change its value every time that the for loop starts over.''' 