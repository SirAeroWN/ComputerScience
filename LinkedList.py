#Sample linked list class

class LinkedListNode:
	def __init__(self, mydata, mynext):
		self.data = mydata
		self.next = mynext
		return

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = self.head
		self.size = 0
		return

	def __str__(self):
		theString = ''
		curNode = self.head
		atTheEnd = False
		while not atTheEnd:
			theString = theString + str(curNode.data)
			if curNode.next == None:
				atTheEnd = True
			curNode = curNode.next
		return theString

	def addToRear(self, data):
		node = LinkedListNode(data, None)
		if self.size == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1
		return

	def removeFromRear(self):
		curNode = self.head
		for i in range(self.size - 2):
			curNode = curNode.next
		curNode.next = None
		self.tail = curNode
		self.size -= 1
		return

	def addToFront(self, data):
		if self.size == 0:
			nextNode = None
		else:
			nextNode = self.head
		node = LinkedListNode(data, nextNode)
		self.head = node
		self.size += 1
		return

	def removeFromFront(self):
		self.head = self.head.next
		self.size -= 1

