
from Price import Price


class Game:
    def __init__(self, gameName, basePrice, rentalPrice, gameDescription):
        self.__gameName = gameName
        self.__basePrice = basePrice
        self.__rentalPrice = rentalPrice
        self.__gameDescription = gameDescription

    def GetPrice(self):
        Price.GetPrice()

