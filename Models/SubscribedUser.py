import User

class SubscribedUser(User):

    def __init__(self, UserName, address, PassWord, Email, RentalStatus ):
        super().__init__(self,UserName,address,PassWord,Email,True)
        self.__RentalStatus = RentalStatus

    def Rent(self, days, item):
        self.__RentalStatus = True
        return

    def CancelSub(self):
        return