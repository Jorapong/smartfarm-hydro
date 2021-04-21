import MySQLdb
import requests
from connectDB import ConnectDB
# from mqttsend import Mqttcon
ConnectDB.connect()
# Mqttcon.mqttconnect()
class Light:
    @classmethod
    def process_light(cls,veget_id):
        light = cls.get_value(veget_id)
        if light < 310 : #แสงมาก
            print('ปิดไฟ')
            # Mqttcon.mqttconnect("@msg/hydroponic/light/all","OFF")
            if ConnectDB.get_status("sunscreenIN",0) == 0:
                print('ปิดสแลนด้านนอก')
                # Mqttcon.mqttconnect("@msg/greenHouse/OS/CLOSE","off")
                # Mqttcon.mqttconnect("@msg/greenHouse/OS/CLOSE","on")
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status("sunscreenIN",0) == 1:
                print('ปิดสแลนด้านใน')
                # Mqttcon.mqttconnect("@msg/greenHouse/IS/CLOSE","off")
                # Mqttcon.mqttconnect("@msg/greenHouse/IS/CLOSE","on")
                #ClosesunscreenIN
                return True
        elif light >335 : #แสงน้อย
            if ConnectDB.get_status("sunscreenOUT",0) == 1:
                print('เปิดสแลนด้านนอก')
                # Mqttcon.mqttconnect("@msg/greenHouse/OS/OPEN","off")
                # Mqttcon.mqttconnect("@msg/greenHouse/OS/OPEN","on")
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status("sunscreenOUT",0) == 0:
                if ConnectDB.get_status("sunscreenIN",0) == 1:
                    print('เปิดสแลนด้านใน')
                    # Mqttcon.mqttconnect("@msg/greenHouse/IS/OPEN","off")
                    # Mqttcon.mqttconnect("@msg/greenHouse/IS/OPEN","on")
                    #Closesunscreenin
                    return True
                elif ConnectDB.get_status("sunscreenIN",0) == 0:
                    print('เปิดไฟ')
                    # Mqttcon.mqttconnect("@msg/hydroponic/light/red","off")
                    # Mqttcon.mqttconnect("@msg/hydroponic/light/blue","on")
                    #Open light
                    return True
        return False



