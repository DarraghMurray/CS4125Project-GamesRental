import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

from config import Config

class DBManager:
    def __init__(self):
        self.__db = mysql.connector.connect(user=Config.DATABASE_CONFIG['user'],password=Config.DATABASE_CONFIG['password'],host=Config.DATABASE_CONFIG['host'],db=Config.DATABASE_CONFIG['dbName'])

    def executeStatement(self, query,params):
        cursor = self.__db.cursor(prepared=True)

        cursor.execute(query,params)
        cursor.close()
        self.__db.commit()
    