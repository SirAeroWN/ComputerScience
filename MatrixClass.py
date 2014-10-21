class Matrix:
	def __init__(self, rows = 2, columns = 2):
		self.rows = rows
		self.columns = columns
		self.contents = []
		width = [1] * columns
		for i in range(0, rows): #in form matrix[rows][columns]
			self.contents.append(width)
		return

	def printit(self):
		print(self.contents)
		return

	def assignRow(self, row, contentList):
		if(len(contentList) == len(self.contents[row])):
			for i in (0, len(self.contents[row])):
				self.contents[row][i] = contentList[i]
		else:
			print("ERROR: in assignRow: List is not same size as matrix")

	def __add__(self, other):
		newMatrix = Matrix()
		for row in range(0, self.rows):
			for col in range(0, self.columns):
				newMatrix.contents[row][col] = self.contents[row][col] + other.contents[row][col]
		return newMatrix
#
#	def assignAll(self, contentList):
#		if((len(contentList[]) == self.__rows) and (len(contentList[0]):
#			for i in range(0, self.__rows):

a = Matrix()
#a.assignRow(0, [1,2])
a.printit()
b = Matrix()
#b.assignRow(1, [1,2])
b.printit()
c = a + b
c.printit()