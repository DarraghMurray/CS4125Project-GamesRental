
import User
from Database.DBConnection import databaseConnection as DC

class AdminUser(User):

    def __init__(self, UserName, address, PassWord, Email, AdminName ):
        super().__init__(self,UserName,address,PassWord,Email)
        self.__AdminName = AdminName

    #receives game object with details of game and adds it to database game table
    def AddGame(gameName, gamePrice, gameRental, gameDescription):
        query = "INSERT INTO games(Gamename,Gameprice,Gamerental,Gamedescription) VALUES(%s,%s,%s,%s"
        parameters = (gameName, gamePrice, gameRental, gameDescription)
        DC.executeStatement(query, parameters)

    def RemoveGame(gameID):
        query = "DELETE FROM games WHERE GameID=%s"
        parameters = (gameID)
        DC.executeStatement(query, parameters)

    def BanUser(userID):
        pass