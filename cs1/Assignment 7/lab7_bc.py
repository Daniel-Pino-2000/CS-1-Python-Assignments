# Parts B & C

# B.1

def mySum(*n):
    '''This function returns the sum of an arbritary number of arguments'''
    for number in n:
        if type(number) is not int:
            raise TypeError('All the arguments must be integers')
        elif number <= 0:
            raise ValueError('All the numbers should be greater than zero')
    return sum(n)

# B.2

def myNewSum(*arg):
    '''This function will be able to take a single list of positive 
    integers as its only argument and will return the sum of 
    the list'''
    
    if len(arg) == 1:
        if type(arg[0]) is list:
            for number in arg[0]:
                if type(number) is not int:
                    raise TypeError("The list's elements must be integers")
                elif type(number) is int and number < 1:
                    raise ValueError('All the supplied numbers must be integers greater than zero')
            return sum(arg[0])
        else:
            if type(arg[0]) is not int:
                raise TypeError("All the supplied numbers must be integers greater than zero ")
            elif type(arg[0]) is int and arg[0] < 1:
                raise ValueError("All the supplied numbers must be integers greater than zero ")
            return arg[0]
        
    else:
        for element in arg:
            if type(element) is not int:
                raise TypeError('The argument must be an integer')
            elif element < 1:
                raise ValueError("All the supplied numbers must be integers greater than zero ")
        return sum(arg)
    	
# B.3

def myOpReduce(numbers, **keyword):
    '''This function does different kinds of operations depending on the value of op,
    '+' for sum, '*' for multiplication and max to return the greater number of the list'''
    commands = ['+', '*', 'max']
    result = 1
    
    if len(keyword) == 0:
        raise ValueError('You have to introduce a keyword argument')
    elif len(keyword) > 1:
        raise ValueError("You can't introduce more than one keyword argument")
    elif 'op' not in keyword or type(keyword['op']) is str and keyword['op'] not in commands:
        raise ValueError('Invalid keyword argument')
    elif type(keyword['op']) is not str:
        raise TypeError('The keyword argument must be a string')
    else:
        if keyword['op'] == '+':
            return sum(numbers)
        elif keyword['op'] == 'max':
            if numbers == []:
                return 0
            else:
                return max(numbers)
        elif keyword['op'] == '*':
            for i in numbers:
                result *= i
            return result


# C.1
# The problem is that the function doesn't specify the problem
def sum_of_key_values(dict, key1, key2):
    return dict[key1] + dict[[key2]
                             
# C.2
# You should let the keyerror happen becouse that will print the
# error message anyway
def sum_of_key_values(dict, key1, key2):
    return dict[key1] + dict[[key2]
		
# C.3
# The problem is that you don´t need the 'raise' statement becouse if
# the error happen you will have a keyerror anyway
def sum_of_key_values(dict, key1, key2):
    return dict[key1] + dict[[key2]

# C.4
# You don´t need to assign the values of key1 and key2 because if they are not
# present in the sum a keyerror will be raise.
def sum_of_key_values(dict, key1, key2):
    return dict[key1] + dict[[key2]
	
# C.5
# The problem is that the user wont be able to see the error message because the
# program will end after the ValueError is raised. The message should be with the Value
# Error instead of just be printed.
def fib(n):
    if n < 0:
        raise ValueError('n must be >= 0')
    
    elif n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# C.6
# The message should be with the ValueError instead of just be printed.
def fib(n):
    if n < 0:
        raise ValueError('n must be >= 0')
    
    elif n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# C.7
# You should raise a ValueError innstead TypeError
def exp_x_over_x(x):
    if x <= 0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
	
# C.8
# Yous should specify what kind of error happened
def exp_x_over_x(x):
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
