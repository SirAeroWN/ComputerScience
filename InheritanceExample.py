from AccountClass import Account

class Amex(Account):
	def __init__(self):
		super().__init__()
		self.type = "American Express"
		self.applePay = True

class myCard(Amex):
	def __init__(self):
		super().__init__()
		self.valid = True
		self.stolen = False

card = myCard()
print(card)
print(card.type)
print(card.valid)