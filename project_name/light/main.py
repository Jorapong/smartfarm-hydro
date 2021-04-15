import MySQLdb
import requests
from connectDB import ConnectDB
ConnectDB.connect()
class Light:
    
    @classmethod
    def process_light(self, veget_id):
        light = self.get_light(veget_id)
        if light < 350 :
            if get_Sunscreenstt() is False:
                return True
            else 
        elif light >1200:
                return True
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

    def on_light():

