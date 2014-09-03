#completes problem 4.1, solve quadratic equation
#import math module for square root
import math

#get input, nondescriptive names because that's what they are
a, b, c = eval(input("Enter a, b, c: "))

#calculate discriminent before the whole thing, might no have to do it all
discriminant = b**2 - (4 * a * c)

#check to see if nonzero and nonnegative, if either stop and return fixed answer
if(discriminant > 0):
	rootOne = (-b + (math.sqrt(discriminant))) / (2 * a)
	rootTwo = (-b - (math.sqrt(discriminant))) / (2 * a)
	answer = "The roots are " + str(rootOne) + " and " + str(rootTwo)
	print(answer)
elif(discriminant == 0):
	print("The root is -1")
else:
	print("The equation has no roots")
