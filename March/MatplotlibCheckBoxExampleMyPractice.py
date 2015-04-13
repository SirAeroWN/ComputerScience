import numpy as np
import matplotlib.pylab as plb
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

def f(x):
	return x**2

a = -5
b = 5
n = 501
x = np.linspace(a, b, n)
dx = (b-a) / float(n - 1)
y = f(x)
yPrime = plb.diff(y) / dx

fig, ax = plt.subplots()
g0, = ax.plot(x, y, lw=2)
g1, = ax.plot(x[:-1], yPrime, visible=False, lw=2)
plt.subplots_adjust(left=0.2)

rax = plt.axes([0.05, 0.42, 0.1, 0.15])
check = CheckButtons(rax, ('f(x)', 'f\'(x)'), (True, False))

def func(label):
    if label == 'f(x)': g0.set_visible(not g0.get_visible())
    elif label == 'f\'(x)': g1.set_visible(not g1.get_visible())
    plt.draw()
check.on_clicked(func)

plt.show()
