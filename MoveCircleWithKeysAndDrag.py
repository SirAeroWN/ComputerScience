from tkinter import * # Import tkinter
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    # Is point (x, y) inside this circle?
    def isInside(self, x, y):
        return distance(self.x, self.y, x, y) <= self.radius

               
class MainGUI:
    def __init__(self):   
        window = Tk() # Create a window
        window.title("Dragging The Blue Circle") # Set title

        self.canvas = Canvas(window, width = width, height = height)
        self.canvas.pack()
        
        self.c1 = Circle(x, y, radius)
        
        self.paint(self.c1, "blue", "c1")
        
        self.canvas.bind("<B1-Motion>", self.mouseMoved)

        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Right>", self.right)
        self.canvas.bind("<Left>", self.left)
        self.canvas.focus_set()
        
        window.mainloop() # Create an event loop
        
    def mouseMoved(self, event):
        if self.c1.isInside(event.x, event.y):
            self.c1.x = event.x
            self.c1.y = event.y
            
        self.canvas.delete("c1")
        self.paint(self.c1, "blue", "c1")
        return
    
    def paint(self, c, color, tags = "stable"):
        self.canvas.create_oval(c.x - c.radius, c.y - c.radius, c.x + c.radius, c.y + c.radius, fill = color, tags = tags)
        return

    def left(self, event):
        self.canvas.move("c1", -5, 0)
        return
    
    def right(self, event):
        self.canvas.move("c1", 5, 0)
        return
    
    def down(self, event):
        self.canvas.move("c1", 0, 5)
        return
    
    def up(self, event):
        self.canvas.move("c1", 0, -5)
        return

def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5    	

    
width = 400
height = 250
x = 100
y = 100
hGap = 120
vGap = 50
radius = 50

MainGUI()
