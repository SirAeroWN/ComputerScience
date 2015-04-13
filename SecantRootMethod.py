# import libraries and such
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# returns the equation, essentially y vals
def f(x):
	return 2 - x**2

# uses equation from mr howard to find the root of the line between two points (the secant line)
def root(Xn1, Xn2): # only pass x vals because ys can be gotten with f(x)
	Xn = Xn1 - (f(Xn1) * ((Xn1 - Xn2)/(f(Xn1) - f(Xn2))))
	return Xn

# used to return y vals for a line between two points - point slope formula
def lineEQ(x1, x0, x):
	return ((f(x0) - f(x1))/(x0 - x1))*(x - x0) + f(x0)

# recursively redraws secant line 6 times to get accurate root
def secantRootMethod(x0, x1, c, x):
	secant.set_ydata(lineEQ(x0, x1, x)) # redraw with found points
	if c <= 5: # do 6 times
		secantRootMethod(x1, root(x0, x1), c + 1, x) # call again
	else:
		print(root(x0, x1)) # at end of recursion, print root
	return

# slider has changed so update secant
def update(val):
	secantRootMethod(leftSlider.val, rightSlider.val, 0, np.linspace(-4.0, 4.0, 1000))
	figure.canvas.draw_idle()
	return

# now for the meat
figure, ax = plt.subplots() # make subplot
plt.subplots_adjust(left = 0.25, bottom = 0.25) # put it in a pretty place
x = np.linspace(-4.0, 4.0, 1000) # 1,000 x's
y = f(x) # for original line
axcolor = 'lightgoldenrodyellow' # pretty color
ax.plot(x,y) # graph the original line
ax.axis([-4, 4, np.amin(y) - 1, np.amax(y) + 1]) # set axis to accomaodate ys and between -4 & 4 xs
ax.grid(True) # want a grid
ax.axhline(0, color='black', lw=2) # put an x axis in there
ax.axvline(0, color='black', lw=2) # put a y axis in there
x0ax = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor) # make left slider space
x1ax  = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor) # make right slider space
leftSlider = Slider(x0ax, 'Left Boundry', -3, 3, valinit = 1) # actually make left slider
rightSlider = Slider(x1ax, 'Right Boundry', -3, 3, valinit = 2) # actually make right slider
secant, = ax.plot(x, lineEQ(leftSlider.val, rightSlider.val, x)) # plot first secant, name it so it can be redrawn

# when sliders change update secant
leftSlider.on_changed(update)
rightSlider.on_changed(update)
plt.show()