######################################################################################
######################################################################################
##### WHEN ADDING A PERSON, YOU MUST FIRST DESELECT THE WINDOW AND THEN RESELECT #####
######################################################################################
######################################################################################

from tkinter import *
from tkinter import filedialog

NumberOfPeople = 0

class LinkedListNode:
    def __init__(self, mydata, mynext):
        self.data = mydata
        self.next = mynext
        return

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
        self.current = self.head
        return

    def __str__(self):
        theString = ''
        curNode = self.head
        atTheEnd = False
        while not atTheEnd:
            theString = theString + str(curNode.data)
            if curNode.next == None:
                atTheEnd = True
            curNode = curNode.next
        return theString

    def addToRear(self, data):
        node = LinkedListNode(data, None)
        if self.size == 0:
            self.head = node
            self.tail = node
            self.current = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return

    def removeFromRear(self):
        curNode = self.head
        for i in range(self.size - 2):
            curNode = curNode.next
        curNode.next = None
        self.tail = curNode
        self.size -= 1
        return

    def addToFront(self, data):
        if self.size == 0:
            nextNode = None
        else:
            nextNode = self.head
        node = LinkedListNode(data, nextNode)
        self.head = node
        self.size += 1
        return

    def removeFromFront(self):
        self.head = self.head.next
        self.size -= 1
        return

class person:
    def __init__(self, fn = None, ln = None, p = None, add = None, c = None, s = None, z = None):
        global NumberOfPeople
        self.firstname = fn
        self.lastname = ln
        self.phone = p
        self.address = add
        self.city = c
        self.state = s
        self.zip = z
        NumberOfPeople += 1
        return

    def getfirstname(self):
        return self.firstname

    def getlastname(self):
        return self.lastname

    def getphone(self):
        return self.phone

    def getaddress(self):
        return self.address

    def getcity(self):
        return self.city

    def getstate(self):
        return self.state

    def getzip(self):
        return self.zip

def previous():
    global current
    if current != 0:
        current -= 1
        update(current)
    return

def nextname():
    global current
    if current != NumberOfPeople-1:
        current +=1
        update(current)
    return

def update(current):
    global First, Last, Phone
    First.set(mylist.current.data.getfirstname())
    Last.set(mylist.current.data.getlastname())
    Phone.set(mylist.current.data.getphone())
    Address.set(mylist.current.data.getaddress())
    City.set(mylist.current.data.getcity())
    State.set(mylist.current.data.getstate())
    Zip.set(mylist.current.data.getzip())
    return

def addperson():
    mylist.append(person(FN.get(), LN.get(), Ph.get(), Ad.get(), Ci.get(), St.get(), Zi.get()))
    FN.set('')
    LN.set('')
    Ph.set('')
    Ad.set('')
    Ci.set('')
    St.set('')
    Zi.set('')
    frame2.pack_forget()
    frame1.pack()
    return

def newpersonframe():
    frame1.pack_forget()
    frame2.pack()
    return

def fileOpen(fileName):
    database = open(fileName, 'r')
    alist = LinkedList()
    for line in database:
        items = parsed(line.strip())
        alist.addToRear(person(items[0], items[1], items[2], items[3], items[4], items[5], items[6]))
    database.close()
    return alist

def parsed(nastyStr):
    personList = nastyStr.split(',')
    for entry in personList:
        entry.strip()
    return personList

def finWrite():
    global dataFile
    global mylist
    global root
    outF = open(dataFile, 'w')
    for peep in mylist:
        thing = peep.getfirstname() + ',' + peep.getlastname() + ',' + peep.getphone() + ',' + peep.getaddress() + ',' + peep.getcity() + ',' + peep.getstate() + ',' + peep.getzip() + '\n'
        outF.write(thing)
    outF.close()
    root.destroy()
    return

current = 0   

root = Tk()

dataFile = filedialog.askopenfilename()
mylist = fileOpen(dataFile)

frame1 = Frame(root)
frame1.pack()

