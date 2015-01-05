from tkinter import * # Import tkinter

class MainGUI():
	def left(self, event):
		self.canvas.move("ball", -5, 0)
	
	def right(self, event):
		self.canvas.move("ball", 5, 0)
	
	def down(self, event):
		self.canvas.move("ball", 0, 5)
	
	def up(self, event):
		self.canvas.move("ball", 0, -5)
	
	def __init__(self):
		window = Tk() # Create a window
		window.title("Moving Ball") # Set a title
		
		width = 200
		height = 100
		
		self.canvas = Canvas(window, bg = "white", width = width, height = height)
		self.canvas.pack()
		self.canvas.create_oval(10, 10, 30, 30, fill = "red", tags = "ball")
		self.canvas.bind("<Up>", self.up)
		self.canvas.bind("<Down>", self.down)
		self.canvas.bind("<Right>", self.right)
		self.canvas.bind("<Left>", self.left)
		self.canvas.focus_set()
		
		window.mainloop() # Create an event loop

MainGUI()
