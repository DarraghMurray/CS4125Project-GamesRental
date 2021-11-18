
from Model.Price import Price
from Model.StoreItem import StoreItem


class Game(StoreItem):

    __releaseState = None
    
    def __init__(self, gameID, gameName, basePrice, rentalPrice, gameDescription, releaseState):
        self.__gameID = gameID
        self.__gameName = gameName
        self.__basePrice = basePrice
        self.__baseRentalPrice = rentalPrice
        self.__gameDescription = gameDescription

    def transition_to(self, releaseState: Price):
        self.__releaseState = releaseState
        self.__releaseState.context = self

    def getPrice(self) -> float:
        return self.__basePrice

    def getRentalPrice(self) -> float:
        return self.__releaseState.getPrice()
