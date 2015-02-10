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

	def inorder(self):
		dataList = []
		self.inorderHelper(dataList, self.root)
		return dataList

	def inorderHelper(self, alist, node):
		if node == None:
			return
		self.inorderHelper(alist, node.left)
		alist.append(node.data)
		self.inorderHelper(alist, node.right)
		return

	def preorder(self):
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

	def postorder(self):
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

a = [5, 3, 6, 2, 4, 8, 1, 7, 9]
b = BinaryTree()
for o in a:
	b.addChild(o)
print(b.inorder())
print('--------------------------------')
print(b.preorder())
print('--------------------------------')
print(b.postorder())