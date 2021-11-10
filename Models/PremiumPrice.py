from Price import Price


class PremiumPrice(Price):

    def GetPrice(self,basePrice):
        return basePrice - (basePrice*0.15)