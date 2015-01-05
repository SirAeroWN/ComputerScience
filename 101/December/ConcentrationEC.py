#only commenting differneces, everything else is explained in Concentration.py comments

from tkinter import *
from tkinter import messagebox
import random #need random library to generate random coordinates

class Card:
	def __init__(self, imageFile, imageNum, nameTag, place, coords): #coordinates are passed as a concatenated string
		self.image = PhotoImage(file = imageFile)
		self.name = nameTag
		self.num = imageNum
		self.selected = False
		self.back = PhotoImage(file = 'image/card/b1fv.gif')
		self.button = Button(place, image = self.back, command = self.flipup)
		self.button.grid(row = int(coords[0]), column = int(coords[1])) #coord string is broken up, makes random assignment easier to manage
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
		global matches
		matches = 0
		global misses
		misses = 0
		global window
		window = Tk()
		window.title = 'Concentration'

		self.frame = Frame(window)
		self.frame.pack()

		self.setRandomBoard() #replaced nasty block of code with a neat little method call. So much prettier, right?

		self.nextbtn = Button(window, text = 'next', command = iterateList)
		self.nextbtn.pack()

		window.mainloop()
		return

	#method for setting up the board in a random fassion
	def setRandomBoard(self):
		self.used = [] #list of used coordinate pairs
		for i in range(0,16): #make sixteen buttons
			coords = self.findCoords(self.used) #get a random set of coordinates that haven't been used
			if i < 8: #loops through all eight images, doesn't matter that the images are assigned in order because the coords are random
				imageStr = 'image/puppy' + str(i + 1) + '.gif'
				number = i + 1
			else:
				imageStr = 'image/puppy' + str(i - 7) + '.gif' #repeat images
				number = i - 7
			name = str(i)
			Card(imageStr, number, name, self.frame, coords) #make the Card instance, grids itself and adds itself to global list
		return

	#make some random coordinates, can't have already been used
	def findCoords(self, usedlist):
		new = str(random.randint(1,4)) + str(random.randint(1,4)) #coordinate canidates, concatenated for comparison
		while contains(usedlist, new): #check to see if the coords have been used already
			new = str(random.randint(1,4)) + str(random.randint(1,4)) #keep making new ones until the pair hasn't been used
		usedlist.append(new) #add the new pair to the used list
		return new

#check to see if coords have already been used
def contains(listy, query):
	result = False
	for obj in listy: #go through the entire list of used coordinates
		if obj == query: #this is why the coords are stuck together into a string, eaier to compare
			result = True
	return result

def finishHim(title, message):
	messagebox.showinfo(title, message)
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
						global misses
						meesage = 'You Won!\nAnd in only took ' + str(misses + 8) + ' tries!' #a more interesting way to win
						finishHim('Winner', meesage)
				elif card.selected:
					global misses
					misses += 1
					card.flipdown()
					card.selected = False
					second.flipdown()
					second.selected = False
					if misses == 5:
						finishHim('Loser', 'You Lost')
		return

allTheCards = []
global matches
matches = 0
global misses
misses = 0

LeGame()