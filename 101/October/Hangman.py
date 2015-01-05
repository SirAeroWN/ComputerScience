#simple game of hangman
import random #for picking word

def toStrList(passString):
	returnList = []
	for i in range(0, len(passString)):
		returnList.append(passString[i])
	return returnList

def toPurStr(passList):
	returnList = ""
	for i in passList:
		returnList = returnList + i
	return returnList

def findLetters(myWord, letter, hiddenString):
	myWord = toStrList(myWord)
	numOfCount = myWord.count(letter)
	if(numOfCount > 0):
		for i in range(0, numOfCount):
			indexOfLetter = myWord.index(letter)
			hiddenString[indexOfLetter] = myWord[indexOfLetter]
			myWord[indexOfLetter] = '-'
	return hiddenString

def prompt(wordToGuess):
	print("(Guess) Enter a letter in word ", toPurStr(wordToGuess), end = '')
	userGuess = input(" > ")
	check = len(userGuess)
	while(check != 1):
		print("Your guess needs to be one letter")
		print("(Guess) Enter a letter in word ", toPurStr(wordToGuess), end = '')
		userGuess = input(" > ")
		check = len(userGuess)
	return userGuess

def inWord(myWord, letter):
	return ((toStrList(myWord)).count(letter) > 0)

def main():
	wordList = ["allow", "abduct", "abjure", "ablest", "abound", "absurd", "abused", "abuser", "acetyl", "acquit", "acuity", "aculei", "acumen", "acuter", "adieux", "adjoin", "adjure", "adjust", "advent", "adverb", "advert", "advice", "advise", "afield", "agnize", "agonic", "aguish", "akimbo", "albino", "albite", "alcove", "alexin", "algoid", "alined", "almond", "almost", "ambush", "amebic", "amidst", "ampule", "amulet", "amused", "anemic", "anodic", "anomic", "anomie", "anthem", "anther", "anyhow", "apercu", "aplite", "aplomb", "arched", "arcing", "ardent", "argent", "argued", "argufy", "argyle", "arisen", "arming", "armlet", "around", "arouse", "arpent", "artful", "ashore", "aspect", "aspire", "atonic", "atopic", "audile", "auklet", "auntie", "author", "autism", "avouch", "avowed", "aweigh", "awhile", "backed", "badger", "badmen", "bagmen", "bagnio", "bailed", "baited", "baling", "balked", "banged", "banger", "bangle", "banker", "banter", "bardic", "barged", "baring", "barite", "barmen", "barong", "goggle", "xerox", "zax", "mellow", "fly", "computer", "phone", "flem", "quitessential", "i give up", "to be or not to be", "my kingdom for a horse", "          ", "do you like phrases that are really long as if i were messing with you"]

	play = 'y'

	while(play == 'y'):

		found = 0
		missed = 0
		word = wordList[random.randint(0, len(wordList)-1)]
		showWord = toStrList(("*"*len(word)))
		guessedWords = []

		while(found == 0):

			guess = prompt(showWord).lower()

			if(guess in guessedWords):
				print("\tYou already guessd", guess)
			elif(not inWord(word, guess)):
				guessedWords.append(guess)
				missed += 1
			else:
				guessedWords.append(guess)
				showWord = findLetters(word, guess, showWord)
				if(toPurStr(showWord) == word):
					print("\tYou got it! It was", word + ".", "But you missed it", missed, "times.")
					found = 1

		play = input("Would you like to play again? y/n ").lower()

main()