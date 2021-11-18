
from Model.Price import Price
from Model.StoreItem import StoreItem


class Game(StoreItem):

    __rentalPriceRange = None
    
    def __init__(self, gameID, gameName, basePrice, rentalPrice, gameDescription, rentalPriceRange):
        self.__gameID = gameID
        self.__gameName = gameName
        self.__basePrice = basePrice
        self.__rentalPrice = rentalPrice
        self.__gameDescription = gameDescription

    def transition_to(self, rentalPriceRange: Price):
        self.__rentalPriceRange = rentalPriceRange
        self.__rentalPriceRange.context = self

    def getPrice(self) -> float:
        return self.__basePrice

    def getRentalPrice(self) -> float:
        return self.__rentalPriceRange.getPrice()
