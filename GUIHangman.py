#simple hangman game GUI

from tkinter import *
from tkinter import messagebox
import random

# class ManipString:
# 	def __init__(self, rawWord):
# 		self.__strList = self.toStrList(rawWord)
# 		self.__hidstrList = self.toStrList(self.hide())
# 		return

# 	def toStrList(self, passString):
# 		returnList = []
# 		for i in range(0, len(passString)):
# 			returnList.append(passString[i])
# 		return returnList

# 	def toPurStr(self, list):
# 		returnList = ""
# 		for i in self.__strList:
# 			returnList = returnList + i
# 		return returnList

# 	def hide(self):
# 		returnList = ""
# 		for i in self.__strList:
# 			returnList = returnList + '*'
# 		return returnList

# 	def getReal(self):
# 		return self.toPurStr(self.__strList)

# 	def getHid(self):
# 		return self.toPurStr(self.__hidstrList)

# 	def update(self, letter):
# 		myWord = self.__strList
# 		numOfCount = myWord.count(letter)
# 		if(numOfCount > 0):
# 			for i in range(0, numOfCount):
# 				indexOfLetter = myWord.index(letter)
# 				self.__hidstrList[indexOfLetter] = myWord[indexOfLetter]
# 				myWord[indexOfLetter] = '-'
# 		return

# class Word:
# 	def __init__(self):
# 		self.__rawString = ManipString(self.getRandomWord())
# 		return

# 	def getRandomWord(self):
# 		wordList = ["allow", "abduct", "abjure", "ablest", "abound", "absurd", "abused", "abuser", "acetyl", "acquit", "acuity", "aculei", "acumen", "acuter", "adieux", "adjoin", "adjure", "adjust", "advent", "adverb", "advert", "advice", "advise", "afield", "agnize", "agonic", "aguish", "akimbo", "albino", "albite", "alcove", "alexin", "algoid", "alined", "almond", "almost", "ambush", "amebic", "amidst", "ampule", "amulet", "amused", "anemic", "anodic", "anomic", "anomie", "anthem", "anther", "anyhow", "apercu", "aplite", "aplomb", "arched", "arcing", "ardent", "argent", "argued", "argufy", "argyle", "arisen", "arming", "armlet", "around", "arouse", "arpent", "artful", "ashore", "aspect", "aspire", "atonic", "atopic", "audile", "auklet", "auntie", "author", "autism", "avouch", "avowed", "aweigh", "awhile", "backed", "badger", "badmen", "bagmen", "bagnio", "bailed", "baited", "baling", "balked", "banged", "banger", "bangle", "banker", "banter", "bardic", "barged", "baring", "barite", "barmen", "barong", "goggle", "xerox", "zax", "mellow", "fly", "computer", "phone", "flem", "quitessential"]
# 		wordStr = wordList[random.randint(0, len(wordList) - 1)]
# 		return wordStr

# 	def isIn(self, letter):
# 		return self.__rawString.getReal().count(letter) > 0

# 	def gethid(self):
# 		return self.__rawString.getHid()

# 	def reHide(self, guess):
# 		self.__rawString.update(guess)
# 		return

# class Game:
# 	def __init__(self):
# 		self.window = Tk()
# 		self.canvas = Canvas(self.window, bg = 'white', width = 400, height = 400)
# 		self.canvas.pack()

# 		self.guessed = []
# 		self.theWord = Word()
# 		self.wordLbl = Label(self.window, text = self.theWord.gethid())
# 		self.wordLbl.pack()
# 		self.guess = StringVar()
# 		self.guessEnt = Entry(self.window, textvariable = self.guess)
# 		self.guessEnt.pack()
# 		self.guessBtn = Button(self.window, text = 'Guess', command = self.wordUp)
# 		self.guessBtn.pack()

# 		self.window.mainloop()
# 		return

# 	def wordUp(self):
# 		if self.guessed.count(self.guess.get()) > -1:
# 			if self.theWord.isIn(self.guess.get()):
# 				self.theWord.reHide(self.guess.get())
# 				self.guessed.append(self.guess.get())
# 				self.wordLbl['text'] = 'updating...'
# 				self.wordLbl['text'] = self.theWord.gethid()
# 		else:
# 			messagebox.showinfo('Really?', 'You already guessed that')

Game()