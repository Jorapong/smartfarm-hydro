import MySQLdb
import requests
class ConnectDB:
    @classmethod
    def mycursor(self):
        mydb = MySQLdb.connect(host="localhost",user="root",password="",database="farm_db")
        mycursor = mydb.cursor()
        return mycursor
    
    @classmethod
    def get_status(self,name):
        mycursor= self.mycursor()
        mycursor.execute("SELECT "+name+" FROM status where veget_id=")
        myresult = mycursor.fetchall()
        return myresult
    
    @classmethod
    def get_statusveget(self,name,veget_id):
        mycursor= self.mycursor()
        mycursor.execute("SELECT "+name+" FROM status where veget_id=")
        myresult = mycursor.fetchall()
        return myresult