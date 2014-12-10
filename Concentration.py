from tkinter import * #import all of tkinter
from tkinter import messagebox #import messagebox class seperately because tkinter library has a weird directory structure and Sublime Text can't handle it

#Card class which each of the individual tiles is an instance of
class Card:
	def __init__(self, imageFile, imageNum, nameTag, place, x, y):
		self.image = PhotoImage(file = imageFile) #this is the image that they will try to match
		self.name = nameTag #unique id for each card, differnetiates same image cards
		self.selected = False #is it face up or down?
		self.num = imageNum #ids the image, two cards will have same number
		self.back = PhotoImage(file = 'image/card/b1fv.gif') #stock card back
		self.button = Button(place, image = self.back, command = self.flipup) #make the button here, class can access and avoids blocky, bloated code
		self.button.grid(row = y, column = x) #put button in correct place
		allTheCards.append(self) #adds to global list of cards, that way they can be accessed in other classes/methods
		return

	#method for when a card is flipped
	def flipup(self):
		self.selected = True #it got flipped
		self.button['image'] = self.image #show them the actual image
		self.button['command'] = self.homer #now when they click it does nothing, just like Homer Simpson :)
		return
	
	#method for flipping down, user never directly uses
	def flipdown(self):
		self.selected = False #flipped back down
		self.button['image'] = self.back #back to the back
		self.button['command'] = self.flipup #if clicked again it will act just like it did originally
		return

	#method to do absolutely nothing
	def homer(self):
		return

#the main GUI class, has all the ugliness of a frenchmen
##it was late when I wrote this, excuse the bad joke pun thingies
class LeGame:
	def __init__(self):
		global window #do this so that the window can be killed by external method
		window = Tk()
		window.title = 'Concentration' #name of the game

		self.frame = Frame(window) #make a neat little frame to put tiles/cards in
		self.frame.pack()

		#this is a big, messy, ugly block of declaring Card objects
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
		#actually, that didn't take long. Thank God for scripts!

		#checks for matching cards and winning/losing
		#need a "next" button because having Card.flipup() check doesn't give the player a fair shake
		##Card.flipup() changes the button image, but apparently the image displayed doesn't actually change until the method returns
		##and if Card.flipup() found that there wasn't a match it would naturally call Card.flipdown() and the user couldn't see what
		##the image on the second card was, making it way to difficult
		self.nextbtn = Button(window, text = 'next', command = iterateList)
		self.nextbtn.pack()

		window.mainloop() #run the window
		return

#now for some non-class methods! They could be in a class I'm sure but who doesn't like some variety?

#depricated, but left for posterity
# #the method for if they lose
# def itsAllOverNow(): #like the Rolling Stones reference?
# 	 #let them know that they lost
# 	finishHim() #find out if they want to continue
# 	return
	

# def theMiracle():
# 	messagebox.showinfo('Winner', 'You Won!')
# 	finishHim()
# 	return

def finishHim(title, message):
	#display messagebox before window is killed or it will make its own puppet which looks bad
	messagebox.showinfo(title, message)
	bart = messagebox.askyesno('Continue?', 'Would you like to play again?') #ask if they want to play again, returns True or False
	global window
	window.destroy() #kill the window no matter how much they beg
	if bart: #see if they wanted to keep playing
		LeGame() #if they did, start it all over and make an instance of the main GUI
	return #they keep playing as much as they want, when their done all of these returns are called and they go back down the stack until it ends

#called to check if the cards match
def iterateList():
		i = 0 #a control variable
		while i < len(allTheCards) - 1:
			if allTheCards[i].selected: #find the last selected card
				second = allTheCards[i]
			i += 1
		for card in allTheCards: #now go through all of the cards again
			if card.name != second.name: #make sure that the crad is not the same as the one that has already been selected, this is why they have names
				if card.selected and card.num == second.num: #see if the card is selected and that the image is the same
					global matches #if it gets here they got a match
					matches += 1
					card.button['state'] = 'disabled' #don"t let them reuse the card, it is now permanently up
					card.selected = False
					second.button['state'] = 'disabled'
					second.selected = False
					if matches == 8: #they have matched all the pairs
						finishHim('Winner', 'You Won!') #let them know that they won and ask if they wish to play again
				elif card.selected: #only checks if card is selected, will do nothing if they only have one selected
					global misses
					misses += 1 #they had an incorrect pair
					card.flipdown() #flip the cards back over
					card.selected = False
					second.flipdown()
					second.selected = False
					if misses == 5: #they missed too many times
						finishHim('Loser', 'You lost') #let them know that they lost and ask if they wish to play again
		return

allTheCards = [] #a list that will have all of the card objets in it
global matches
matches = 0 #number of correct pairings
global misses
misses = 0 #number of incorrect pairings
LeGame() #start me up
#ha, another music reference