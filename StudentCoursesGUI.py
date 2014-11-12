#This is a basic gui that takes a students name and classes and displays them

from tkinter import *
from tkinter import ttk

class ThisLooksUgly():
	def __init__(self):
		self.window = Tk()

		self.form = Frame(self.window)
		self.summary = Frame(self.window)

		self.firstName = StringVar()
		self.lastName = StringVar()

		firstNameLbl = Label(self.form, text = "First Name:").grid(row = 1, column = 1)
		firstNameEntry = Entry(self.form, textvariable = self.firstName).grid(row = 1, column = 2)
		lastNameLbl = Label(self.form, text = "Last Name:").grid(row = 1, column = 3)
		lastNameEntry = Entry(self.form, textvariable = self.lastName).grid(row = 1, column = 4)

		self.maths = ["Linear Algebra & Vector Calculus", "Calculus", "Connections in Math"]
		self.sciences = ["Computer Science", "Anatomy & Physiology"]
		self.senSems = ["iPad Apps", "Nuclear", "SEM", "High Speed Photography"]

		self.mathCourse = StringVar()
		self.mathCourse.set("Choose Course")
		self.scienceCourse = StringVar()
		self.scienceCourse.set("Choose Course")
		self.senSemCourse = StringVar()
		self.senSemCourse.set("Choose Course")

		self.mathCbo = ttk.Combobox(self.form, values = self.maths, textvariable = self.mathCourse, state = 'readonly').grid(row = 2, column = 1)
		self.scienceCbo = ttk.Combobox(self.form, values = self.sciences, textvariable = self.scienceCourse, state = 'readonly').grid(row = 2, column = 2)
		self.senSemCbo = ttk.Combobox(self.form, values = self.senSems, textvariable = self.senSemCourse, state = 'readonly').grid(row = 2, column = 3)

		self.form.pack()

		Button(self.form, text = "Submit", command = self.submit).grid(row = 3, column = 2)

		self.window.mainloop()

	def submit(self):
		Label(self.summary, text = "Name:").grid(row = 1, column = 1)
		self.fName = Label(self.summary, text = (self.firstName.get() + " " + self.lastName.get()))
		self.fName.grid(row = 1, column = 2)
		Label(self.summary, text = "Math").grid(row = 2, column = 1)
		self.mCou = Label(self.summary, text = self.mathCourse.get())
		self.mCou.grid(row = 2, column = 2)
		Label(self.summary, text = "Science").grid(row = 3, column = 1)
		self.SciCou = Label(self.summary, text = self.scienceCourse.get())
		self.SciCou.grid(row = 3, column = 2)
		Label(self.summary, text = "Senior Seminar").grid(row = 4, column = 1)
		self.senCou = Label(self.summary, text = self.senSemCourse.get())
		self.senCou.grid(row = 4, column = 2)
		self.summary.pack()
		self.form.destroy()
		#self.summary.pack()

ThisLooksUgly()