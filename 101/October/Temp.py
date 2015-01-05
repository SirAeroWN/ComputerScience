def makeMatrix(rows, columns):
	matrix = []
	for i in range(0, rows):
		newRow = [0] * columns
		matrix.append(newRow)
	return matrix

u = makeMatrix(3,4)
print (u)