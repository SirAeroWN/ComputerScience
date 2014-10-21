class Matrix:
	def __init__(self, rows, columns):
		self.__contents = []
		width = [0] * columns
		for i in range(0, rows):
			self.__contents.append(width)