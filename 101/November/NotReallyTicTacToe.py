from tkinter import *
import random

class phony:
	def __init__(self):
		self.window = Tk()
		self.window.geometry("125x135")
		self.X = PhotoImage(file = "image/x.gif")
		self.O = PhotoImage(file = "image/o.gif")
		for i in range(0,3):
			for j in range(0,3):
				self.rando = random.randint(0,1)
				if self.rando == 0:
					Label(self.window, image = self.X).grid(row = i, column = j)
				else:
					Label(self.window, image = self.O).grid(row = i, column = j)
		self.window.mainloop()
phony()