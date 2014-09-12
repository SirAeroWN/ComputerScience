#copletes problem 4.3, solving a 2 x 2 linear equation

#get input
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

#now make sure there is a solution and then compute it
denom = (a * d) - (b * c)
if(denom == 0):
	print("The equation has no solution")
else:
	x = (e * d - b * f) / denom
	y = (a * f - e * c) / denom
	answer = "x is " + format(x, ".1f") + " and y is " + format(y, ".1f")
	print(answer)