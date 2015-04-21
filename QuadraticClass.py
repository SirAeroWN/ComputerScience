class Quad:
	def __init__(self, a, b, c):
		self.__a = eval(str(a))
		self.__b = eval(str(b))
		self.__c = eval(str(c))
		self.__roots = self.findRoots()
		return

	def __str__(self):
		string = str(a) + 'x^2'

	def seta(self, a):
		self.__a = a
		self.__roots = self.findRoots()
		return

	def setb(self, b):
		self.__b = b
		self.__roots = self.findRoots()
		return

	def setc(self, c):
		self.__c = c
		self.__roots = self.findRoots()
		return

	def geta(self):
		return a

	def getb(self):
		return b

	def getc(self):
		return c

	def getRoots(self):
		return self.__roots

	def findRoots(self):
		desc = self.simplify(self.__b**2 - (4 * self.__a * self.__c))
		first = -1 * self.__b
		den = 2 * self.__a
		final = self.stringify(self.reduction(first, desc, den))
		return final

	def simplify(self, number):
		self.inside = number
		listReturn = [1,'r',1]
		if self.inside == 0:
			return [0, 'r', 0]
		elif self.inside < 0:
			listReturn[1] = 'i'
			self.inside = self.inside * -1
			number = number * -1
		out = self.simplifyHelper(number, 2)
		listReturn[0] = out
		listReturn[2] = self.inside
		return listReturn

	def simplifyHelper(self, number, devisor):
		if devisor > 50:
			self.inside = number
			return 1
		outside = 1
		if (number % devisor**2) == 0:
			outside = devisor
			number = number // devisor**2
			return outside * self.simplifyHelper(number, devisor)
		else:
			return outside * self.simplifyHelper(number, devisor + 1)

	def stringify(self, info):
		bTerm = info[0]
		disc = info[1]
		denom = info[2]
		first = str(bTerm)
		second = self.discString(disc)
		if denom != 1:
			third = '\n' + '-' * len(first + second + ' + ') + '\n'
			fourth = ' ' * (len(first + second + ' + ') // 2) + str(denom)
			back = second + third + fourth
		else:
			back = second
		if second == '':
			x = first + back
		else:
			x = first + ' ' + "\u00B1" + ' ' + back
		return x

	def discString(self, discList):
		if discList[0] == 0 or discList[2] == 0:
			return ''
		string = ''
		if discList[0] == 1:
			string += ''
		else:
			string += str(discList[0])
		if discList[1] == 'i':
			string += 'i'
		if discList[2] == 1 and discList[0]  == 1:
			string += '1'
		elif discList[2] == 1 and discList[0] != 1:
			string += ''
		else:
			string += 'sqrt(' + str(discList[2]) + ')'
		return string

	def reduction(self, bTerm, discriminant, denominator):
		for i in range(denominator, 1, -1):
			if (bTerm % i == 0) and (discriminant[0] % i == 0) and (denominator % i == 0):
				bTerm = bTerm // i
				discriminant[0] = discriminant[0] // i
				denominator = denominator // i
		return bTerm, discriminant, denominator

test = Quad(1, 4, -5)
print(test.getRoots())