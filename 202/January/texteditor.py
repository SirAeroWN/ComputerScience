from tkinter import *
from tkinter import filedialog
from random import randint

class FileEditor:
    
    def __init__(self):
        self.window=Tk()
        self.window.title('Simple Text Editor')

        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'File', menu = operationMenu)
        operationMenu.add_command(label = 'New')
        operationMenu.add_command(label = 'Open', command = self.openFile)
        operationMenu.add_command(label = 'Open Encrypted File', command = self.openEFile)
        operationMenu.add_command(label = 'Save', command = self.saveFile)
        operationMenu.add_command(label = 'Save As Encrypted', command = self.saveEFile)
        operationMenu.add_separator()
        operationMenu.add_command(label = 'Exit', command = self.exitEditor)

        helpMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'Help', menu = helpMenu)
        helpMenu.add_command(label = 'You will not find help here!')


        frame1 = Frame(self.window)
        frame1.grid(row=2, column=1)
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(frame1, width=40, height=20, wrap = WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)

        self.window.mainloop()
        

    def openFile(self):
        ftypes = [("Text files","*.txt"),
                ("Python files", "*.py"),
                ("HTML files","*.htm"),
                ("All files","*.*")]
        
        filenameforReading = filedialog.askopenfilename(filetypes = ftypes)
        infile = open(filenameforReading, 'r')
        self.text.delete("1.0", END)
        self.text.insert(END, infile.read())
        infile.close()

    def openEFile(self):
        ftypes = [("Text files","*.txt"),
                ("Python files", "*.py"),
                ("HTML files","*.htm"),
                ("All files","*.*")]
        
        filenameforReading = filedialog.askopenfilename(filetypes = ftypes)
        infile = open(filenameforReading, 'r')
        self.text.delete("1.0", END)
        self.text.insert(END, self.decrypt(infile.read()))
        infile.close()

    def saveFile(self):
        filenameforWriting = filedialog.asksaveasfilename(defaultextension='.txt')
        outfile = open(filenameforWriting, 'w')

        outfile.write(self.text.get(1.0, END))
        outfile.close()

    def saveEFile(self):
        filenameforWriting = filedialog.asksaveasfilename(defaultextension='.txt')
        outfile = open(filenameforWriting, 'w')

        outfile.write(self.encrypt(self.text.get(1.0, END)))
        outfile.close()

    def exitEditor(self):
        self.window.destroy()

    def encrypt(self, unencryptedStr):
        key = randint(1,9)
        fancy = str(key)
        for i in range(0, len(unencryptedStr)):
            fancy += chr(ord(unencryptedStr[i]) + key)
        return fancy

    def decrypt(self, encryptedStr):
        keyS = encryptedStr[0]
        key = int(keyS)
        notSoFancy = ''
        for i in range(2, len(encryptedStr)):
            notSoFancy += chr(ord(encryptedStr[i]) - key)
        return notSoFancy


FileEditor()        
