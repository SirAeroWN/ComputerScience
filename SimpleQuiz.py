#Simple Quiz
#Asks user for name, SSN, and then four questions with answers A, B, C, D
#Prints out results in a standard format

#Gets name
def getName():
	return input("Enter your name: ")

#Gets SSN and calls validateSSN to make sure SSN works
def getSSN():
	valid = False
	while(not valid): #Keep prompting until they give you one that works
		SSNumber = input("Enter your Social Security Number (xxx-xx-xxxx): ")
		if(validateSSN(SSNumber)):
			valid = True #wow they actually did it
		else:
			print("That is not a valid Social Security Number, make sure you included dashes and typed it correctly.") #give a helpful hint for how they screwed up
	return SSNumber

#makes sure SSN is in proper format, has several checks in increasing complexity
def validateSSN(possibleSSN):
	valid = False
	if(len(possibleSSN) == 11): #check for correct length
		if(possibleSSN.count('-') == 2): #make sure it has - before trying to split, cant use try: yet
			possibleSSNList = possibleSSN.split('-')
			if((len(possibleSSNList[0]) == 3) and (len(possibleSSNList[1]) == 2) and (len(possibleSSNList[2]) == 4)): #make sure the sections are right size
				valid = True #it did work!
	return valid

#prints queston and answers from list
def askQuestion(questionList, indexOfQuestion):
	for i in range(indexOfQuestion, indexOfQuestion + 5): #start index is question next four are answers, +5 because not inclusive
		print(questionList[i])
	return

#prompt the user for their answer
def getAnswer():
	acceptable = False
	while(not acceptable):
		userAnswer = input("Which is the best answer chioce? ").lower() #ask again
		if(checkAcceptable(userAnswer)):
			acceptable = True #finally!
		else:
			print("That is not an answer choice.") #tell them they screwed up
	return userAnswer

#makes sure user input can be an answer
def checkAcceptable(candidate):
	returnVal = False
	if((candidate == 'a') or (candidate == 'b') or (candidate == 'c') or (candidate == 'd')): #input is automatically switched to lower case, only need to check for lower
		returnVal = True
	return returnVal

#find out if they got them right and compile list to print based on rightness
def checkAnswers(answerList):
	correctList = ['a', 'b', 'c', 'd'] #right answers
	displayList = []
	numCorrect = 0 #for percentage
	for i in range(0, len(answerList)):
		displayList.append(str(i + 1)) #always going to have Q number at far left
		if(answerList[i] == correctList[i]):
			displayList.append("Correct")
			displayList.append('') #got it right, add correct and not correct answer
			numCorrect += 1 #increase score
		else:
			displayList.append("Wrong")
			displayList.append(correctList[i].upper()) #they were wrong, tell them and display answer in uppercase because that looks better
	percentCorrect = str((numCorrect / 4) * 100) + '%' #make percentage not decimal
	displayList.append(percentCorrect)
	return displayList

#prints the resuts table
def displayResults(name, SSNumber, displayListing):
	nameHeader = "\n" + format('', ">12s") + name + "'s " + "Test Results"
	SSNHeader = format('', ">9s") + "Social Security #: " + SSNumber #formatting stuffs
	tableHeader = "Question    Result       Correct Answer"
	print(nameHeader)
	print(SSNHeader, end = "\n\n")
	print(tableHeader)
	displaySpecAnswers(displayListing) #call function to print reduntant output
	print("\nTest score:", displayListing[len(displayListing)-1]) #round it out with their pathetic score

#prints the content of the table nicely
def displaySpecAnswers(displayList):
	for i in range(0, 12, 3): #going to print 3 objects at a time, so iterate i by 3
		displayString = format(displayList[i], "<12s") + format(displayList[i + 1], "<13s") + displayList[i + 2]
		print(displayString)

#now for the main stuff
def main():
	#Qs and answer choices
	questionsAndChoices = ["1) What are printers?", "  (A) Pure evil", "  (B) Mana from Heaven", "  (C) Devices that put ink on paper", "  (D) Cheap",
							 "2) Which is a very old Bash exploit?", "  (A) The Heartbleed bug", "  (B) env x='() { :;}; echo vulnerable' bash -c \"echo test\"", "  (C) The Bashbug bug", "  (D) curl -fsSL https://raw.0day.exploit.com/totallytheanswer",
							 "3) What is Python?", "  (A) A snake", "  (B) Something else that don't want none", "  (C) A programming language without semicolons", "  (D) A verb",
							 "4) At what point is it too late to program?", "  (A) 1:00 am", "  (B) When you see the sun come up", "  (C) It's never too late!", "  (D) when you starhjyuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"]
	userAnswers = [] #user answers, not filled yet

	#get their info
	userName = getName()
	userSSN = getSSN()

	#ask and get all the questions' answers
	for i in range(0, 20, 5):
		askQuestion(questionsAndChoices, i)
		userAnswers.append(getAnswer())

	#display every thing
	displayResultsList = checkAnswers(userAnswers)
	displayResults(userName, userSSN, displayResultsList)

	#see if they want to continue
	cont = input("\nWould you like to take the quiz again? y/n ").lower()
	if(cont == 'y'):
		returnVal = True
	else:
		returnVal = False
	return returnVal

#Go until they want to stop
#main() returns True/False for continue or not
while(main()):
	print("\n\n\nYou asked for it:\n\n\n")
print("GoodBye")