from tkinter import *
from tkinter import messagebox
import random

class Card:
	def __init__(self, used = -1):
		self.__rawImageVal = self.assignRawImageVal(used)
		self.__imageString = PhotoImage( file = "image/card/" + str(self.__rawImageVal) + ".gif")
		self.__cardVal = self.assignCardVal(self.__rawImageVal)
		return

	def getImage(self):
		return self.__imageString

	def getVal(self):
		return self.__cardVal

	def getRawImageVal(self):
		return self.__rawImageVal
	
	def assignRawImageVal(self, alreadyUsed):
		val = random.randint(1, 52)
		while val == alreadyUsed:
			val = random.randint(1, 52)
		return val

	def assignCardVal(self, rawValue):
		value = rawValue % 13
		if value == 0:
			value += 13
		return value

	def compare(self, other):
		value = 0
		if self.__cardVal > other.getVal():
			value = 1
		elif self.__cardVal < other.getVal():
			value = -1
		print(value)
		return value

class HighLow:
	def __init__(self):
		self.window = Tk()
		self.window.title = "High Low Game"
		self.infoFrm = Frame(self.window)
		self.HiLo = IntVar()
		self.HiLo.set(0)
		self.firstCardImage = PhotoImage(file = "image/card/b1fv.gif")
		self.firstCardBtn = Button(self.window, image = self.firstCardImage, command = self.processCard)
		self.infoLbl  = Label(self.infoFrm, text = "<- Pull a card")
		self.highRdo = Radiobutton(self.infoFrm, variable = self.HiLo, value = 1, text = "High", command = self.processRdo)
		self.lowRdo = Radiobutton(self.infoFrm, variable = self.HiLo, value = -1, text = "Low", command = self.processRdo)
		self.secondCardImage = PhotoImage(file = "image/card/b1fv.gif")
		self.secondCardBtn = Button(self.window, image = self.secondCardImage, command = self.evaluateCards, state = DISABLED)
		self.drawBtn = Button(self.window, text = "Draw", command = self.reset)
		
		self.firstCardBtn.grid(row = 1, column = 1)
		self.secondCardBtn.grid(row = 1, column = 3)
		self.infoLbl.grid(row = 1, column = 1)
		self.infoFrm.grid(row = 1, column = 2)

		self.window.mainloop()
		return

	def processCard(self):
		self.firstCard = Card()
		self.firstCardBtn["image"] = self.firstCard.getImage()
		self.firstCardBtn["state"] = "disabled"
		self.highRdo.grid(row = 2, column = 1)
		self.lowRdo.grid(row = 3, column = 1)
		self.infoLbl["text"] = "Choose High or Low"
		return

	def processRdo(self):
		self.secondCardBtn["state"] = "active"
		self.highRdo.grid_remove()
		self.lowRdo.grid_remove()
		self.infoLbl["text"] = "Pull your second card ->"
		print(self.HiLo.get())
		return

	def evaluateCards(self):
		self.secondCard = Card(self.firstCard.getRawImageVal)
		self.secondCardBtn["image"] = self.secondCard.getImage()
		if self.secondCard.compare(self.firstCard) == self.HiLo.get():
			self.infoLbl["text"] = "You Won!"
		else:
			self.infoLbl["text"] = "You Lost!"
		self.drawBtn.grid(row = 2, column = 2)
		return

	def reset(self):
		self.firstCardBtn["state"] = "active"
		self.firstCardBtn["image"] = self.firstCardImage
		self.secondCardBtn["image"] = self.secondCardImage
		self.infoLbl["text"] = "<- Pull a card"
		self.secondCardBtn["state"] = "disabled"
		self.drawBtn.grid_remove()
		self.HiLo.set(0)
		return

HighLow()