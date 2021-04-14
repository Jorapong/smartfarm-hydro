import MySQLdb
import requests
from connectDB import ConnectDB
class Light:
    @classmethod
    def get_light(self,veget_id):
        light=0
        mycursor = ConnectDB.mycursor()
        mycursor.execute("SELECT light FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            light = row[0]
        return light

    @classmethod
    def get_Sunscreenstt(self):
        mycursor = ConnectDB.mycursor()
        mycursor.execute("SELECT sunscreen FROM status")
        myresult = mycursor.fetchall()
        for row in myresult:
            if row[0]==0:
                return False
            elif row[0]==1:
                return True
        return False

    @classmethod
    def get_lightstt(self):
        mycursor = ConnectDB.mycursor()
        mycursor.execute("SELECT lightstt FROM status")
        myresult = mycursor.fetchall()
        for row in myresult:
            if row[0]==0:
                return False
            elif row[0]==1:
                return True
        return False
    
    @classmethod
    def process_light(self, veget_id):
        light = self.get_light(veget_id)
        if get_Sunscreenstt() is False:
            if light > 1000 :
                return True
            elif light >1200:
                return True
        print("test")
        return False

    def switch(state):
        # mcu.command(state)
        pass
