from DBManager import DBManager

databaseConnection = DBManager()

query = "INSERT INTO games(Gamename,Gameprice,Gamerental,Gamedescription) VALUES(%s, %s, %s, %s)"
tuple = ("game",50.00, 5.99, "helfe")
databaseConnection.executeStatement(query, tuple)