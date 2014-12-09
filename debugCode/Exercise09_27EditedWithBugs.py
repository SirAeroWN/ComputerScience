from tkinter import * # Import tkinter
    
def getMonthlyPayment(loanAmount, numberOfYears, monthlyInterestRate):
    amount = loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)))
    return amount

class MainGUI:
    def __init__(self):        
        window = Tk() # Create a window
        window.title("Compare Interest Rates") # Set title
        
        frame1 = Frame(window)
        frame1.pack()
        
        Label(frame1, text = "Loan Amount").grid(row = 1, column = 1, sticky = W)
        
        self.loanAmount = StringVar()
        self.loanAmount.set('10')
        frame2 = Frame(window)
        frame2.pack()
        scrollbar = Scrollbar(frame2)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(frame2, wrap = WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)
        self.burden = Entry(frame1, textvariable = self.loanAmount, justify = RIGHT).grid(row = 1, column = 2)
        Label(frame1, text = "Years").grid(row = 1, column = 3, padx = 5)
        self.numberOfYears = StringVar()
        self.numberOfYears.set('10')
        self.duration = Entry(frame1, textvariable = self.numberOfYears, justify = RIGHT).grid(row = 1, column = 4)
        Button(frame1, text = "Calculate", command = self.computeFutureValue).grid(row = 1, column = 5, sticky = E)
        self.computeFutureValue()
        
        
        
        window.mainloop() # Create an event loop

    def computeFutureValue(self):
        self.text.delete(1.0, END)
        loan = float(self.loanAmount.get())
        years = float(self.numberOfYears.get())

        self.text.insert(END, format("Interest Rate", "20s") + format("Monthly Payment", "20s") +
                         format("Total Payment", "20s") + "\n")    
       
                    
        annualInterestRate = 5
        while annualInterestRate <= 8:
            monthlyPayment = getMonthlyPayment(loan, years, annualInterestRate / 1200)
            totalPayment = monthlyPayment * years * 12
            self.text.insert(END, format(annualInterestRate, "<20.2f") + format(monthlyPayment, "<20.2f")
                             + format(totalPayment, "<20.2f") + "\n")
                            
            annualInterestRate += 1 / 8

MainGUI()
