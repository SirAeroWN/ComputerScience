from StudentClass import Student

def addScoresBeacauseIDontWantToType(leStudent, scores, exam):
	for score in scores:
		leStudent.addTestScore(score)
	leStudent.setExam(exam)
	return

def printThisStuff(classList):
	table = "First Name   Last Name    StudentID    Semester Avg\n"
	print(table)
	for studente in classList:
		printStudent(studente)
	return

def printStudent(elStudent):
	line = format(elStudent.getFirstName(), "<13s") + format(elStudent.getLastName(), "<13s") + format(str(elStudent.getStudentID()), "<13s") + str(elStudent.getGrade()) + "\n"
	print(line)
	return

csCourse = []

student1 = Student("Amy Amazing")
addScoresBeacauseIDontWantToType(student1, [100, 99, 98], 100)
csCourse.append(student1)

student2 = Student("Mike Mediocre")
addScoresBeacauseIDontWantToType(student2, [80, 70, 75], 72)
csCourse.append(student2)

student3 = Student("Sam Slacker")
addScoresBeacauseIDontWantToType(student3, [50, 40, 20], 60)
csCourse.append(student3)

print("Computer Science Class")
printThisStuff(csCourse)

mathCourse = []

addScoresBeacauseIDontWantToType(student1, [100, 95], 99)
mathCourse.append(student1)

addScoresBeacauseIDontWantToType(student2, [70, 75], 80)
mathCourse.append(student2)

addScoresBeacauseIDontWantToType(student3, [50, 60], 40)
mathCourse.append(student3)

print("\n\nMath Class")
printThisStuff(mathCourse)