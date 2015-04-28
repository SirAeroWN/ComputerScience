# symbolically calculates derivivative
# input is strict: in general form ax^3 + bx^2 + cx + d
# handles any number of powers and terms
# if you try a divide or multiply shit will go down

class DoublyLinkedListNode:
	def __init__(self, mydata, mynext, myprevious):
		self.data = mydata
		self.next = mynext
		self.prev = myprevious
		return

class DEQ:
	def __init__(self):
		self.head = None
		self.tail = self.head
		self.size = 0
		return

	def __str__(self):
		theString = ''
		curNode = self.head
		atTheEnd = False
		theString = theString + str(curNode.data)
		if curNode.next == None:
			atTheEnd = True
		curNode = curNode.next
		while not atTheEnd:
			theString = theString + ' + ' + str(curNode.data)
			if curNode.next == None:
				atTheEnd = True
			curNode = curNode.next
		return theString

	def addToTail(self, data):
		node = DoublyLinkedListNode(data, None, self.tail)
		if self.size == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1
		return

	def removeFromTail(self):
		self.tail = self.tail.prev
		self.tail.next = None
		return

	def addToHead(self, data):
		if self.size == 0:
			nextNode = None
		else:
			nextNode = self.head
		node = DoublyLinkedListNode(data, nextNode, None)
		self.head.prev = node
		self.head = node
		self.size += 1
		return

	def removeFromHead(self):
		self.head = self.head.next
		self.head.prev = None
		self.size -= 1
		return

	def removeCurrent(self, current):
		if current == self.tail:
			self.removeFromTail()
		elif current == self.head:
			self.removeFromHead()
		else:
			current.prev.next = current.next
			current.next.prev = current.prev
		return

	def peekHead(self):
		return self.head.data

	def peekTail(self):
		return self.head.data

# takes in from ax^b, a can be negative
class term:
	def __init__(self, termInStringForm):
		propertyList = self.assessString(termInStringForm) # returns a list [float coeficient, string letter, float power]
		self.co = propertyList[0]
		self.letter = propertyList[1]
		self.power = propertyList[2]
		return

	def __str__(self):
		string = str(self.co) + self.letter
		if self.power != 0 and self.power != 1:
			string += '^' + str(self.power)
		return string

	def assessString(self, termString):
		coefficient = float(self.assessCoHelper(termString, 0))
		letterList = self.assessLHelper(termString)
		letter = letterList[0]
		if letterList[1] >= (len(termString) - 1):
			power = 0
		else:
			power = eval(self.assessPHelper(termString, letterList[1] + 2))
		return [coefficient, letter, power]

	# recursive helper for coeficient
	def assessCoHelper(self, tstr, iterr):
		if iterr == len(tstr): # we have reached the very end so we return, should only happen if dealing with a constant
			return ''
		letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		if iterr == 0 and tstr[iterr].lower() in letters: # no coeficient so coeficient is 1
			return '1'
		if tstr[iterr].lower() not in letters: # char is a number, check to see if next char is too
			return tstr[iterr] + self.assessCoHelper(tstr, iterr + 1)
		elif tstr[iterr].lower() in letters: # char is a letter, return nothing and stop the recursion chain
			return ''

	# iterative helper for letter
	def assessLHelper(self, tstr):
		letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		found = False
		i = 0
		result = ['letter', 0]
		while not found:
			#print(i)
			if i == len(tstr):
				result[0] = ''
				result[1] = i
				found = True
			elif tstr[i].lower() in letters:
				result[0] = tstr[i]
				result[1] = i
				found = True
			else:
				i += 1
		return result

	# recursive helper for power
	def assessPHelper(self, tstr, iterr):
		if iterr == len(tstr):
			return ''
		else:
			return tstr[iterr] + self.assessPHelper(tstr, iterr + 1)

# takes in form ax^b + cx^d + ... + e, coeficieants can be negative, '+' is for now just a formality but is also a necessity
class poly:
	def __init__(self, polynomialString):
		self.terms = self.interpret(polynomialString.strip())
		return

	def __str__(self):
		return str(self.terms)

	def interpret(self, poly):
		que = DEQ()
		start = 0
		index = 0
		atEnd = False
		prime = False
		while not atEnd:
			if start == len(poly) - 1:
				prime = True
			index = self.getTerm(poly, start)
			print('start:', start, '\nindex:', index)
			if index == len(poly) - 1:
				que.addToTail(term(poly[start:]))
			else:
				que.addToTail(term(poly[start:index]))
			start = self.getNewStart(poly, index)
			if prime:
				atEnd = True
			#print('start2:', start)
		return que

	def getTerm(self, poly, currindex):
		ind = currindex
		there = False
		while not there:
			if ind == len(poly):
				ind = (len(poly) - 1)
				there = True
			elif poly[ind] == ' ':
				there = True
			else:
				ind += 1
		return ind

	def getNewStart(self, poly, ind):
		there = False
		while not there:
			if poly[ind] == ' ' or poly[ind] == '+':
				ind += 1
			else:
				there = True
		return ind

print(term('4'))
a = poly('x^4 + 6x^3 + -5x^2 + 3x + 4')
print(a)