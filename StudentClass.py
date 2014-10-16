#This is a simple student class with various descriptors of a student

import random

class Student:
	def __init__(self, name):
		name = name.split(' ')
		self.__firstname = name[0]
		self.__lastname = name[1]
		self.__studentID = Student.generateID()
		self.__testScores = []
		self.__exam = 0
		return

	def getFirstName(self):
		return self.__firstname

	def getLastName(self):
		return self.__lastname

	def getStudentID(self):
		return self.__studentID

	def getExam(self):
		return self.__exam

	def setFirstName(self, newFirst):
		self.__firstname = str(newFirst)
		return

	def setLastName(self, newLast):
		self.__lastname = str(newLast)
		return

	def setExam(self, examScore):
		self.__exam = float(examScore)
		return

	def generateID():
		baseNum = str(random.randint(1, 9999))
		ID = baseNum + ('0' * (4 - len(baseNum)))
		return ID

	def addTestScore(self, testScore):
		self.__testScores.append(float(testScore))
		return

	def getGrade(self):
		testAverage = sum(self.__testScores) / len(self.__testScores)
		grade = (testAverage * .75) + (self.__exam * .25)
		grade = format(grade, ".2f")
		return grade
