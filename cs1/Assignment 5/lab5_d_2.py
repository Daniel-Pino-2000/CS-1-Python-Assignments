from tkinter import *
from random import *
from math import *

# Graphics commands.

def draw_line(starting_location, ending_location, color):
    global current_color, canvas
    return canvas.create_line(starting_location[0], starting_location[1], ending_location[0], \
                              ending_location[1], fill = color, width = 3)


def draw_start(x, y):
    global N, lines_list, current_color
    radius = random_size(50, 101)
    points = []
    angle = pi/2
    
    for i in range(N):
        points.append((x + radius * cos(-angle), y + radius * sin(-angle)))
        angle += 2 * pi/N
        
    farther_point = (N-1)//2
    
    for i in range(N):
        # * Remove this print
        print(farther_point)
        lines_list.append(draw_line((points[i][0], points[i][1]), (points[farther_point][0], points[farther_point][1]), \
                                    current_color))
        farther_point += 1
        if farther_point >= N:
            farther_point = 0
            
                                    
def random_color():
    '''The function will generate random color values in the format
    recognized by the Tkinter graphics package.'''
    sequence = 'abcdef0123456789'
    color = '#'

    for i in range(6):
        color += choice(sequence)

    return color

def random_size(lower_int, upper_int):
    '''This function takes two arguments and both must be non-negative even 
    integers where the first argument must be smaller than the second, and returns
    a random even integrer which is between the lower number and the upper number.'''
    assert lower_int >= 0 and upper_int > 0
    assert lower_int < upper_int

    while True:
        random_number = randint(lower_int, upper_int)
        if random_number % 2 == 0:
            break

    assert random_number % 2 == 0
    return random_number


def delete_lines():
    '''This function clears all circles from the screen.'''
    global lines_list
    for line in lines_list:
        canvas.delete(line)

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global current_color, N
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        current_color = random_color()
    elif event.keysym == 'x':
        delete_lines()
        lines_list = []
    elif event.keysym == 'plus':
        N += 2
        print(N)
    elif event.keysym == 'minus':
        if N != 5:
            N -= 2
            print(N)

def button_handler(event):
    '''Handle left mouse button click events.'''
    draw_start(event.x, event.y)




if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    current_color = random_color()
    lines_list = []
    N = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
