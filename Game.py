
from Price import Price
from StoreItem import StoreItem


class Game(StoreItem):
    def __init__(self, gameName, basePrice, rentalPrice, gameDescription):
        self.__gameName = gameName
        self.__basePrice = basePrice
        self.__rentalPrice = rentalPrice
        self.__gameDescription = gameDescription

    def getPrice(self) -> float:
        return self.__basePrice

