#asks user for some personal info and puts that in a file, then reads it; uses a GUI

from tkinter import *

class Person:
	def __init__(self, infoString):
		info = infoString.split(',')
		self.first = info[0].strip()
		self.last = info[1].strip()
		self.color = info[2].strip()
		return

	def __str__(self):
		lestr = self.first + ' ' + self.last + '\'s favorite color is ' + self.color
		return lestr

class dumbdumb:
	def __init__(self):
		self.root = Tk()
		window = Frame(self.root)
		window.pack()
		Label(window, text = "First Name:").grid(row = 1, column = 1)
		Label(window, text = "Last Name:").grid(row = 2, column = 1)
		Label(window, text = "Favorite Color:").grid(row = 3, column = 1)
		self.First = StringVar()
		self.Last = StringVar()
		self.Color = StringVar()
		self.first = Entry(window, textvariable = self.First)
		self.first.grid(row = 1, column = 2)
		self.last = Entry(window, textvariable = self.Last)
		self.last.grid(row = 2, column = 2)
		self.color = Entry(window, textvariable = self.Color)
		self.color.grid(row = 3, column = 2)
		addBtn = Button(self.root, text = "Add", command = self.add)
		addBtn.pack()
		doneBtn = Button(self.root, text = "Done", command = self.done)
		doneBtn.pack()
		self.root.mainloop()
		return

	def add(self):
		oFile = open("people.peeps", "a")
		thing = self.First.get() + ',' + self.Last.get() + ',' + self.Color.get() + '\n'
		oFile.write(thing)
		oFile.close()
		self.First.set('')
		self.Last.set('')
		self.Color.set('')
		return

	def done(self):
		self.root.destroy()
		people = []

		iFile = open("people.peeps", "r")

		for line in iFile:
			people.append(Person(line.strip()))

		iFile.close()

		for peep in people:
			print(peep)
		return


oFile = open("people.peeps", "w")
oFile.close()
dumbdumb()