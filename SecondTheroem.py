from matplotlib.pylab import *

def f(x):
	return (x**2)

a = 0
b = 2
n = 100
dx = (b - a) / float(n - 1)
x = linspace(a, b, n)
y = f(x)
yp = dx * y
print(yp)
dy = x * y

plot(x,y)
plot(x, dy, 'r--o')
xlabel('x')
ylabel('y')
legend(['f(x) = x^2', 'integral f(x) = (x^3)/3'])

axis([-2,2,-2,2])
title('Function and integral')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)

show()