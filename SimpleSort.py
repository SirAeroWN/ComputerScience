def displaySortedNumbers(num1, num2, num3):
    first = num1
    second = num2
    third = num3

    if(num2 < num1 and num2 < num3):
        first = num2
    elif(num3 < num1 and num3 < num2):
        first = num3

    if((num1 < num2 and num1 > num3) or (num1 > num2 and num1 < num3)):
        second = num1
    elif((num3 < num2 and num3 > num1) or (num3 > num2 and num3 < num1)):
        second = num3

    if(num1 > num2 and num1 > num3):
        third = num1
    elif(num2 > num1 and num2 > num3):
        third = num2

    print("The sorted numbers are", first, second, third)
    return

firstUser, secondUser, thirdUser = eval(input("Enter three numbers seperated by commas: "))
displaySortedNumbers(firstUser, secondUser, thirdUser)
