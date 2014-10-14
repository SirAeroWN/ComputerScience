class Complex:
	def __init__(self, realParam = 0, imagParam = 0):
		self.__real = realParam
		self.__imag = imagParam
		return

	def getReal(self):
		return self.__real

	def getImag(self):
		return self.__imag

	def setReal(self, newReal):
		self.__real = newReal
		return

	def setImag(self, newImag):
		self.__imag = newImag
		return

	def __str__(self):
		return str(str(self.__real) + ' + ' + str(self.__imag) + 'i')

	def __add__(self, other):
		newComplex = Complex((self.__real + other.getReal()), (self.__imag + other.getImag()))
		return newComplex

	def __mul__(self, other):
		newComplex = Complex(((self.__real * other.getReal()) - (self.__imag * other.getImag())), ((self.__imag * other.getReal()) + (self.__real * other.getImag())))
		return newComplex

z = Complex(10, 20)
print(z)
w = Complex(1, 2)
print(w)
y = w * z
print(y)