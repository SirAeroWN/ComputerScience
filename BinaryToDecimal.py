#This recursively converts a binary number in string form to a decimal number

def decimalToBinary(value):
	newBinStr = ''
	for i in range(len(value) - 1, -1, -1):
		newBinStr += value[i]
	return decimalToBinaryHelper(newBinStr, 0, len(newBinStr))

def decimalToBinaryHelper(binStr, place, maxPlace):
	if place == maxPlace:
		returnThing = 0
	elif binStr[place] == '0':
		returnThing = 0 + decimalToBinaryHelper(binStr, place + 1, maxPlace)
	else:
		returnThing = 2**place + decimalToBinaryHelper(binStr, place + 1, maxPlace)
	return returnThing

print(decimalToBinary('10101'))