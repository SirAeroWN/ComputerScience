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