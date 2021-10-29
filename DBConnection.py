import mysql.connector

from config import Config

class DBConnection:
    def __init__(self):
         self.db=mysql.connector.connect(
            Config.DATABASE_CONFIG['user'],
            Config.DATABASE_CONFIG['password'],
            Config.DATABASE_CONFIG['host'],
            Config.DATABASE_CONFIG['dbName']
            )

    def executeStatement(self, query, params):
        pass
    