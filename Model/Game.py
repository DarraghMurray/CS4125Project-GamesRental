
from Model.Price import Price
from Model.StoreItem import StoreItem


class Game(StoreItem):
    def __init__(self, gameID, gameName, basePrice, rentalPrice, gameDescription):
        self.__gameID = gameID
        self.__gameName = gameName
        self.__basePrice = basePrice
        self.__rentalPrice = rentalPrice
        self.__gameDescription = gameDescription

    def getPrice(self) -> float:
        return self.__basePrice

