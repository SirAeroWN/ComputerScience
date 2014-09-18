#This is supposed to be an IDLE style conversation bot

import random
import webotlists

def badMouth(theInput):
    for cuss in webotlists.swearwords:
        if(theInput == cuss):
            print("Now don't get angry")
    return

def respond():
    rand = random.randint(1, 2)
    if(rand == 1):
        print("Fly like a beaver")
    elif(rand == 2):
        print("Give me all your money")
        return

def main():
    userInput = input("> ")
    while(userInput != "#QUIT"):
        userInput = input("> ")
        badMouth(userInput)
        respond()

main()