Fnamelabel = Label(frame1, text = "First name: ").grid(row = 0, column = 0)
Lnamelabel = Label(frame1, text = "Last Name: ").grid(row = 1, column = 0)
PLabel = Label(frame1, text = "Phone Number: ").grid(row = 2, column = 0)
AddLabel = Label(frame1, text = "Address: ").grid(row = 3, column = 0)
CLabel = Label(frame1, text = "City: ").grid(row = 4, column = 0)
SLabel = Label(frame1, text = "State: ").grid(row = 5, column = 0)
ZLabel = Label(frame1, text = "Zip: ").grid(row = 6, column = 0)
First = StringVar()
First.set(mylist.head.data.getfirstname())
Last = StringVar()
Last.set(mylist.head.data.getlastname())
Phone = StringVar()
Phone.set(mylist.head.data.getphone())
Address = StringVar()
Address.set(mylist.head.data.getaddress())
City = StringVar()
City.set(mylist.head.data.getcity())
State = StringVar()
State.set(mylist.head.data.getstate())
Zip = StringVar()
Zip.set(mylist.head.data.getzip())

FirstNameLabel = Label(frame1, textvariable = First).grid(row = 0, column = 1)
LastNameLabel = Label(frame1, textvariable = Last).grid(row = 1, column = 1)
PhoneLable = Label(frame1, textvariable = Phone).grid(row = 2, column = 1)
AddressLable = Label(frame1, textvariable = Address).grid(row = 3, column = 1)
CityLable = Label(frame1, textvariable = City).grid(row = 4, column = 1)
StateLable = Label(frame1, textvariable = State).grid(row = 5, column = 1)
ZipLable = Label(frame1, textvariable = Zip).grid(row = 6, column = 1)

prev = Button(frame1, text = 'Prev', command = previous).grid(row = 8, column = 0)
Next = Button(frame1, text = 'Next', command = nextname).grid(row = 8, column = 1)
New = Button(frame1, text = 'New', command = newpersonframe).grid(row = 9, columnspan = 2)
Fin = Button(frame1, text = 'Finish', command = finWrite).grid(row = 10, columnspan = 2)

frame2 = Frame(root)

FN = StringVar()
FN.set('')
LN = StringVar()
LN.set('')
Ph = StringVar()
Ph.set('')
Ad = StringVar()
Ad.set('')
Ci = StringVar()
Ci.set('')
St = StringVar()
St.set('')
Zi = StringVar()
Zi.set('')
FirstEntry = Entry(frame2, textvariable = FN).grid(row = 1, column = 1)
LastEntry = Entry(frame2, textvariable = LN).grid(row = 2, column = 1)
PhoneEntry = Entry(frame2, textvariable = Ph).grid(row = 3, column = 1)
AddressEntry = Entry(frame2, textvariable = Ad).grid(row = 4, column = 1)
CityEntry = Entry(frame2, textvariable = Ci).grid(row = 5, column = 1)
StateEntry = Entry(frame2, textvariable = St).grid(row = 6, column = 1)
ZipEntry = Entry(frame2, textvariable = Zi).grid(row = 7, column = 1)

InstLabel = Label(frame2, text = 'Please enter you information below').grid(row = 0, columnspan = 2)
FirstLabel = Label(frame2, text = 'First Name: ').grid(row = 1, column = 0)
LastLabel = Label(frame2, text = 'Last Name: ').grid(row = 2, column = 0)
PhoneLabel = Label(frame2, text = 'Phone Number: ').grid(row = 3, column = 0)
AddressLabel = Label(frame2, text = 'Address: ').grid(row = 4, column = 0)
CityLabel = Label(frame2, text = 'City: ').grid(row = 5, column = 0)
StateLabel = Label(frame2, text = 'State: ').grid(row = 6, column = 0)
ZipLabel = Label(frame2, text = 'Zip: ').grid(row = 7, column = 0)
Add = Button(frame2, text = 'Add', command = addperson).grid(row = 8, columnspan = 2)

root.mainloop()
