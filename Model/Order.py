from DataLayer.DBConnection import databaseConnection

class Order:
    def __init__(self, orderID, items, amountPaid):
        self.__orderID = orderID
        self.__items = items
        self.__amountPaid = amountPaid


    def confirmOrder(self):
        #transaction occurs
        #add order data to database
        return

    def addToDatabase(self, UserID, Total):
        query = "INSERT INTO orders(UserID,total) VALUES(%s, %s)"
        tuple = (UserID, Total)
        databaseConnection.executeStatement(query, tuple)