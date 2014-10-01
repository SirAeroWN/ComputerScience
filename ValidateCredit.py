def isValid(number):
    prefixName = ""
    validity = False
    if(getSize(number) >= 13 and getSize(number) <= 16):
        if(((sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10) == 0):
                validity = True
        else:
                validity = False
    return validity

def sumOfDoubleEvenPlace(number):
    evenSum = 0
    for i in range(len(number)-2, -1, -2):
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
    for i in range(len(number)-1, -1, -2):
    	oddSum = oddSum + int(number[i])
    return oddSum

def prefixMatched(number, d):
    return (getPrefix(number, len(str(d))) == d)

def getSize(d):
    return len(d)

def getPrefix(number, k):
    rtnPrefix = ""
    for i in range(0, k):
    	rtnPrefix = rtnPrefix + str(number[i])
    return rtnPrefix

def checkPrefix(number):
    if(prefixMatched(number, '4')):
    	print("Visa")
    elif(prefixMatched(number, '5')):
    	print("Master Card")
    elif(prefixMatched(number, '37')):
    	print("American Express")
    elif(prefixMatched(number, '6')):
    	print("Discover")
    return

CCNumber = input("Please enter your credit card number: ")
if(isValid(CCNumber)):
    print("Your credit card number is valid, and is a ", end = '')
    checkPrefix(CCNumber)
else:
    print("Your credit card number is not valid")
