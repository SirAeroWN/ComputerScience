import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def f(x):
	return 2 - x**2

def root(Xn1, Xn2):
	Xn = Xn1 - (f(Xn1) * ((Xn1 - Xn2)/(f(Xn1) - f(Xn2))))
	return Xn

def lineEQ(x1, x0, x):
	return ((f(x0) - f(x1))/(x0 - x1))*(x - x0) + f(x0)

def secantRootMethod(x0, x1, c, x):
	plt.plot(x, lineEQ(x0, x1, x))
	if c <= 5:
		secantRootMethod(x1, root(x0, x1), c + 1, x)
	else:
		print(root(x0, x1))
	return

figure, ax = plt.subplots()
plt.subplots_adjust(left = 0.25, bottom = 0.25)
x = np.linspace(-4.0, 4.0, 100000) # 100,000 x's
y = f(x)
x0 = 1
x1 = 2
original, = plt.plot(x,y)
secantRootMethod(x0, x1, 0, x)
plt.axis([-4, 4, np.amin(y) - 1, np.amax(y) + 1])
plt.grid(True)
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.show()