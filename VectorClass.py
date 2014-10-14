#simple vector class

class Vector:
	def __init__(self, xVal = 0, yVal = 0):
		self.__x = xVal
		self.__y = yVal
		return

	def __add__(self, other):
		return Vector((self.__x + other.getX()), (self.__y + other.getY()))

	def __sub__(self, other):
		return Vector((self.__x - other.getX()), (self.__y - other.getY()))

	def __mul__(self, other):
		return ((self.__x * other.getX()) + (self.__y * other.getY()))

	def __str__(self):
		return str('<' + str(self.__x) + ',' + str(self.__y) + '>')

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def setX(self, newX):
		self.__x = newX
		return

	def setY(self, newY):
		self.__y = newY
		return

u = Vector(3,4)
print(u)
v = Vector(1,2)
print(v)
print(u + v)
print(u - v)
print(u * v)