#establish constants to be used
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#now get user input
today = eval(input("Enter today's day: "))
future = eval(input("Enter the number of days elapsed since today: "))
if(today > 6):
	print("Whoa there cowboy")
elif(today < 0):
	print("What are you even doing?")
else:
	date = future + today
	date = date - ((date//7) * 7)
	answer = "Today is " + week[today] + " and the future day is " + week[date]
	print(answer)