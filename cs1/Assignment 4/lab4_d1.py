# D.1

from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x700')
    canvas = Canvas(root, width=800, height=700)
    canvas.pack()
    red_rectangle = canvas.create_rectangle(0, 0, 100, 100, 
                                            fill = 'red', outline ='red')
    
    green_rectangle = canvas.create_rectangle(700, 0, 800, 100,
                                              fill = 'green', outline= 'green')
    
    blue_rectangle = canvas.create_rectangle(0, 600, 100, 700,
                                             fill = 'blue', outline= 'blue')    
    
    yellow_rectangle = canvas.create_rectangle(700, 600, 800, 700,
                                              fill = 'yellow', outline= 'yellow')  
        
    root.mainloop()