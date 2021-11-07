from CartInterface import CartInterface


class User:
    
    def __init__(self, UserID, UserName, address, PassWord, Email, isPremium ):
        self.__UserID = UserID
        self.__UserName = UserName
        self.__address = address
        self.__creditCardInfo = ""
        self.__PassWord = PassWord
        self.__Email = Email
        self.IsPremium = isPremium

    def verifyLogIn(self):
        return True

    def addToCart(self, item):
        #calls cart add to cart which places game in cart item list
        return

