from CartInterface import CartInterface


class Cart(CartInterface):
    def __init__(self, itemNames ):
        self.__itemNames = itemNames

    def UpdateCart(self):
        pass

    def AddToCart(self, item):
        self.__itemNames.append(item)

    def RemoveFromCart(self, item):
        if item in self.__itemNames:
            self.__itemNames.remove(item)
    
    def ClearCart(self):
        self.__itemNames.clear()

    def ProceedToOrder(self):
        #calls appropriate methods to begin transaction
        #on successful purchase add to database games library
        pass