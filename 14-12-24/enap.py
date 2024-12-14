class lap:
    def __init__(self):
        self.__price = 100000
    def sell(self):
        print("selling price is" , self.__price)
    def maxprice(self,minprice):
        self.__price = minprice
    
c=lap()
c.sell()

c.__price = 100000
c.sell()

c.maxprice(10000)
c.sell