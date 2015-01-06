#gets a file from user, prints random numbers to it, and then reads the numbers from the file

import random #to generate random numbers
import os.path #to test if file exists

fileStr = input('Enter a filename: ') #get file

while os.path.isfile(fileStr): #keep asking until its a new filename
	fileStr = input('File name already used\nEnter a different filename: ')

outFile = open(fileStr, "w") #open it to write

for i in range(0,100): #write a hundred numbers
	if i == 99:
		outFile.write((str(random.randint(0,100))))
	else:
		outFile.write((str(random.randint(0, 100)) + ' '))

outFile.close() #close to actually write

infile = open(fileStr, "r") #open and read
nums = infile.readline().split(' ')
nums.sort()
for item in nums:
	print(item, end = ' ')