class Complex:
	def __init__(self, realParam = 0, imagParam = 0):
		self.__real = realParam
		self.__imag = imagParam
		return

	def getRealPart(self):
		return self.__real

	def getImaginaryPart(self):
		return self.__imag

	def setReal(self, newReal):
		self.__real = newReal
		return

	def setImag(self, newImag):
		self.__imag = newImag
		return

	def __add__(self, other):
		newComplex = Complex((self.__real + other.getRealPart()), (self.__imag + other.getImaginaryPart()))
		return newComplex

	def __sub__(self, other):
		newComplex = Complex((self.__real - other.getRealPart()), (self.__imag - other.getImaginaryPart()))
		return newComplex

	def __mul__(self, other):
		newComplex = Complex(((self.__real * other.getRealPart()) - (self.__imag * other.getImaginaryPart())), ((self.__imag * other.getRealPart()) + (self.__real * other.getImaginaryPart())))
		return newComplex

	def __truediv__(self, other):
		newComplex = Complex(((self.__real * other.getRealPart() + self.__imag * other.getImaginaryPart()) / (other.getRealPart()**2 + other.getImaginaryPart()**2)), ((self.__imag * other.getRealPart() - self.__real * other.getImaginaryPart()) / (other.getRealPart()**2 + other.getImaginaryPart()**2)))
		return newComplex

	def __abs__(self):
		absolute = ((self.__real**2 + self.__imag**2)**(0.5))
		return absolute

	def __str__(self):
		fancy = "(" + str(self.getRealPart()) + " + " + str(self.getImaginaryPart()) + "i)"
		return fancy

z = Complex(10, 20)
print(z)
w = Complex(1, 2)
print(w)
y = w * z
print(y)
y = w - z
print(y)
y = w + z
print(y)
y = w / z
print(y)
print(abs(z))
