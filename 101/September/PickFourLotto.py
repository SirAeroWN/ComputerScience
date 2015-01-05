import random

firstDig = str(random.randint(0,9))
secondDig = str(random.randint(0,9))
thirdDig = str(random.randint(0,9))
fourthDig = str(random.randint(0,9))

winner = firstDig + secondDig + thirdDig + fourthDig
print(winner)
guess = input("Guess the four digit lotto number: ")

while(True):
    guess = input("You lose, guess again: ")
    if(guess == 'q'):
        print("Thank you for playing")
        break
    if(guess == winner):
        print("You won!")
        break
