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
		return

class BinaryTreeNode:
	def __init__(self, data, leftChild = None, rightChild = None):
		self.data = data
		self.left = leftChild
		self.right = rightChild
		return

class BinaryTree:
	def __init__(self):
		self.root = None
		self.height = 0
		return

	def __str__(self):
		lestr = self.strAcrue(self.root)
		return lestr


	def addChild(self, data):
		node = BinaryTreeNode(data)
		if self.root:
			self.__compare(node, self.root)
		else:
			self.root = node
			self.height = 1
		return

	def __compare(self, lowerNode, higherNode):
		if lowerNode.data <= higherNode.data:
			if higherNode.left == None:
				higherNode.left = lowerNode
				return
			else:
				self.__compare(lowerNode, higherNode.left)
		else:
			if higherNode.right == None:
				higherNode.right = lowerNode
				return
			else:
				self.__compare(lowerNode, higherNode.right)
		return

	def strAcrue(self, node):
		if node == None:
			return ''
		else:
			return self.strAcrue(node.left) + str(node.data) + self.strAcrue(node.right)

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

class Stack:
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

	def push(self, data): #add to the top
		if self.size == 0:
			nextNode = None
		else:
			nextNode = self.head
		node = LinkedListNode(data, nextNode)
		self.head = node
		self.size += 1
		return

	def pop(self):
		self.head = self.head.next
		self.size -= 1
		return

class Queue:
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

	def enqueue(self, data):
		node = LinkedListNode(data, None)
		if self.size == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1
		return

	def dequeue(self):
		response = self.head.data
		self.head = self.head.next
		self.size -= 1
		return response

	def peek(self):
		return self.head.data

lst = ['a', 'z', 'b', 'y', 'c', 'x', 'd', 'w', 'u', 'e', 't', 'f', 's', 'g', 'r', 'h', 'q', 'i', 'p', 'j', 'o', 'k', 'n', 'l', 'm', 'v']
a = BinaryTree()
for i in lst:
	a.addChild(i)
print(a)