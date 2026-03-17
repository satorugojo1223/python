# computer price

class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("the max price is", self.__maxprice)

    def setmaxprice(self, price):
        self.__maxprice = price

computer1 = computer()
computer1.__maxprice = 2000
computer1.sell()

computer.setmaxprice(2300)
computer.sell()