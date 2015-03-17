from numpy import *
import numpy as np

a = np.arange(1, 21, 1, dtype=int_)
print(a)

b = np.array(a + a)
print(b)

c = np.array(a**2)
print(c)

d = np.array(b + c)
print(d)