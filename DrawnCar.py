from tkinter import *

class Car:
	def __init__(self):
		self.window = Tk()
		self.window.geometry("320x160")
		self.canvas = Canvas(self.window, bg = "white", width = 320, height = 160)
		self.canvas.pack()

		#rectangle (x1,y1, x2,y2) where 1 is top left and 2 is bottom right
		self.x1 = 100
		self.y1 = 100
		self.x2 = self.x1 + 40
		self.y2 = self.y1 + 20
		self.cabX1 = self.x1 + 10
		self.cabY1 = self.y1 - 10
		self.cabX2 = self.cabX1 + 20
		self.cabY2 = self.cabY1 + 10
		self.wheelX1 = self.cabX1 - 5
		self.wheelX2 = self.cabX2 - 15
		self.wheelY1 = self.cabY1 + 30
		self.wheelY2 = self.cabY1 + 40
		self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = 'red', tags = 'body')
		self.canvas.create_rectangle(self.cabX1, self.cabY1, self.cabX2, self.cabY2, fill = 'red', tags = 'body')
		self.canvas.create_oval(self.wheelX1, self.wheelY1, self.wheelX2, self.wheelY2, fill = 'black', tags = "body")
		self.canvas.create_oval(self.wheelX1 + 20, self.wheelY1, self.wheelX2 + 20, self.wheelY2, fill = 'black', tags = "body")

		self.canvas.bind("<Button-1>", self.left)
		self.canvas.bind("<Button-3>", self.right)
		self.window.mainloop()
		return

	def left(self, event):
		self.canvas.move('body', -5, 0)
		return

	def right(self, event):
		self.canvas.move('body', 5, 0)
		return
Car()