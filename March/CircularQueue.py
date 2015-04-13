class DoublyLinkedListNode:
	def __init__(self, mydata, mynext, myprevious):
		self.data = mydata
		self.next = mynext
		self.prev = myprevious
		return

class CQueue:
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

	def addToTail(self, data):
		node = DoublyLinkedListNode(data, self.head, self.tail)
		if self.size == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
			self.head.prev = self.tail
		self.size += 1
		return

	def removeFromTail(self):
		self.tail = self.tail.prev
		self.tail.next = self.head
		self.size -= 1
		return

	def addToHead(self, data):
		if self.size == 0:
			nextNode = None
		else:
			nextNode = self.head
		node = DoublyLinkedListNode(data, nextNode, self.tail)
		self.head.prev = node
		self.head = node
		self.size += 1
		return

	def removeFromHead(self):
		self.head = self.head.next
		self.head.prev = None
		self.size -= 1
		return

	def peekHead(self):
		return self.head.data

	def peekTail(self):
		return self.tail.data