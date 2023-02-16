# David Pena
# Part D
import random
# D.1
def make_random_code():
	'''Takes no arguments and returns a string of 4 characters, one of 'R', 
	'G', 'B', 'Y', 'O', or 'W'.'''
	string = ''
	# * options not opcions :)
	random_opcions = 'R', 'G', 'B', 'Y', 'O', 'W'
	for i in range(4):
		string += random.choice(random_opcions)
	return string

# D.2
def count_exact_matches(Computer_Colors, User_Colors):
	'''Takes two strings with four colors each and returns how many of the colors
	match. The colors must be in the same place to match'''
	matches = 0
	for index, letter in enumerate(Computer_Colors):
		if letter == User_Colors[index]:
			matches += 1
	return matches

# D.3
def count_letter_matches(Computer_Colors, User_Colors):
	'''Takes two strings with four colors each and returns how many of the colors
	match. The colors do not need to be in the same place to match'''
	Computer_List = list(Computer_Colors)
	User_List = list(User_Colors)
	matches = 0
	
	for index, letter in enumerate(Computer_List):
		if letter in User_List:
			matches += 1
			User_List.remove(letter)
	return matches

# D.4 
def compare_codes (Code, Guess):
	'''Takes two arguments: the Code chosen by the codemaker and the Guess made
	by the user'''
	black_pegs = count_exact_matches(Code, Guess)
	white_pegs = count_letter_matches(Code, Guess) - black_pegs
	blank_pegs = 4 - (black_pegs + white_pegs)
	
	# * You can simplify this all into one line.
	#   Hint: use multiplication for these numbers with strings
	Pegs_List = [black_pegs, white_pegs, blank_pegs]
	string = ''
	for index, number in enumerate(Pegs_List):
		if index == 0:
			string += 'b' * number
		elif index == 1:
			string += 'w' * number
		else:
			string += '-' * number
	return string

# D.5
def run_game ():
	'''Runs the game of Mastermind using the other functions written.'''
	print('New game.')
	
	secret_code = make_random_code()
	moves = 0
	
	while True:
		user_guess = input('Enter your guess: ')
		moves += 1
		result = compare_codes(secret_code, user_guess)
		print('Result: %s' % result)
		if result == 'bbbb':
			print('Congratulations! You cracked the code in %d moves!' % moves)
			break

# * You're missing `if __name__ == '__main__':` here which causes run_game to be
#   called when I try to run the tests. Try changing the code as before and 
#   running "lab2b_tests.py", you'll see that the game starts when we actually
#   want to run the tests!
if __name__ == '__main__':
	run_game()
		