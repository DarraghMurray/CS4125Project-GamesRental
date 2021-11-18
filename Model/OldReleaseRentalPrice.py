from Model.Price import Price,Prices

class OldReleaseRentalPrice(Price):

    def GetPrice(self, baseRental):
        return baseRental * Prices.OldRelease