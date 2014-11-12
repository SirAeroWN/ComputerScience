from tkinter import *

def validateinfo():
    #validate SSN
    #Reassign widgets to the frame
    entryname.destroy(), entryssn.destroy(), submit.destroy()
    labelname.grid_remove() #just to demonstrate the remove guy
    labelssn.grid_remove()
    labelname['text'] = name.get() + "'s Quiz"
    labelssn['text'] = 'ID Number: '+ ssn.get()
    labelname.grid(row = 1, column = 1)
    labelssn.grid(row = 2, column = 1)
    question.grid(row = 1, column = 1, sticky = W)
    radioA.grid(row = 2, column = 1,sticky = W)
    radioB.grid(row = 3, column = 1,sticky = W)
    radioC.grid(row = 4, column = 1,sticky = W)
    nextbutton.grid(row = 5, column = 1, columnspan = 2)
    return

def questionHandler():
    global currentquestion
    global responses
    answers = [1,1,2,3]
    if(selection.get() == answers[currentquestion]):
        responses += 1
    currentquestion += 1
    selection.set(0) #to uncheck a radio button
    if(currentquestion < (len(questions) - 1)):
        question['text'] = questions[currentquestion]
        radioA['text'] = possibleanswers[currentquestion * 3]
        radioB['text'] = possibleanswers[currentquestion * 3 + 1]
        radioC['text'] = possibleanswers[currentquestion * 3 + 2]
    else:
        if(selection.get() == answers[currentquestion]):
            responses += 1
        question['text'] = questions[currentquestion]
        radioA['text'] = possibleanswers[currentquestion * 3]
        radioB['text'] = possibleanswers[currentquestion * 3 + 1]
        radioC['text'] = possibleanswers[currentquestion * 3 + 2]
        global nextbutton
        nextbutton.destroy()
        signBtn = Button(framequestions, text = "Sign Pledge", command = signThatPledge).grid(row = 5, column = 1)
    return

def signThatPledge():
    global responses
    if(selection.get() == 3):
            responses += 1
    global pledgeFrame
    pledgeFrame = Frame(window)
    framequestions.destroy()
    pledgeFrame.pack()
    global checked
    checked = IntVar()
    checked.set(0)
    agreed = Checkbutton(pledgeFrame, text = "I, " + name.get() + ", did not give or accept unauthorized assistance on this quiz", variable = checked).pack()
    scoreItBtn = Button(pledgeFrame, text = "Click for Score", command = score).pack()
    return

def score():
    global pledgeFrame
    global checked
    pledgeFrame.destroy()
    finalScore = 0
    if(checked.get() == 1):
        finalScore = responses / 4
    grade = "Your grade is a " + str(finalScore * 100) + "%"
    messagebox.showinfo("Grade", grade)
    window.destroy()
    return
    
questions = ['What is your favorite color?', 'Is it cold outside?', "Are roses red?", "Are violets blue?"]
possibleanswers = ['Red','Blue','Green', 'Yes', 'No', "I haven't been outside", "Heck if I know", "Duh", "No", "No, they're violet", "Not if you're a dog", "Who cares? No one loves me anyway"]
currentquestion = 0
responses = 0
window = Tk()
#pledgeWindow = Tk()

frameheader = Frame(window)
framequestions = Frame(window)
frameresults = Frame(window)
frameheader.pack()
framequestions.pack()
frameresults.pack()

# Create and grid widgets for header frame
name = StringVar()
name.set('')
entryname = Entry(frameheader, textvariable = name)
ssn = StringVar()
ssn.set('')
entryssn = Entry(frameheader, textvariable = ssn)
labelname = Label(frameheader, text = 'Enter name: ')
labelssn = Label(frameheader, text = 'Enter Social Security #: ')
submit = Button(frameheader, text = 'Submit info ', command = validateinfo)

labelname.grid(row = 1, column = 1)
entryname.grid(row = 1, column = 2)
labelssn.grid(row = 2, column = 1)
entryssn.grid(row = 2, column = 2)
submit.grid(row = 3, column = 1, columnspan = 2)


#Create and grid widgets for question frame
question = Label(framequestions, text = questions[currentquestion])
selection = IntVar()
selection.set(0)
radioA = Radiobutton(framequestions, text = possibleanswers[currentquestion * 3], variable = selection, value = 1)
radioB = Radiobutton(framequestions, text = possibleanswers[currentquestion * 3 + 1] , variable = selection, value = 2)
radioC = Radiobutton(framequestions, text = possibleanswers[currentquestion * 3 + 2], variable = selection, value = 3)
nextbutton = Button(framequestions, text = 'Next', command = questionHandler)

window.mainloop()
