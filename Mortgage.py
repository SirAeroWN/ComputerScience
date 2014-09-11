#prompt user for loan and duration
loan = eval(input("Enter the loan amount: "))
duration = eval(input("Enter the duration of the loan: "))

#print header
print(format("Interest Rate", "<17s"), format("Monthly Payment", "<20s"), format("Total Payment", "<35s"))

interest = 5

for interest in range(5000, 8125, 125):

    monthRate = interest / 1200000
    monthPay = (loan) * ((monthRate * ((1 + monthRate)**(duration * 12))) / ((1 + monthRate)**(duration * 12) - 1))
    total = monthPay * 12 * duration

    print(format((interest / 1000), "<17.3f"), format(monthPay, "<20.3f"), format(total, "<30.3f"))
    
