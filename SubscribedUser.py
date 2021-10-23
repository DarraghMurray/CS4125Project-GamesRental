class SubscribedUser(User):

    def __init__(self, UserName, address, PassWord, Email, RentalStatus ):
        super().__init__(self,UserName,address,PassWord,Email)
        self.__RentalStatus = RentalStatus

    def CancelSub():
        return