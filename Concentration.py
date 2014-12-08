from tkinter import *
from tkinter import messagebox

class Card:
	def __init__(self, imageFile, imageNum, nameTag, place, x, y):
		self.image = PhotoImage(file = imageFile)
		self.name = nameTag
		self.selected = False
		self.num = imageNum
		self.back = PhotoImage(file = 'image/card/b1fv.gif')
		self.button = Button(place, image = self.back, command = self.flipup)
		self.button.grid(row = y, column = x)
		allTheCards.append(self)
		return

	def flipup(self):
		self.selected = True
		self.button['image'] = self.image
		self.button['command'] = self.homer
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

		self.btn1 = Card('image/puppy1.gif', 1, 'these', self.frame, 1, 1)
		self.btn2 = Card('image/puppy2.gif', 2, 'names', self.frame, 1, 2)
		self.btn3 = Card('image/puppy3.gif', 3, 'do', self.frame, 1, 3)
		self.btn4 = Card('image/puppy4.gif', 4, 'not', self.frame, 1, 4)
		self.btn5 = Card('image/puppy1.gif', 1, 'really', self.frame, 2, 1)
		self.btn6 = Card('image/puppy5.gif', 5, 'matter', self.frame, 2, 2)
		self.btn7 = Card('image/puppy6.gif', 6, ',', self.frame, 2, 3)
		self.btn8 = Card('image/puppy7.gif', 7, 'they', self.frame, 2, 4)
		self.btn9 = Card('image/puppy8.gif', 8, 'are', self.frame, 3, 1)
		self.btn10 = Card('image/puppy4.gif', 4, 'just', self.frame, 3, 2)
		self.btn11 = Card('image/puppy7.gif', 7, 'for', self.frame, 3, 3)
		self.btn12 = Card('image/puppy8.gif', 8, 'telling', self.frame, 3, 4)
		self.btn13 = Card('image/puppy2.gif', 2, 'them', self.frame, 4, 1)
		self.btn14 = Card('image/puppy6.gif', 6, 'apart', self.frame, 4, 2)
		self.btn15 = Card('image/puppy5.gif', 5, 'from', self.frame, 4, 3)
		self.btn16 = Card('image/puppy3.gif', 3, 'eachother', self.frame, 4, 4)

		self.nextbtn = Button(window, text = 'next', command = iterateList)
		self.nextbtn.pack()

		window.mainloop()
		return

def itsAllOverNow():
	messagebox.showinfo('Loser', 'You Lost')
	global window
	window.destroy()
	return

def theMiracle():
	messagebox.showinfo('Winner', 'You Won!')
	global window
	window.destroy()
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
					print(matches)
					card.button['state'] = 'disabled'
					card.selected = False
					second.button['state'] = 'disabled'
					second.selected = False
					if matches == 8:
						theMiracle()
				elif card.selected:
					global misses
					misses += 1
					print(misses)
					card.flipdown()
					card.selected = False
					second.flipdown()
					second.selected = False
					if misses == 5:
						itsAllOverNow()
		return

allTheCards = []
global matches
matches = 0
global misses
misses = 0
bart = 0
LeGame()
while bart == 0:
	if messagebox.askyesno('Continue?', 'Would you like to play again?'):
		LeGame()
	else:
		bart = 1