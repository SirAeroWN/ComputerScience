#matrix Class and main function to find solution for a 2x2 or 3x3 matrix

class Matrix:
	def __init__(self, rows = 2, columns = 2):
		self.__rows = rows
		self.__columns = columns
		self.__contents = []
		for i in range(0, rows): #in form matrix[rows][columns]
			self.__contents.append([0] * columns) #makes matrix full of zeros
		return

	#overloads * operator
	#######also, Cailean was supposed to do this but did not######
	def __mul__(self, other):
		if(self.__columns == other.getRows()): #chaeck sizes
			newMatrix = Matrix(self.__rows, other.getColumns())
			for i in range(0, self.__rows): #goes through all of the rows
				for j in range(0, other.getColumns()): #goes through self cols and other rows
					coordVal = 0
					for k in range(0, self.__columns): #iterates through to add all vals
						coordVal += self.__contents[i][k] * other.getEntry(k, j)# other.__contents[k][j]
					newMatrix.__contents[i][j] = coordVal
		return newMatrix

	#overides print
	def __str__(self):
		leString = ""
		for i in range(0, self.__rows): #each row
			leString = leString + "["
			for j in range(0, self.__columns): #each item in col
				if(j == 0):
					leString = leString + str(self.__contents[i][j])
				else:
					leString = leString + "," + str(self.__contents[i][j])
			leString = leString + "]\n"
		return leString

	#you know about getters
	def getRows(self):
		return self.__rows

	def getColumns(self):
		return self.__columns

	#you can assign a whole row at one time
	def assignRow(self, row, contentList):
		if(len(contentList) == self.__columns):
			upper = self.__columns
			i = 0
			while(i < upper):
				self.__contents[row][i] = contentList[i]
				i += 1
		else:
			print("ERROR: in assignRow: List is not same size as matrix")
		return

	#same for col
	def assignColumn(self, column, contentList):
		if(len(contentList) == self.__rows):
			for i in range(0, self.__rows):
				self.__contents[i][column] = contentList[i]
		return

	def getEntry(self, row, column):
		return self.__contents[row][column]

	def setEntry(self, row, column, newVal):
		self.__contents[row][column] = newVal

	#adds identity matrix to left
	def augmentIdentity(self):
		augmented = Matrix(self.__rows, (self.__columns * 2))
		for i in range(0, self.__rows):
			newRow = self.__contents[i]
			for j in range(0, i):
				newRow.append(0)
			newRow.append(1)
			for k in range(0, (self.__rows - i) - 1):
				newRow.append(0)
			augmented.assignRow(i, newRow)
		self.__columns = self.__columns * 2
		return augmented

	#multiplies row, doesnt directly alter
	def rowMul(self, row, scalar):
		alterMatrix = self
		for i in range(0, alterMatrix.__columns):
			alterMatrix.__contents[row][i] = alterMatrix.__contents[row][i] * scalar
		return alterMatrix

	#divides row, doesnt directly alter
	def rowDiv(self, row, scalar):
		alteredMatrix = self
		for i in range(0, alteredMatrix.__columns):
			alteredMatrix.__contents[row][i] = alteredMatrix.__contents[row][i] / scalar
		return alteredMatrix

	#adds two rows, alters second
	def rowAdd(self, first, second):
		alteredMatrix = self
		for i in range(0, alteredMatrix.__columns):
			alteredMatrix.__contents[second][i] = alteredMatrix.__contents[second][i] + alteredMatrix.__contents[first][i]
		return alteredMatrix

	#combines two rows
	def rowCombine(self, scalarRow1, MulDiv, row1, row2):
		propMatrix = self
		if(MulDiv == 1):
			propMatrix.rowMul(row1, scalarRow1)
		else:
			propMatrix.rowDiv(row1, scalarRow1)
		propMatrix.rowAdd(row1, row2)
		if(MulDiv == 1):
			propMatrix.rowDiv(row1, scalarRow1)
		else:
			propMatrix.rowMul(row1, scalarRow1)
		return propMatrix

	#row reduce until identity is on left
	def rref(self):
		#get bottom triangle of zeros
		for k in range(0, self.__rows): #every row
			for i in range(k, self.__rows): #leading val is one now
				self.rowDiv(i, self.__contents[i][k])
			for j in range(k + 1, self.__rows): #multiplies and combines to get a zero
				self.rowCombine(-1, 1, k, j)

		#get top triangle of zeros
		#same as above but opposite
		for i in range(0, (self.__rows) - 1):
			for j in range((i + 1), self.__rows):
				if(self.__contents[i][j] != 0):
					self.rowCombine((-1 * self.__contents[i][j]), 1, j, i)
		return

	#removes Identity from left side
	def stripFront(self):
		stripped = Matrix(self.__rows, int(self.__columns / 2))
		for i in range(0, self.__rows):
			k = 0
			for j in range(self.__rows, self.__columns):
				stripped.__contents[i][k] = float(format(self.__contents[i][j], "4.4f"))
				k += 1
		self.__contents = stripped.__contents
		self.__columns = int(self.__columns / 2)
		return

	#gets determinate
	def determinant(self):
		if(self.__rows == 2):
			determinant = (self.__contents[0][0] * self.__contents[1][1])-(self.__contents[0][1]*self.__contents[1][0])
		elif(self.__rows == 3):
			determinant = (self.__contents[0][0]*self.__contents[1][1]*self.__contents[2][2])+(self.__contents[0][1]*self.__contents[1][2]*self.__contents[2][0])+(self.__contents[0][2]*self.__contents[1][0]*self.__contents[2][1])-(self.__contents[0][2]*self.__contents[1][1]*self.__contents[2][0])-(self.__contents[0][1]*self.__contents[1][0]*self.__contents[2][2])-(self.__contents[0][0]*self.__contents[1][2]*self.__contents[2][1])
		return determinant

