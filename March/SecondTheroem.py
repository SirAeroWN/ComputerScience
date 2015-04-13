from matplotlib.pylab import *

def f(x):
	return (x**2)

def RHS(a, b):
	n = 100
	dx = (b - a) / float(n - 1)
	x = linspace(a, b, n)
	y = f(x)
	yp = dx * y
	return yp.sum()

a = -2
b = 2
n = 100
x = linspace(a, b, n)
y = zeros(100)

for i in range(1, n):
	y[i] = RHS(0, x[i])

plot(x,y)
xlabel('x')
ylabel('y')
legend(['f(x) = x^2', 'integral f(x) = (x^3)/3'])

axis([-2,2,-2,2])
title('Function and integral')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)

show()