class DoublyLinkedListNode:
	def __init__(self, mydata, mynext, myprevious):
		self.data = mydata
		self.next = mynext
		self.prev = myprevious
		return

class DoublyLinkedList:
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
		node = DoublyLinkedListNode(data, None, self.tail)
		if self.size == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1
		return

	def removeFromRear(self):
		self.tail = self.tail.prev
		self.tail.next = None
		return

	def addToFront(self, data):
		if self.size == 0:
			nextNode = None
		else:
			nextNode = self.head
		node = DoublyLinkedListNode(data, nextNode, None)
		self.head.prev = node
		self.head = node
		self.size += 1
		return

	def removeFromFront(self):
		self.head = self.head.next
		self.head.prev = None
		self.size -= 1
		return