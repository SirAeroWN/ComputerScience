def reverseDepricated(number):
	numStr = str(number)
	i = len(numStr) - 1
	returnStr = ""
	while(i >= 0):
	    returnStr = returnStr + numStr[i]
	    i -= 1
	return int(returnStr)

def isPalindrome(number):
        return (number == reverse(number))

def reverse(number):
    numStr = ""
    while(number > 0):
        lowestPlace = number % 10
        number = number // 10
        numStr = numStr + str(lowestPlace)
    return int(numStr)

def isPrime(number):
    divisor = 2
    boolVal = True
    while(divisor <= (number / 2)):
        if((number % divisor) == 0):
            boolVal = False
        divisor += 1
    return boolVal

def findNumOfPrimes():
    count = 0
    for i in range(1, 10001):
        #if(isPrime(i)):
        if(isPalindrome(i)):
            count += 1
    return count

def isPrimePalindrome(number):
    boolVal = False
    if(isPalindrome(number)):
        if(isPrime(number)):
            boolVal = True
    return boolVal

def formatPrint(unformStr):
    print(format(unformStr, ">7s"), end = '')
    return

def findYoPalenPrimes():
    count = 0
    displayCount = 0
    candidate = 1
    while(count < 100):
        if(isPrimePalindrome(candidate)):
            formatPrint(str(candidate))
            displayCount += 1
            count += 1
        if(displayCount == 10):
            print("\n")
            displayCount = 0
        candidate += 1
    return

findYoPalenPrimes()

