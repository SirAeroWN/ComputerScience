from ListStructures import Stack
from tkinter import *

class calc(Stack):
	def __init__(self):
		super().__init__()
		self.displayVal = '0'
		self.new = True
		self.memory = '0'
		root = Tk()
		root.title("RPN")
		img = PhotoImage(file = 'image/china.gif')
		root.tk.call('wm', 'iconphoto', root._w, img)
		self.display = Label(root, text = self.displayVal)
		self.display.grid(row = 1, columnspan = 4)
		Button(root, text = 'Enter', command = self.enter).grid(row = 2, column = 1)
		Button(root, text = 'Clear', command = self.clearall).grid(row = 2, column = 2)
		Button(root, text = 'Store', command = self.inMem).grid(row = 2, column = 3)
		Button(root, text = 'Mem', command = self.outMem).grid(row = 2, column = 4)
		Button(root, text = '   *   ', command = self.multiply).grid(row = 3, column = 1)
		Button(root, text = '   /   ', command = self.divide).grid(row = 4, column = 1)
		Button(root, text = '  +   ', command = self.add).grid(row = 5, column = 1)
		Button(root, text = '   -   ', command = self.subtract).grid(row = 6, column = 1)
		Button(root, text = '   7   ', command = self.seven).grid(row = 3, column = 2)
		Button(root, text = '   8   ', command = self.eight).grid(row = 3, column = 3)
		Button(root, text = '   9   ', command = self.nine).grid(row = 3, column = 4)
		Button(root, text = '   4   ', command = self.four).grid(row = 4, column = 2)
		Button(root, text = '   5   ', command = self.five).grid(row = 4, column = 3)
		Button(root, text = '   6   ', command = self.six).grid(row = 4, column = 4)
		Button(root, text = '   1   ', command = self.one).grid(row = 5, column = 2)
		Button(root, text = '   2   ', command = self.two).grid(row = 5, column = 3)
		Button(root, text = '   3   ', command = self.three).grid(row = 5, column = 4)
		Button(root, text = '  del ', command = self.delete).grid(row = 6, column = 4)
		Button(root, text = '    .   ', command = self.dot).grid(row = 6, column = 3)
		Button(root, text = '   0   ', command = self.zero).grid(row = 6, column = 2)
		root.mainloop()
		return

	def one(self):
		self.changeDisplay('1')
		return

	def two(self):
		self.changeDisplay('2')
		return
		
	def three(self):
		self.changeDisplay('3')
		return
		
	def four(self):
		self.changeDisplay('4')
		return
		
	def five(self):
		self.changeDisplay('5')
		return
		
	def six(self):
		self.changeDisplay('6')
		return
		
	def seven(self):
		self.changeDisplay('7')
		return

	def eight(self):
		self.changeDisplay('8')
		return
		
	def nine(self):
		self.changeDisplay('9')
		return
		
	def zero(self):
		self.changeDisplay('0')
		return
		
	def dot(self):
		if self.new:
			self.changeDisplay('0.')
		elif '.' in self.displayVal:
			doNothing = True
		else:
			self.changeDisplay('.')
		return
		
	def delete(self):
		self.new = True
		self.changeDisplay('0')
		self.new = True
		return

	def enter(self):
		if self.new == False:
			floatBool = True
			localDisplayVal = self.displayVal
			if localDisplayVal[len(localDisplayVal) - 1] == '.':
				localDisplayVal = localDisplayVal + '0'
			elif '.' not in localDisplayVal:
				floatBool = False
			if floatBool:
				valToPush = float(localDisplayVal)
			else:
				valToPush = int(localDisplayVal)
			self.push(valToPush)
			self.new = True
		return

	def changeDisplay(self, num):
		if self.new:
			self.displayVal = num
		else:
			self.displayVal = self.displayVal + num
		self.display['text'] = self.displayVal
		self.new = False
		return

	def clearall(self):
		for node in range(self.size - 1):
			self.pop()
		self.changeDisplay('0')
		self.new = True
		return

	def inMem(self):
		self.memory = self.displayVal
		return

	def outMem(self):
		self.displayVal = self.memory
		self.display['text'] = self.displayVal
		return

	def multiply(self):
		self.enter()
		try:
			num1 = self.pop()
			num2 = self.pop()
			newVal = num1 * num2
			self.push(newVal)
			self.changeDisplay(str(newVal))
		except:
			self.changeDisplay('ERROR: TOO FEW ARGUMENTS')
			self.clearall()
		self.new = True
		return

	def divide(self):
		self.enter()
		try:
			num1 = self.pop()
			num2 = self.pop()
			newVal = num1 / num2
			self.push(newVal)
			self.changeDisplay(str(newVal))
		except:
			self.changeDisplay('ERROR: TOO FEW ARGUMENTS')
			self.clearall()
		self.new = True
		return

	def add(self):
		self.enter()
		try:
			num1 = self.pop()
			num2 = self.pop()
			newVal = num1 + num2
			self.push(newVal)
			self.changeDisplay(str(newVal))
		except:
			self.changeDisplay('ERROR: TOO FEW ARGUMENTS')
			self.clearall()
		self.new = True
		return

	def subtract(self):
		self.enter()
		try:
			num1 = self.pop()
			num2 = self.pop()
			newVal = num1 - num2
			self.push(newVal)
			self.changeDisplay(str(newVal))
		except:
			self.changeDisplay('ERROR: TOO FEW ARGUMENTS')
			self.clearall()
		self.new = True
		return

pole = calc()