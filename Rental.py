class Rental:
    def __init__(self, DaysRented, ItemRented):
        self.__DaysRented = DaysRented
        self.__ItemRented = ItemRented

    def getRentedGames(self):
        return self.__ItemRented