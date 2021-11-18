from Model.Price import Price,Prices

class IndieRentalPrice(Price):

    def GetPrice(self, basePrice):
        return Prices.Indie