from Model.Price import Price, Prices


class NewReleaseRentalPrice(Price):

    def GetPrice(self, baseRental):
        return baseRental*Prices.NewRelease