#asks user for some personal info and puts that in a file, then reads it

class Person:
	def __init__(self, infoString):
		info = infoString.split(',')
		self.first = info[0].strip()
		self.last = info[1].strip()
		self.color = info[2].strip()
		return

	def __str__(self):
		lestr = self.first + ' ' + self.last + '\'s favorite color is ' + self.color
		return lestr

oFile = open("people.peeps", "w")

more = True

while more:
	person = input("Enter a first name, last name, and favorite color, seperated by commas: ")
	oFile.write(person + '\n')
	if input("Do you want to add another person? [y/n]: ") == 'n':
		more = False
oFile.close()

people = []

iFile = open("people.peeps", "r")

for line in iFile:
	people.append(Person(line.strip()))

iFile.close()

for peep in people:
	print(peep)