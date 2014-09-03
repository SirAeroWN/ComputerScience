#Take the yaer that the user inputs and print out a calender for it

#get user input
userTyped = input("Please enter a year, or 'q' to stop: ")
c = 0
#these are the length of months, not really needed but it makes it easier to uderstand :D
jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
Oct = 31 #must have capital because oct is reserved
nov = 30
dec = 31

leap = 0

while(userTyped != 'q'):
    userYear = eval(userTyped)
    #now set up the constants for the congruence and iterating
    k = userYear % 100 #year minus century eg: 14 out of 2014
    j = userYear // 100 #century minus year eg 20 out of 2014

    #determine if it is a leap year:
    #1)If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5
    #2)If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4
    #3)If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5
    #4)The year is a leap year
    #5)The year is not a leap year

    leap = 0 #normally not a leap year
    if((((userYear % 4) == 0) and ((userYear % 100) != 0)) or ((userYear % 400) == 0)):
        #Leap Year!
        feb = 29
        leap = 1 #will check for this in loops to see if need to add one to the day because february is longer
    else:
    	#not a leap year
    	feb = 28 #need to set feb to 28 in case there has already been a leap year

    m = 1 #start on january which has to be 13 in zellar's congruence

    iterContinue = "yes"
    check = 0
    
    while(m <= 12):
        
        h = 0

        #start on first day of month each time    
        q = 1 

        #Now set to correct month for string & days
        if(m == 1):
            days = jan
            m = 13
            month = "January"
            k -= 1 #january and february are months 13 and 14 of the previous year, gets reset when moving on to march
        elif(m == 2):
            days = feb
            m = 14
            month = "February"
        elif(m == 3):
            days = mar
            k += 1
            month = "March"
        elif(m == 4):
            days = apr
            month = "April"
        elif(m == 5):
            days = may
            month = "May"
        elif(m == 6):
            days = jun
            month = "June"
        elif(m == 7):
            days = jul
            month = "July"
        elif(m == 8):
            days = aug
            month = "August"
        elif(m == 9):
            days = sep
            month = "September"
        elif(m == 10):
            days = Oct
            month = "October"
        elif(m == 11):
            days = nov
            month = "November"
        elif(m == 12):
            days = dec
            month = "December"

        #the month header is printed once per month
        print(format(month, ">35s"), str(userYear))
        print(format("______________________________", ">49s"))
        print(format("Sun", ">23s"), format("Mon", ">3s"), format("Tue", ">3s"), format("Wed", ">3s"), format("Thu", ">3s"), format("Fri", ">3s"), format("Sat", ">3s"))
        while(q <= days):
            h = ((q + ((13 * (m + 1)) / 5) + k + (k / 4) + (j / 4) + (5 * j)) % 7) #zellars congruence
            h = int(h) #fixes decimal return
            if(((m % 2) != 0) and ((m != 13) or (m != 14))):
               h = h + 1

            #If first day of month put the '1' in whichever column is apropriate, if in saturday(0) allow for \n
            if(q == 1):
                if(h == 1):
                    print(format('1', ">22s"), end = '')
                elif(h == 2):
                    print(format('1', ">26s"), end = '')
                elif(h == 3):
                    print(format('1', ">30s"), end = '')
                elif(h == 4):
                    print(format('1', ">34s"), end = '')
                elif(h == 5):
                    print(format('1', ">38s"), end = '')
                elif(h == 6):
                    print(format('1', ">42s"), end = '')
                else:
                    print(format('1', ">46s"))
            #If not first day print the day, if sunday(1) need to allot more space, allow \n on staurday
            else:
                if(h == 1):
                    print(format(str(q), ">22s"), end = '')
                elif(h >= 2 and h <=6):
                    print(format(str(q), ">4s"), end = '')
                else:
                    print(format(str(q), ">4s"))
            if(q == days and h != 0): #for when month doesn't end on a staurday
                print()
            q += 1 #iterates day

        #because of weird calcs, need to set month back to normal
        if(month == "January"):
            m = 1
            print("January", m, k
                  )

        if(month == "February"):
            m = 2
            print("February", m, k)

        m += 1 #iterates month
        print(m, k)
        
    #ask them if they want out
    userTyped = input("\nPlease enter a year, or \"q\" to stop: ")
