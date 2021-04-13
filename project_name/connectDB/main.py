import MySQLdb
import requests
class ConnectDB:
    @classmethod
    def mycursor(self):
        mydb = MySQLdb.connect(host="localhost",user="root",password="",database="farm_db")
        mycursor = mydb.cursor()
        return mycursor