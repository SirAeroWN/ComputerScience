#A simple class for rectangles

class Rectangle:
	"""simple rectangle class that can return area and perimeter"""
	def __init__(self, width = 1, height = 2):
		self.__width = width
		self.__height = height

	def getWidth(self):
		return self.__width

	def setWidth(self, newWidth):
		self.__width = newWidth

	def getHeight(self):
		return self.__height

	def setHeight(self, newHeight):
		self.__height = newHeight

	def getArea(self):
		return (self.__height * self.__width)

	def getPerimeter(self):
		return ((2 * self.__height) + (2 * self.__width))

def main():
	babysFirstRectangle = Rectangle(4, 40)
	myFirstRectangle = Rectangle(3.5, 35.7)
	print("width:", babysFirstRectangle.getWidth(), "height:", babysFirstRectangle.getHeight(), "area:", babysFirstRectangle.getArea(), "perimeter:", babysFirstRectangle.getPerimeter())
	print("width:", myFirstRectangle.getWidth(), "height:", myFirstRectangle.getHeight(), "area:", myFirstRectangle.getArea(), "perimeter:", myFirstRectangle.getPerimeter())

main()