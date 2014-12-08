from tkinter import *
from tkinter import messagebox
import random

class Card:
	def __init__(self, imageFile, imageNum, nameTag, place, coords):
		self.image = PhotoImage(file = imageFile)
		self.name = nameTag
		self.num = imageNum
		self.selected = False
		self.back = PhotoImage(file = 'image/card/b1fv.gif')
		self.button = Button(place, image = self.back, command = self.flipup)
		self.button.grid(row = int(coords[0]), column = int(coords[1]))
		allTheCards.append(self)
		return

	def flipup(self):
		self.selected = True
		self.button['image'] = self.image
		self.button['command'] = self.homer
		nonSelected = []
		return
	
	def flipdown(self):
		self.selected = False
		self.button['image'] = self.back
		self.button['command'] = self.flipup
		return

	def homer(self):
		return

class LeGame:
	def __init__(self):
		global window
		window = Tk()
		window.title = 'Concentration'

		self.frame = Frame(window)
		self.frame.pack()

		self.setRandomBoard()

		self.nextbtn = Button(window, text = 'next', command = iterateList)
		self.nextbtn.pack()

		window.mainloop()
		return

	def setRandomBoard(self):
		self.used = []
		for i in range(0,16):
			coords = self.findCoords(self.used)
			if i < 8:
				imageStr = 'image/puppy' + str(i + 1) + '.gif'
				number = i + 1
			else:
				imageStr = 'image/puppy' + str(i - 7) + '.gif'
				number = i - 7
			name = str(i)
			newCard = Card(imageStr, number, name, self.frame, coords)
		return

	def findCoords(self, usedlist):
		new = str(random.randint(1,4)) + str(random.randint(1,4))
		while contains(usedlist, new):
			new = str(random.randint(1,4)) + str(random.randint(1,4))
		usedlist.append(new)
		return new

def contains(listy, query):
	result = False
	for obj in listy:
		if obj == query:
			result = True
	return result

def itsAllOverNow():
	messagebox.showinfo('Loser', 'You Lost')
	bart = messagebox.askyesno('Continue?', 'Would you like to play again?')
	global window
	window.destroy()
	if bart:
		LeGame()
	return

def theMiracle():
	global misses
	meesage = 'You Won!\nAnd in only took ' + str(misses + 8) + ' tries!'
	messagebox.showinfo('Winner', meesage)
	bart = messagebox.askyesno('Continue?', 'Would you like to play again?')
	global window
	window.destroy()
	if bart:
		LeGame()
	return

def iterateList():
		i = 0
		while i < len(allTheCards) - 1:
			if allTheCards[i].selected:
				second = allTheCards[i]
			i += 1
		for card in allTheCards:
			if card.name != second.name:
				if card.selected and card.num == second.num:
					global matches
					matches += 1
					card.button['state'] = 'disabled'
					card.selected = False
					second.button['state'] = 'disabled'
					second.selected = False
					if matches == 8:
						theMiracle()
				elif card.selected:
					global misses
					misses += 1
					card.flipdown()
					card.selected = False
					second.flipdown()
					second.selected = False
					if misses == 30:
						itsAllOverNow()
		return

allTheCards = []
global matches
matches = 0
global misses
misses = 0

theThingFromTheBasement = LeGame()