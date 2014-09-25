def isValid(number):
	prefixName = ""
	validity = False
	if(getSize(number) >= 13 and getSize(number) <= 16):
		visaPrefix = 4
		MasterPrefix = 5
		AmExPrefix = 37
		DiscoverPrefix = 6
		if(prefixMatched(number, visaPrefix)):
			prefixName = "Visa"
		elif(prefixMatched(number, MasterPrefix)):
			prefixName = "Master Card"
		elif(prefixMatched(number, AmExPrefix)):
			prefixName = "American Express"
		elif(prefixMatched(number, DiscoverPrefix)):
			prefixName = "Discover"
		if(((sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10) == 0):
			validity = True
		else:
			validity = False
	return validity

def sumOfDoubleEvenPlace(number):
	evenSum = 0
	for i in range(0, len(number), 2):
		evenSum = evenSum + getDigit(number[i])
	return evenSum

def getDigit(number):
	passedNum = int(number)
	passedNum = passedNum * 2
	if(passedNum > 9):
		passedNum = str(passedNum)
		numToReturn = int(passedNum[0]) + int(passedNum[1])
	else:
		numToReturn = passedNum
	return numToReturn

def sumOfOddPlace(number):
	oddSum = 0
	for i in range(1, len(number), 2):
		oddSum = oddSum + int(number[i])
	return oddSum

def prefixMatched(number, d):
	return getPrefix(number, len(str(d))) == d

def getSize(d):
	return len(d)

def getPrefix(number, k):
	rtnPrefix = ""
	for i in range(0, k):
		rtnPrefix = rtnPrefix + number[i]
	return rtnPrefix


if(isValid(input("Please enter your credit card number: "))):
	print("Your credit card number is valid, and mine now")
else:
	print("Your credit card number is not valid")