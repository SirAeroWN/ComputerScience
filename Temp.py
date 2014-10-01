def getPrefix(number, k):
    rtnPrefix = ""
    for i in range(0, k):
    	rtnPrefix = rtnPrefix + str(number[i])
    return rtnPrefix

def prefixMatched(number, d):
    return (getPrefix(number, len(str(d))) == d)

def checkPrefix(number):
    if(prefixMatched(number, 4)):
    	print("Visa")
    elif(prefixMatched(number, 5)):
    	print("Master Card")
    elif(prefixMatched(number, 37)):
    	print("American Express")
    elif(prefixMatched(number, 6)):
    	print("Discover")
    return

checkPrefix()