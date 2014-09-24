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
	while(divisor <= (number / 2)):
		if((number % divisor) == 0):
			return False
		divisor += 1
	return True

def findNumOfPrimes():
	count = 0
	for i in range(1, 10001):
		if(isPrime(i)):
			count += 1
	return count

print(findNumOfPrimes())
