from matplotlib.pylab import *

def f(x):
	return (2 / (pi**0.5)) * exp(-1  * x**2)

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

for i in range(0, n):
	y[i] = RHS(0, x[i])

plot(x,y)
xlabel('x')
ylabel('y')
legend(['antiderivative of f(x) = 2/sqrt(pi) e^-t^2'])

axis([-2,2,-2,2])
title('Function and integral')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)

show()