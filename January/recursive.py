import time

def foo(num):
	if num != 0:
		x = num * foo(num - 1)
		return x
	return 1

def gcd(m, n):
	val = m % n
	if val != 0:
		n = gcd(m, m % n)
	return n

print(gcd(16, 12))