#simple game of hangman
import random #for picking word
import String #for doing partial word hiding

def findLetters(myWord, hiddenString):
	myWord = String.toStrList(myWord)

wordList = ["allow", "abduct", "abjure", "ablest", "abound", "absurd", "abused", "abuser", "acetyl", "acquit", "acuity", "aculei", "acumen", "acuter", "adieux", "adjoin", "adjure", "adjust", "advent", "adverb", "advert", "advice", "advise", "afield", "agnize", "agonic", "aguish", "akimbo", "albino", "albite", "alcove", "alexin", "algoid", "alined", "almond", "almost", "ambush", "amebic", "amidst", "ampule", "amulet", "amused", "anemic", "anodic", "anomic", "anomie", "anthem", "anther", "anyhow", "apercu", "aplite", "aplomb", "arched", "arcing", "ardent", "argent", "argued", "argufy", "argyle", "arisen", "arming", "armlet", "around", "arouse", "arpent", "artful", "ashore", "aspect", "aspire", "atonic", "atopic", "audile", "auklet", "auntie", "author", "autism", "avouch", "avowed", "aweigh", "awhile", "backed", "badger", "badmen", "bagmen", "bagnio", "bailed", "baited", "baling", "balked", "banged", "banger", "bangle", "banker", "banter", "bardic", "barged", "baring", "barite", "barmen", "barong", "goggle", "xerox", "zax", "mellow", "fly", "computer", "phone", "flem", "quitessential"]

found = 0
word = wordList[random.randint(0, 108)]
showWord = String.toStrList(("*"*len(word)))
while(found == 0):
	print("Enter a letter in word ", String.toPurStr(showWord), end = '')
	guess = input(" > ")
