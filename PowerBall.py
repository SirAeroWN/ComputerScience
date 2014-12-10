import random

def prompt(upper, message):
	entry = eval(input(message))
	gotit = False
	while gotit == False:
		if entry > upper or entry < 1:
			retry = "Your number was not in the allowable range, 1-" + str(upper) + ", please try again: "
			entry = eval(input(retry))
		else:
			gotit = True
	return int(entry)

def getLottoNumber():
	lotto = ''
	lottoList =[]
	for i in range(0,5):
		lottoList.append(random.randint(1,59))
	lottoList.append(random.randint(1,35))
	lotto = sortandConvert(lottoList)
	return lotto

def sortandConvert(numList):
	listToSort = numList
	for i in range(len(listToSort)):
		minim = listToSort[i]
		minimIndex = i
		for j  in range(i + 1, len(listToSort)):
			if minim > listToSort[j]:
				minim = listToSort[j]
				minimIndex = j
		if minimIndex != i:
			listToSort[minimIndex] = listToSort[i]
			listToSort[i] = minim
	sortStr = ''
	for num in listToSort:
		sortStr += str(num)
	return sortStr

guesses = ''
guessList = []
for i in range(0,5):
	guessList.append(prompt(59, "Enter your number: "))
guessList.append(prompt(35, "Guess the PowerBall number: "))
guesses += sortandConvert(guessList)

rando = getLottoNumber()

if rando == guesses:
	print("Wow! You won on the very first draw, you should actually buy a lottery ticket.")
else:
	draws = 1
	missed = True
	while missed:
		draws += 1
		if draws % 1000000 == 0:
			print(draws)
		if guesses == getLottoNumber():
			print("You won the Lottery! It took", draws, "though...")
			missed = False