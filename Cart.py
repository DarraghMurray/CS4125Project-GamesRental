class Cart:
    def __init__(self, itemNames ):
        self.__itemNames = itemNames

    def UpdateCart(self):
        pass

    def AddItem(self, item):
        self.__itemNames.append(item)

    def ProceedToOrder(self):
        pass