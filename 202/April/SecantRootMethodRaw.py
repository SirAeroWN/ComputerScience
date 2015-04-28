# import libraries and such
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



class stuffs:
	def __init__(self):
		window = Tk()
		self.x0 = IntVar()
		self.x0.set(2)
		self.x1 = IntVar()
		self.x1.set(1)		
		Label(window, text = 'Left Integer Boundary:').grid(row = 1, column = 1)
		Label(window, text = 'Right Integer Boundary:').grid(row = 2, column = 1)
		Entry(window, textvariable = self.x0).grid(row = 1, column = 2)
		Entry(window, textvariable = self.x1).grid(row = 2, column = 2)
		Button(window, text = 'Graph!', command = self.graphIt).grid(row = 3, column = 1, columnspan = 2)
		window.mainloop()
		return

	def graphIt(self):
		# now for the meat
		figure, ax = plt.subplots() # make subplot
		plt.subplots_adjust(left = 0.25, bottom = 0.25) # put it in a pretty place
		x = np.linspace(-4.0, 4.0, 1000) # 1,000 x's
		y = self.f(x) # for original line
		axcolor = 'lightgoldenrodyellow' # pretty color
		ax.plot(x,y) # graph the original line
		ax.axis([-4, 4, np.amin(y) - 1, np.amax(y) + 1]) # set axis to accomaodate ys and between -4 & 4 xs
		ax.grid(True) # want a grid
		ax.axhline(0, color='black', lw=2) # put an x axis in there
		ax.axvline(0, color='black', lw=2) # put a y axis in there
		self.secant, = ax.plot(x, self.lineEQ(self.x0.get(), self.x1.get(), x)) # plot first secant, name it so it can be redrawn
		self.secantRootMethod(self.x0.get(), self.root(self.x0.get(), self.x1.get()), 1, x)
		plt.show()
		return

	# returns the equation, essentially y vals
	def f(self, x):
		return 2 - x**2

	# uses equation from mr howard to find the root of the line between two points (the secant line)
	def root(self, Xn1, Xn2): # only pass x vals because ys can be gotten with f(x)
		Xn = Xn1 - (self.f(Xn1) * ((Xn1 - Xn2)/(self.f(Xn1) - self.f(Xn2))))
		return Xn

	# used to return y vals for a line between two points - point slope formula
	def lineEQ(self, x1, x0, x):
		return ((self.f(x0) - self.f(x1))/(x0 - x1))*(x - x0) + self.f(x0)

	# recursively redraws secant line 6 times to get accurate root
	def secantRootMethod(self, x0, x1, c, x):
		self.secant.set_ydata(self.lineEQ(x0, x1, x)) # redraw with found points
		if c <= 5: # do 6 times
			self.secantRootMethod(x1, self.root(x0, x1), c + 1, x) # call again
		return

stuffs()