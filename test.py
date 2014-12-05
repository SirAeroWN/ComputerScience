from tkinter import *

window = Tk()
foo = PhotoImage(file = 'image/redChecker.gif')
canvas = Canvas(window, width = 500, height = 500, bg = 'black')
canvas.create_image(250, 250, image = foo)
canvas.pack()
window.mainloop()