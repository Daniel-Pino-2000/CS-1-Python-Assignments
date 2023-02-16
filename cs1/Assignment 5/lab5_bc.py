# Part B

from math import *

# B.1
class Point:
    '''This class represents a point in three-dimensional Eucalidean space and have two methods, 
    the constructor method(__init__) and the 'distanceTo' method.'''
    
    def __init__(self, x, y, z):
        ''''This method takes x,y, and z coordinates of the point and stores them in the object.'''
        self.x_coordinate = x
        self.y_coordinate = y
        self.z_coordinate = z
    
    def distanceTo(self, point):
        '''This method takes another point as its input and computes the distance between that point
        and the point being acted on.'''
        # * Split this into separate lines, you can rename the x, y, z magnitudes as
        #   m_x, m_y, m_z so that it is more readable. We would want to wrap
        #  at 80 characters per line.
        distance = sqrt((self.x_coordinate - point.x_coordinate)**2 + (self.y_coordinate - point.y_coordinate)**2\
                        + (self.z_coordinate - point.z_coordinate)**2)
        
        return distance
        
# B.2
class Triangle:
    
    def __init__(self, point1, point2, point3):
        '''This constructor method takes as arguments three Point objects'''
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    
    def area(self):
        '''This method computes the area of the area of the triangle.'''
        # Lenght of side 1
        a = self.point1.distanceTo(self.point2)
        # Lenght of side 2
        b = self.point2.distanceTo(self.point3)
        # Lenght of side 3
        c = self.point3.distanceTo(self.point1)
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    
# B.3
class Averager:
    '''This class store a list of numbers and has methods to perform various
    operations.'''
    
    def __init__(self):
        self.numbers = []
    
    def getNums(self):
        '''Returns a copy of the list of numbers stored so far.'''
        return self.numbers[:]
    
    def append(self, new_number):
        '''Appends a new number to the list.'''
        self.numbers.append(new_number)
    
    def extend(self, new_numbers):
        '''Appends a list of numbers to the existing list.'''
        # * new_numbers is already a list, we don't need to call list(new_numbers)
        new_numbers = list(new_numbers)
        self.numbers += new_numbers
    
    def limits(self):
        '''This method computes the minimum and maximum of the stored list.
        If the list is empty, returns the tuple(0, 0).'''
        if len(self.numbers) == 0:
            return (0, 0)
        return (min(self.numbers), max(self.numbers))
    
    def average(self):
        '''Computes the average of the stored list. If the list is empty, returns 0.'''
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers)/len(self.numbers)
		
		
# Part C

# C.1
# You don't need the 'else' statement.

def is_positive(x):
    # * You don't really need the `if` either, this is a common mistake in 
    #   programming, if you ever have:
    #    if <expression>:
    #       return True
    #    return False
    #   This can just be simply written as:
    #    return <expression>
    #   So in this case we can do:
    #    return x > 0
    if x > 0:
        return True
    return False
		
# C.2
# You don't need to start the variable assigning the value '-1' because it will be assign 
# with another value later and won't be use before that, also don't need the (==) sign to
# compare 'found' with 'True' because Python interpret the statement that way too. 

def find(x, lst):
    # * Location is never defined in the outer scope of the function, you also
    #   don't really need 'found' if you set location to -1 initially and just
    #   return -1 at the end.
    found = False
    for i, item in enumerate(lst):
        if item == x:
            found = True
            location = i
    if found:
        return location
    return -1
	
# C.3
# You should use 'elif' and return the string without making an assignment once the 'if' 
#  statement is True so that way the function will be faster.

def categorize(x):
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    elif x > 0 and x < 10:
        return 'small'
    return 'large'


# C.4
# If len(lst) != 0 you should use a 'for in' statement that adds to 'total' all the values of 'lst'.

def sum_list(lst):
    
    if len(lst) == 0:
        return 0
    total = 0
    for item in lst:
        total += item
    return total
