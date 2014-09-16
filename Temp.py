def sumMyInt(endNum):
    MyNum = 0
    for i in range(1, endNum + 1):
        MyNum += i
    return MyNum

userNum = eval(input("Give me an integer, please: "))
print("I done addeded some numbers, and this is what I gots: " + str(sumMyInt(userNum)))
