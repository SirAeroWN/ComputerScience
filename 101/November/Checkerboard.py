from tkinter import *

class Board:
	def __init__(self):
		self.window = Tk()
		self.window.geometry("195x195")
		self.size = 160

		for i in range(0,8):
			for j in range(0,8):
				if(i + j) % 2 == 0:
					self.canvas = Canvas(self.window, bg = "white", width = self.size/8, height = self.size/8)
					self.canvas.grid(row = i, column = j)
				else:
					self.canvas = Canvas(self.window, bg = "black", width = self.size/8, height = self.size/8)
					self.canvas.grid(row = i, column = j)
		self.window.mainloop()
Board()