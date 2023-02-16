# D.3

from random import *
from tkinter import *
from lab4_d2 import draw_square

# * Don't paste, import from the module lab4_b
def random_size(lower_int, upper_int):
    '''This function takes two arguments and both must be non-negative even 
    integers where the first argument must be smaller than the second, and returns
    a random even integrer which is between the lower number and the upper number.'''
    assert lower_int >= 0 and upper_int > 0
    assert lower_int % 2 == 0 and upper_int % 2 == 0
    assert lower_int < upper_int

    while True:
        random_number = randint(lower_int, upper_int)
        if random_number % 2 == 0:
            break

    assert random_number % 2 == 0
    return random_number	

# * Don't paste, import from the module lab4_b
def random_position(max_x, max_y):
    '''This function takes as its arguments two integers and both are >= 0.
    It will return a random (x, y) pair, with both x >= 0 and y >= 0
    and with x <= max_x and y <= max_y.'''
    assert max_x >= 0 and max_y >= 0

    random_x = randint(0, max_x)
    random_y = randint(0, max_y)

    return random_x, random_y

# * Don't paste, import from the module lab4_b
def random_color():
    '''The function will generate random color values in the format
    recognized by the Tkinter graphics package.'''
    sequence = 'abcdef0123456789'
    color = '#'

    for i in range(6):
        color += choice(sequence)

    return color

def exit_python(event):
    '''Exit Python when the event
    'event' occurs.'''
    quit()

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x700')
    canvas = Canvas(root, width=800, height=700)
    canvas.pack()
    
    for i in range(50):
        draw_square(canvas, random_color(), random_size(20, 150), random_position(800, 700))
        
    root.bind('<q>', exit_python)
    root.mainloop()