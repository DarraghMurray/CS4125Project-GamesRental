class AdminUser(User):

    def __init__(self, UserName, address, PassWord, Email, AdminName ):
        super().__init__(self,UserName,address,PassWord,Email)
        self.__AdminName = AdminName