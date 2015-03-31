from matplotlib.pylab import *

def f(x):
    return (x**2)/2

a = -2  #left endpoint
b = 2   #right endpoint
n = 51  #number of subintervals + 1
dx = (b-a)/float(n-1)   #delta x
x = linspace(a, b, n)   #generate array of x values on the specified interval
y = f(x)                #generate array of y values using function
yp = diff(y)/dx         #diff computes difference between each y value.  Scalar division by dx computed derivative approx
subplot(2,1,1)          #Create subplot ... 2 rows, 1 column, place in window 1
plot(x,y)               #Plot graph

xlabel('x')
ylabel('f(x)')
legend(['f(x) = x^2/2'])
axis([-2,2,-2,2])
title('Function')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)

subplot(2,1,2)          #Create subplot ... 2 rows, 1 column, place in window 2
plot(x[:-1], yp, 'r-')  #Plot yp (derivative), as red lines.  There will be one less number in this array, hence the need for x[:-1]
xlabel('x')
ylabel('f\'(x)')
legend(['f\'(x) = x'])
axis([-2,2,-2,2])
title('Derivative')
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)

show()
