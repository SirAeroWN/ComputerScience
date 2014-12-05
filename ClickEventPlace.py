from tkinter import *

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Event Demo") # Set a title
        canvas = Canvas(window, bg = "white", width = 200, height = 200)
        canvas.pack()

        #make the circle
        canvas.create_oval(50, 50, 150, 150, fill = 'blue')
        self.radius = 50
        
        # Bind with <Button-1> event
        canvas.bind("<Button-1>", self.processMouseEvent)
        
        window.mainloop() # Create an event loop

    def processMouseEvent(self, event):
        if self.isInside(100, 100, event.x, event.y):
            print("You clicked inside the circle")
        else:
            print("You clicked outside the circle")
    
    def isInside(self, rootX, rootY, x, y):
        return self.distance(rootX, rootY, x, y) <= self.radius

    def distance(self, x1, y1, x2, y2):
        return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

MouseKeyEventDemo() # Create GUI