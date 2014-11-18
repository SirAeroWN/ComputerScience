from tkinter import *
from tkinter import messagebox
import random

def choosecard1():
    card1Num = random.randint(1,52)
    if(card1Num % 13 == 0):
        card1Val.set(13)
    else:
        card1Val.set(card1Num)
    cardtop1["file"] = 'image/card/' + str(card1Num) + '.gif'
    card1button["image"] = cardtop1
    card1button["command"] = doNothing
    return

def choosecard2():
    card2Num = random.randint(1,52)
    if(card2Num % 13 == 0):
        card2Val.set(13)
    else:
        card2Val.set(card2Num)
    cardtop2["file"] = 'image/card/' + str(card2Num) + '.gif'
    card2button["image"] = cardtop2
    card2button["command"] = doNothing
    if(hi.get() == 1 and card1Val.get() < card2Val.get()):
        messagebox.showinfo("Winner", "You Won!")
    elif(hi.get() == 2 and card1Val.get() > card2Val.get()):
        messagebox.showinfo("Winner", "You Won!")
    else:
        messagebox.showinfo("Loser", "You Lost")
    reset.grid(row = 2, column = 1, columnspan = 2)
    return

def newdeal():
    cardtop1["file"] = "image/card/b1fv.gif"
    cardtop2["file"] = "image/card/b1fv.gif"
    card1button["command"] = choosecard1
    card2button["command"] = choosecard2
    hi.set(0)
    reset.grid_remove()
    return

def doNothing():
    return

def ready():
    card2button["command"] = choosecard2
    return

window = Tk()
window.geometry("300x300")

cardtop1 = PhotoImage(file = "image/card/b1fv.gif")
card1button = Button(window, image = cardtop1, command = choosecard1)
card1button.grid(row = 1, column = 1)
cardtop2 = PhotoImage(file = "image/card/b1fv.gif")
card2button = Button(window, image = cardtop2, command = doNothing)
card2button.grid(row = 1, column = 2)
hi = IntVar()
hi.set(0)
card1Val = IntVar()
card1Val.set(1)
card2Val = IntVar()
card2Val.set(1)
hiRdo = Radiobutton(window, text = "Hi", variable = hi, value = 1, command = ready)
hiRdo.grid(row = 1, column = 3)
loRdo = Radiobutton(window, text = "Low", variable = hi, value = 2, command = ready)
loRdo.grid(row = 1, column = 4)

reset = Button(window, text = "Draw", command = newdeal)

window.mainloop()