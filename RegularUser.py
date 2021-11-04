import User


class RegularUser(User):

    def __init__(self, UserName, address, PassWord, Email ):
        super().__init__(self,UserName,address,PassWord,Email, False)

    def changeAccType(self):
        return

    def purchaseGame(self):
        return
    