#simple bank account with id, balance,interest, etc.

class Account:
	def __init__(self, Id = 0, balance = 100, annualInterestRate = 0):
		self.__id = Id
		self.__balance = float(balance)
		self.__yearIntRate = float(annualInterestRate)
		return

	def getId(self):
		return self.__id

	def getBalance(self):
		return self.__balance

	def getYearIntRate(self):
		return self.__yearIntRate

	def setId(self, newId):
		self.__id = newId
		return

	def setBalance(self, newBalance):
		self.__yearIntRate = newBalance
		return

	def setYearIntRate(self, newInt):
		self.__yearIntRate = newInt
		return

	def getMonthlyInterestRate(self):
		return (self.__yearIntRate / 12)

	def getMonthlyInterest(self):
		return (self.__balance * (self.getMonthlyInterestRate() / 100))

	def withdraw(self, credit):
		self.__balance -= credit
		return

	def deposit(self, debit):
		self.__balance += debit
		return

	def __str__(self):
		return str("id: " + str(self.__id) + "\nbalance: " + str(self.__balance) + "\nmonthly interest rate: " + str(self.getMonthlyInterestRate()) + "\nmonthly interest: " + str(self.getMonthlyInterest()))

myAccnt = Account(1122, 20000, 4.5)
myAccnt.withdraw(2500)
myAccnt.deposit(3000)
print(myAccnt)
