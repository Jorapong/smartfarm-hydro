import MySQLdb
import requests
from connectDB import ConnectDB
from mqttsend import Mqttcon
ConnectDB.connect()
Mqttcon.mqttconnect()
class Light:
    @classmethod
    def process_light(self, veget_id):
        light = self.get_light(veget_id)
        if light < 350 :
            Mqttcon.mqttconnect("@msg/hydroponic/light/all","OFF")
            if ConnectDB.get_status("sunscreenIN",0) == 0:
                Mqttcon.mqttconnect("'@msg/greenHouse/OS/CLOSE","off")
                Mqttcon.mqttconnect("@msg/greenHouse/OS/CLOSE","on")
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status("sunscreenIN",0) == 1:
                Mqttcon.mqttconnect("@msg/greenHouse/IS/CLOSE","off")
                Mqttcon.mqttconnect("@msg/greenHouse/IS/CLOSE","on")
                #ClosesunscreenIN
                return True
        elif light >400:
            if ConnectDB.get_status("sunscreenOUT",0) == 1:
                Mqttcon.mqttconnect("@msg/greenHouse/OS/OPEN","off")
                Mqttcon.mqttconnect("@msg/greenHouse/OS/OPEN","on")
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status("sunscreenOUT",0) == 0:
                if ConnectDB.get_status("sunscreenIN",0) == 1:
                    Mqttcon.mqttconnect("@msg/greenHouse/IS/OPEN","off")
                    Mqttcon.mqttconnect("@msg/greenHouse/IS/OPEN","on")
                    #Closesunscreenin
                    return True
                elif ConnectDB.get_status("sunscreenIN",0) == 0:
                    Mqttcon.mqttconnect("@msg/hydroponic/light/red","off")
                    Mqttcon.mqttconnect("@msg/hydroponic/light/blue","on")
                    #Open light
                    return True
        return False



