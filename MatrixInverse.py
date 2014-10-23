from MatrixClass import Matrix

# a = Matrix()
# a.assignRow(0, [4,3])
# a.assignRow(1, [3,2])
# a.augmentIdentity()
# a.rref()
# a.printit()

b = Matrix(3, 3)
b.assignRow(0, [1,4,-3])
b.assignRow(1, [-2,-7,6])
b.assignRow(2, [1,7,-2])
b.Inverse()
b.printit()