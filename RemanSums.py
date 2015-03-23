from matplotlib.pylab import *

def f(x):
	return (x**2) / 2

a = -2
b = 2
n = 51
dx = (b - a) / float(n - 1)
x = linspace(a, b, n)
y = f(x)
dy = dx * y

plot(x,y)
plot(x, dy, 'r--o')
xlabel('x')
ylabel('y')
legend(['f(x) = (x^2)/2', 'integral f(x) = (x^3)/6'])

axis([-2,2,-2,2])
title('Function and integral')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)

show()