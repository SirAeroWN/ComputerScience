#This is to be a library for vectors
#It is and will be limited
#There are better alternitives that you should probably use

class Vector:
	def __init__(self, size):
		if(validNumber(0, size)):
			if(size > 0):
				self.components = [0] * size
			else:
				print("that is not a valid size for a matrix")
		else:
			print("Size must be a number")

	def assignComp(self, index, new):
		if(index >= 0 and index < len(self.components)):
			if(new >= 0 or new < 0):
				self.components[index] = new
			else:
				print("Only numbers may be assigned to vectors")
		else:
			print("Accessed index must be in matrix")
		return

	def scalarMult(self, scalar):
		if(scalar >= 0 or scalar < 0):
			for i in range(0, len(self.components)):
				self.components[i] = self.components[i] * scalar
		else:
			print("Multiply by a number")
		return

def validNumber(typeT, number):
	if(typeT == 0):
		try:
			test = int(number)
		except:
			return False
	else:
		try:
			test = float(number)
		except:
			return False
	return True

vec = Vector(-1)
vec.assignComp(3, 78)
print(vec.components)
vec.scalarMult(3)
print(vec.components)
