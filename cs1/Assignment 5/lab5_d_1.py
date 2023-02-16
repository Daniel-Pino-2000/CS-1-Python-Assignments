from tkinter import *
from random import *

# Graphics commands.

#<your code goes here>

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global current_color
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        current_color = random_color()
    elif event.keysym == 'x':
        delete_circles()
        circles_list = []
        

def button_handler(event):
    '''Handle left mouse button click events.'''
    global circles_list
    circle = draw_a_circle(event.x, event.y)
    circles_list.append(circle)

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

def random_color():
    '''The function will generate random color values in the format
    recognized by the Tkinter graphics package.'''
    sequence = 'abcdef0123456789'
    color = '#'

    for i in range(6):
        color += choice(sequence)

    return color

def draw_a_circle(x, y):
    '''This function draws a circle. The arguments are the coordinates where
    the user clicked.'''
    global current_color
    diameter = random_size(10, 50)
    return canvas.create_oval(x - diameter/2, y - diameter/2, x + diameter/2, \
                              y + diameter/2, fill = current_color, outline = current_color)

def delete_circles():
    '''This function clears all circles from the screen.'''
    global circles_list
    for circle in circles_list:
        canvas.delete(circle)
    


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    current_color = random_color()
    circles_list = []

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
