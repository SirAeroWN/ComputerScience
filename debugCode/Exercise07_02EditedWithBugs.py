class Stock:
    # Construct a stock object 
    def __init__(self, name, symbol, previousPrice, currentPrice):
        self.__name = name
        self.__symbol = symbol
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setPreviousPrice(self, previousPrice):
        self.__previousPrice = previousPrice
        return

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
        return

    def getChangePercent(self):
        return format((self.__currentPrice - self.__previousPrice) * 100 / self.__previousPrice, "5.2f") + "%"

def main():
    # Create a rectangle with width 4 and height 40 
    stock = Stock("Intel Corperation", "INTC", 20.5, 20.35)
    print("The price change is for", stock.getName(), "with symbol", stock.getSymbol(), "is ", stock.getChangePercent())
    stock.setCurrentPrice(25)
    print("The price change is for", stock.getName(), "with symbol", stock.getSymbol(), "is ", stock.getChangePercent())

main()