#checks that solution exists
def DoesSolutionExist(matrix):
	if(matrix.determinant() == 0):
		solution = False
	else:
		solution = True
	return solution

#returns inverted matrix
def Inverse(matrix):
		if(DoesSolutionExist(matrix)):
			inverted = matrix
			inverted.augmentIdentity()
			inverted.rref()
			inverted.stripFront()
		else:
			print("Not invertable!")
			inverted = None
		return inverted

#multiplies inv(A) and constant C
def SystemSolution(matrixA, matrixC):
	if(DoesSolutionExist(matrixA)):
		answer = Inverse(matrixA) * matrixC
	else:
		answer = "Solution does not exist"
	return answer

#actually gets the contents and interacts with the user (ew, users)
#######also, it is important to note the Cailean did about 45% of this######
def main():
	run = True
	while run == True:
		equations = eval(input("Does your system have 2 or 3 linear equations?"))
		if(equations < 2 or equations > 3):
			print("Invalid number of equations")
			run = True
		else:
			run = False
		first = []
		second = []
		third = []
		constants = []
		a = Matrix(equations, equations)
		c = Matrix(equations, 1)
		if equations == 2:
			first.append(eval(input("Enter coefficient of X for first equation: ")))
			first.append(eval(input("Enter coefficient of Y for first equation: ")))
			constants.append(eval(input("Enter constant of first equation: ")))
			second.append(eval(input("Enter coefficient of X for second equation: ")))
			second.append(eval(input("Enter coefficient of Y for second equation: ")))
			constants.append(eval(input("Enter constant of second equation: ")))
			a.assignRow(0, first)
			a.assignRow(1, second)
			c.assignColumn(0, constants)
		if equations == 3:
			first.append(eval(input("Enter coefficient of X for first equation: ")))
			first.append(eval(input("Enter coefficient of Y for first equation: ")))
			first.append(eval(input("Enter coefficient of Z for first equation: ")))
			constants.append(eval(input("Enter constant of first equation: ")))
			second.append(eval(input("Enter coefficient of X for second equation: ")))
			second.append(eval(input("Enter coefficient of Y for second equation: ")))
			second.append(eval(input("Enter coefficient of Z for second equation: ")))
			constants.append(eval(input("Enter constant of second equation: ")))
			third.append(eval(input("Enter coefficient of X for third equation: ")))
			third.append(eval(input("Enter coefficient of Y for third equation: ")))
			third.append(eval(input("Enter coefficient of Z for third equation: ")))
			constants.append(eval(input("Enter constant of third equation: ")))
			a.assignRow(0, first)
			a.assignRow(1, second)
			a.assignRow(2, third)
			c.assignColumn(0, constants)
	print((SystemSolution(a,c)))
		

main()