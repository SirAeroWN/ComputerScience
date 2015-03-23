from matplotlib.pylab import *

def foo(x):
	return (x**2)/2

a = -2
b = 2
n = 51


x = linspace(a, b, n)
y = foo(x)

plot(x,y)

xlabel('x')
ylabel('y')
legend(['f(x) = x^2/2'])
axis([-2,2,-2,2])
title('Function Graph')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)
show()