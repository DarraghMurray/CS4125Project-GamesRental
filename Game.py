
from Price import Price


class Game:
    def __init__(self, gameName, basePrice):
        self.__gameName = gameName
        self.__basePrice = basePrice

    def GetPrice(self):
        Price.GetPrice()

