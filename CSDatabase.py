CS = ["chef", "tell", 60, "will", "norvelle", 52, "lisa", "lotz", 99]

again = 'y'

while(again.lower() == 'y'):

	for i in range(0, len(CS), 3):
		passFail = "Passing"
		if(CS[i + 2] < 70):
			passFail = "Failing"
		print(CS[i], CS[i+1], "has a ", str(CS[i+2]), "which is", passFail)
	
	again = input("Add another student? y/n ")
	if (again.lower() == 'y'):
		CS.append(input("First name: "))
		CS.append(input("Last name: "))
		CS.append(eval(input("Numeric grade: ")))