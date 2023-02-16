# D.2

from tkinter import *

def draw_square(canvas, color, size, center):
    '''This function draws a square and also returns the square that was drawn.
    The argument 'canvas' is the canvas on which the square will be drawn, 'color' 
    is the color of the square, 'size' is the width and height of the square and
    'center' is the position of the center of the square represented as a tuple of
    two integers, the horizontal and vertical position of the center in pixels.'''
    
    
    square = canvas.create_rectangle(center[0]-size/2, center[1]-size/2, 
                                     center[0]+size/2, center[1]+size/2,
                                     fill=color, outline=color)
    return square

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x700')
    canvas = Canvas(root, width=800, height=700)
    canvas.pack()
    
    draw_square(canvas, 'red', 100, (50, 50))
    draw_square(canvas, 'green', 100, (750, 50))
    draw_square(canvas, 'yellow', 100, (750, 650))
    draw_square(canvas, 'blue', 100, (50, 650))
    root.mainloop()