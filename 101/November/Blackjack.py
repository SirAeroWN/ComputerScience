# a simple blackjack game

from tkinter import *
import random

class Blackjack():
	def __init__(self):
		self.root = Tk()
		self.root.title("Blackjack")
		self.topCard = PhotoImage(file = "image/card/b1fv.gif")
		self.topCardLbl = Label(self.root, image = self.topCard).pack()
		self.score = 0
		print(self.score)
		self.scoreLbl = Label(self.root, text = str(self.score))
		self.scoreLbl.pack()
		self.hitBtn = Button(self.root, text = "Hit me!", command = self.hitTheFatty)
		self.hitBtn.pack()
		self.root.mainloop()
		return

	def hitTheFatty(self):
		cardVal = random.randint(1,52)
		if(cardVal % 13 == 0):
			self.score += 13
		self.score += cardVal % 13
		print(self.score)
		self.scoreStr = str(self.score)
		if(self.score > 21):
			self.scoreStr = "You Lose"
			self.hitBtn.destroy()
		elif(self.score == 21):
			self.scoreStr = "You Win!"
			self.hitBtn.destroy()
		self.scoreLbl["text"] = self.scoreStr
		self.topCard["file"] = "image/card/" + str(cardVal) + ".gif"
		return

Blackjack()