from tkinter import *

class Card:
	def __init__(self, imageFile, imageNum, nameTag, place):
		self.image = PhotoImage(file = imageFile)
		self.name = nameTag
		self.selected = False
		self.num = imageNum
		self.back = PhotoImage(file = 'image/card/b1fv.gif')
		self.button = Button(place, image = self.back, command = self.flip)
		return

	def flip(self):
		

class LeGame:
	def __init__(self):
		self.window = Tk()
		self.window.title = 'Concentration'

		self.frame = Frame(self.window)
		self.frame.pack()

		self.picNum = 0
		self.misses = 0
		self.matches = 0
		self.selected = 0

		self.pup1 = PhotoImage(file = 'image/puppy1.gif') #
		self.pup2 = PhotoImage(file = 'image/puppy2.gif')
		self.pup3 = PhotoImage(file = 'image/puppy3.gif')
		self.pup4 = PhotoImage(file = 'image/puppy4.gif')
		self.pup5 = PhotoImage(file = 'image/puppy5.gif')
		self.pup6 = PhotoImage(file = 'image/puppy6.gif')
		self.pup7 = PhotoImage(file = 'image/puppy7.gif')
		self.pup8 = PhotoImage(file = 'image/puppy8.gif')

		self.setupBoard()

		self.window.mainloop()
		return

	def setupBoard(self):
		self.btn1 = Button(self.frame, image = self.pup1, state = 'active', command = self.set1)
		self.btn2 = Button(self.frame, image = self.pup2, state = 'active', command = self.set2)
		self.btn3 = Button(self.frame, image = self.pup3, state = 'active', command = self.set3)
		self.btn4 = Button(self.frame, image = self.pup4, state = 'active', command = self.set4)
		self.btn5 = Button(self.frame, image = self.pup1, state = 'active', command = self.set5)
		self.btn6 = Button(self.frame, image = self.pup5, state = 'active', command = self.set6)
		self.btn7 = Button(self.frame, image = self.pup6, state = 'active', command = self.set7)
		self.btn8 = Button(self.frame, image = self.pup7, state = 'active', command = self.set8)
		self.btn9 = Button(self.frame, image = self.pup8, state = 'active', command = self.set9)
		self.btn10 = Button(self.frame, image = self.pup4, state = 'active', command = self.set10)
		self.btn11 = Button(self.frame, image = self.pup7, state = 'active', command = self.set11)
		self.btn12 = Button(self.frame, image = self.pup8, state = 'active', command = self.set12)
		self.btn13 = Button(self.frame, image = self.pup2, state = 'active', command = self.set13)
		self.btn14 = Button(self.frame, image = self.pup6, state = 'active', command = self.set14)
		self.btn15 = Button(self.frame, image = self.pup5, state = 'active', command = self.set15)
		self.btn16 = Button(self.frame, image = self.pup3, state = 'active', command = self.set16)
		self.btn1.grid(row = 1, column = 1)
		self.btn2.grid(row = 1, column = 2)
		self.btn3.grid(row = 1, column = 3)
		self.btn4.grid(row = 1, column = 4)
		self.btn5.grid(row = 2, column = 1)
		self.btn6.grid(row = 2, column = 2)
		self.btn7.grid(row = 2, column = 3)
		self.btn8.grid(row = 2, column = 4)
		self.btn9.grid(row = 3, column = 1)
		self.btn10.grid(row = 3, column = 2)
		self.btn11.grid(row = 3, column = 3)
		self.btn12.grid(row = 3, column = 4)
		self.btn13.grid(row = 4, column = 1)
		self.btn14.grid(row = 4, column = 2)
		self.btn15.grid(row = 4, column = 3)
		self.btn16.grid(row = 4, column = 4)
		return

	def checkMatch(self, otherNum):
		if self.picNum == otherNum:
			match = True
			self.matches += 1
		else:
			match = False
			self.misses += 1
		return match


	def set1(self):
		if self.selected == 0:
			self.selected = 1
			self.btn1["state"] = "disabled"
			self.picNum = 1
		else:
			self.selected = 0
			if(self.checkMatch(1)):
				self.btn1["state"] = "disabled"
		return

	def set2(self):
		if self.selected == 0:
			self.selected += 1
			self.btn2["state"] = "disabled"
			self.picNum = 2
		else:
			self.selected -= 1
			if(self.checkMatch(2)):
				self.btn2["state"] = "disabled"
		return

	def set3(self):
		if self.selected == 0:
			self.selected += 1
			self.btn3["state"] = "disabled"
			self.picNum = 3
		else:
			self.selected -= 1
			if(self.checkMatch(3)):
				self.btn3["state"] = "disabled"
		return

	def set4(self):
		if self.selected == 0:
			self.selected += 1
			self.btn4["state"] = "disabled"
			self.picNum = 4
		else:
			self.selected -= 1
			if(self.checkMatch(4)):
				self.btn4["state"] = "disabled"
		return

	def set5(self):
		if self.selected == 0:
			self.selected += 1
			self.btn5["state"] = "disabled"
			self.picNum = 5
		else:
			self.selected -= 1
			if(self.checkMatch(5)):
				self.btn5["state"] = "disabled"
		return

	def set6(self):
		if self.selected == 0:
			self.selected += 1
			self.btn6["state"] = "disabled"
			self.picNum = 6
		else:
			self.selected -= 1
			if(self.checkMatch(6)):
				self.btn6["state"] = "disabled"
		return

	def set7(self):
		if self.selected == 0:
			self.selected += 1
			self.btn7["state"] = "disabled"
			self.picNum = 7
		else:
			self.selected -= 1
			if(self.checkMatch(7)):
				self.btn7["state"] = "disabled"
		return

	def set8(self):
		if self.selected == 0:
			self.selected += 1
			self.btn8["state"] = "disabled"
			self.picNum = 8
		else:
			self.selected -= 1
			if(self.checkMatch(8)):
				self.btn8["state"] = "disabled"
		return

	def set9(self):
		if self.selected == 0:
			self.selected += 1
			self.btn9["state"] = "disabled"
			self.picNum = 9
		else:
			self.selected -= 1
			if(self.checkMatch(9)):
				self.btn9["state"] = "disabled"
		return

	def set10(self):
		if self.selected == 0:
			self.selected += 1
			self.btn10["state"] = "disabled"
			self.picNum = 10
		else:
			self.selected -= 1
			if(self.checkMatch(10)):
				self.btn10["state"] = "disabled"
		return

	def set11(self):
		if self.selected == 0:
			self.selected += 1
			self.btn11["state"] = "disabled"
			self.picNum = 11
		else:
			self.selected -= 1
			if(self.checkMatch(11)):
				self.btn11["state"] = "disabled"
		return

	def set12(self):
		if self.selected == 0:
			self.selected += 1
			self.btn12["state"] = "disabled"
			self.picNum = 12
		else:
			self.selected -= 1
			if(self.checkMatch(12)):
				self.btn12["state"] = "disabled"
		return

	def set13(self):
		if self.selected == 0:
			self.selected += 1
			self.btn13["state"] = "disabled"
			self.picNum = 13
		else:
			self.selected -= 1
			if(self.checkMatch(13)):
				self.btn13["state"] = "disabled"
		return

	def set14(self):
		if self.selected == 0:
			self.selected += 1
			self.btn14["state"] = "disabled"
			self.picNum = 14
		else:
			self.selected -= 1
			if(self.checkMatch(14)):
				self.btn14["state"] = "disabled"
		return

	def set15(self):
		if self.selected == 0:
			self.selected += 1
			self.btn15["state"] = "disabled"
			self.picNum = 15
		else:
			self.selected -= 1
			if(self.checkMatch(15)):
				self.btn15["state"] = "disabled"
		return

	def set16(self):
		if self.selected == 0:
			self.selected += 1
			self.btn16["state"] = "disabled"
			self.picNum = 16
		else:
			self.selected -= 1
			if(self.checkMatch(16)):
				self.btn16["state"] = "disabled"
		return

LeGame()