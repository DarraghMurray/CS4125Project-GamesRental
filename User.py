from CartInterface import CartInterface


class User:
    
    def __init__(self, UserName, address, PassWord, Email ):
        self.__UserName = UserName
        self.__address = address
        self.__creditCardInfo = ""
        self.__PassWord = PassWord
        self.__Email = Email
        self.IsPremium = False

    def verifyLogIn(self):
        return True

    def addToCart(self, item):
        #calls cart add to cart which places game in cart item list
        return

