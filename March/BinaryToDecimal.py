#This recursively converts a binary number in string form to a decimal number

# wrapper for recursive function
def decimalToBinary(value):
	newBinStr = '' # empty string
	# now flip the binary around so we can go left -> right and be going from 0 place up
	for i in range(len(value) - 1, -1, -1):
		newBinStr += value[i]
	return decimalToBinaryHelper(newBinStr, 0, len(newBinStr)) # start recursive calls

# recursive converter
def decimalToBinaryHelper(binStr, place, maxPlace):
	if place == maxPlace: # if at the very end return a 0 to stop recursion and not change end value
		returnThing = 0
	elif binStr[place] == '0': # if the place has a zero in it then we add zero to decimal and call again
		returnThing = 0 + decimalToBinaryHelper(binStr, place + 1, maxPlace)
	else: # otherwise it must be a 1 so we add 2^whatever place it is and call again
		returnThing = 2**place + decimalToBinaryHelper(binStr, place + 1, maxPlace)
	return returnThing

print(decimalToBinary('10101')) # test number = 21