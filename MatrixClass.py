class Matrix:
	def __init__(self, rows = 2, columns = 2):
		self.rows = rows
		self.columns = columns
		self.contents = []
		for i in range(0, rows): #in form matrix[rows][columns]
			self.contents.append([0] * columns)
		return

	def printit(self):
		print(self.contents)
		return

	def assignRow(self, row, contentList):
		if(len(contentList) == len(self.contents[row])):
			upper = len(self.contents[row])
			i = 0
			while(i < upper):
				self.contents[row][i] = contentList[i]
				i += 1
		else:
			print("ERROR: in assignRow: List is not same size as matrix")

	def augmentIdentity(self):
		augmented = Matrix(self.rows, (self.columns * 2))
		for i in range(0, self.rows):
			newRow = self.contents[i]
			for j in range(0, i):
				newRow.append(0)
			newRow.append(1)
			for k in range(0, (self.rows - i) - 1):
				newRow.append(0)
			augmented.assignRow(i, newRow)
		self.columns = self.columns * 2
		return augmented

	def rowMul(self, row, scalar):
		alterMatrix = self
		for i in range(0, alterMatrix.columns):
			alterMatrix.contents[row][i] = alterMatrix.contents[row][i] * scalar
		return alterMatrix

	def rowDiv(self, row, scalar):
		alteredMatrix = self
		for i in range(0, alteredMatrix.columns):
			alteredMatrix.contents[row][i] = alteredMatrix.contents[row][i] / scalar
		return alteredMatrix

	def rowAdd(self, first, second):
		alteredMatrix = self
		for i in range(0, alteredMatrix.columns):
			alteredMatrix.contents[second][i] = alteredMatrix.contents[second][i] + alteredMatrix.contents[first][i]
		return alteredMatrix

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

	def rref(self):
		#get bottom triangle of zeros
		for k in range(0, self.rows):
			for i in range(k, self.rows):
				self.rowDiv(i, self.contents[i][k])
			for j in range(k + 1, self.rows):
				self.rowCombine(-1, 1, k, j)

		#get top triangle of zeros
		for i in range(0, (self.rows) - 1):
			for j in range((i + 1), self.rows):
				if(self.contents[i][j] != 0):
					self.rowCombine((-1 * self.contents[i][j]), 1, j, i)
		return

	def stripFront(self):
		stripped = Matrix(self.rows, int(self.columns / 2))
		for i in range(0, self.rows):
			k = 0
			for j in range(self.rows, self.columns):
				stripped.contents[i][k] = float(format(self.contents[i][j], ".4f"))
				k += 1
		self.contents = stripped.contents
		return

	def Inverse(matrix):
		inverted = matrix
		inverted.augmentIdentity()
		inverted.rref()
		inverted.stripFront()
		return inverted

	def SystemSolution(matrixA, matrixC):
		matrixB = Inverse(matrixA) * matrixC
		return matrixB