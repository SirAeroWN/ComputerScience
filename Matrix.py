#this is to test, expirament, and maybe implement a method of interacting with matrices
#0,0 is in the top right corner

#define global variables so all methods can access and change them
x = 0
y = 0

def printMatrix(Matrix):
    for i in range(0, x):
        print('[', end = ' ')
        for j in range(0, y):
            print(str(Matrix[i][j]), end = ' ')
        print(']')

def populMatrix(Matrix):
    for i in range(0, x):
        row = "\nFor the " + str((i + 1)) + " row:"
        print(row)
        for j in range(0, y):
            column = "For the " + str((j + 1)) + " column:"
            print(column, end = '')
            Matrix[i][j] = eval(input(' '))

def scalarMultMatrix(a, Matrix):
    for i in range(0, x):
        for j in range(0, y):
            Matrix[i][j] = Matrix[i][j] * a

#ask the user to describe the matrix eg m X n
x, y = eval(input("Please enter the matrix dimensions: "))

#for some reason it won't allow anything besides a square matrix
#the list will be "square" which means data might be accedentally added
#in areas that won't be used, just means to be careful

maxSize = 0
if(x != y):
    if(x > y):
        maxSize = x
    else:
        maxSize = y
else:
    maxSize = x

#set the matrix to the requested size, don't add one because of range() funkyness, there is a 0,0
matrix = [[0 for s in range(maxSize)] for s in range(maxSize)]

#get values for matrix
populMatrix(matrix)

#get a scalar to multiply the matrix by and then multiply
scalar = eval(input("Enter a scalar for multiplication: "))
scalarMultMatrix(scalar, matrix)

#now show them your matrix
printMatrix(matrix)

