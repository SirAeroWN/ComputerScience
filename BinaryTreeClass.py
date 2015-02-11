class BinaryTreeNode:
	def __init__(self, data, leftChild = None, rightChild = None):
		self.data = data
		self.left = leftChild
		self.right = rightChild
		return

class BinaryTree:
	def __init__(self):
		self.root = None
		self.size = 0 #this never really updates...
		return

	def addChild(self, data):
		node = BinaryTreeNode(data)
		self.size += 1
		if self.root: #if it has a root already then you need to put the new node in the right place
			self.__compare(node, self.root)
		else: #otherwise it is the new root
			self.root = node
		return

	def __compare(self, lowerNode, higherNode):
		if lowerNode.data <= higherNode.data: #smaller and equal to will go to the left
			if higherNode.left == None: #check to see if there is alreay a node there
				higherNode.left = lowerNode
				return
			else:
				self.__compare(lowerNode, higherNode.left) #if there is a node there then compare the new node to it
		else:
			if higherNode.right == None: #if higher the go to right
				higherNode.right = lowerNode
				return
			else:
				self.__compare(lowerNode, higherNode.right) #if there is already a right node compare with that one
		return

	def inorder(self): #returns a list
		dataList = []
		self.inorderHelper(dataList, self.root)
		return dataList

	def inorderHelper(self, alist, node):
		if node == None: #don't return anything if there is nothing to return
			return
		self.inorderHelper(alist, node.left) #go all the way to the left
		alist.append(node.data) #once that ^ returns you pring the current node
		self.inorderHelper(alist, node.right) #now go down the right side
		return

	def preorder(self): #same as above, different order
		dataList = []
		self.preorderHelper(dataList, self.root)
		return dataList

	def preorderHelper(self, alist, node):
		if node == None:
			return
		alist.append(node.data)
		self.preorderHelper(alist, node.left)
		self.preorderHelper(alist, node.right)
		return

	def postorder(self): #same as above, different order
		dataList = []
		self.postorderHelper(dataList, self.root)
		return dataList

	def postorderHelper(self, alist, node):
		if node == None:
			return
		self.postorderHelper(alist, node.left)
		self.postorderHelper(alist, node.right)
		alist.append(node.data)
		return

# TheTreeOfLife = BinaryTree()
# continueing = True
# while continueing:
# 	tempInput = input("Enter a string to populate the binary tree with [type 'end' to stop]: ")
# 	if tempInput.lower() == 'end':
# 		continueing = False
# 	else:
# 		TheTreeOfLife.addChild(tempInput)

# print("Your input inorder: ", end = '')
# print(TheTreeOfLife.inorder())
# print("Your input preorder: ", end = '')
# print(TheTreeOfLife.preorder())
# print("Your input postorder: ", end = '')
# print(TheTreeOfLife.postorder())

#I made a ASCII box :)
#___
#|_|
