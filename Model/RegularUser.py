from Model.SubscribedUser import SubscribedUser
from Model.User import User


class RegularUser(User):

    def __init__(self, UserName, address, PassWord, Email ):
        super().__init__(self,UserName,address,PassWord,Email, False)

    def subscribe(self)-> SubscribedUser:
        return

    def purchaseGame(self):
        return
    