import MySQLdb
import requests
from connectDB import ConnectDB

#from mqttsend import Mqttcon
ConnectDB.connect()
#Mqttcon.connect()
import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.31.41" 
client = mqtt.Client("P1")
client.username_pw_set("smartfarm", "123456788")
client.connect(broker_address)
class Light:
    @classmethod
<<<<<<< Updated upstream
    def process_light(cls,veget_id):
        light = ConnectDB.get_values("light",veget_id)
        print(light)
        if light < 265 : #แสงมาก
            print('ปิดไฟ')
            client.publish("@msg/hydroponic/light/all","OFF")
            if ConnectDB.get_status(3,0) == 1:
                print('ปิดสแลนด้านนอก')
                client.publish("@msg/greenHouse/OS/CLOSE","off")
                client.publish("@msg/greenHouse/OS/CLOSE","on")
=======
    def process_light(self, veget_id):
        light = self.get_light(veget_id)
        if light < 310 :
            Mqttcon.mqttconnect("@msg/hydroponic/light/all","OFF")
            if ConnectDB.get_status("sunscreenIN",0) == 0:
                Mqttcon.mqttconnect("'@msg/greenHouse/OS/CLOSE","OFF")
                Mqttcon.mqttconnect("@msg/greenHouse/OS/CLOSE","ON")
>>>>>>> Stashed changes
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status(4,0) == 1:
                print('ปิดสแลนด้านใน')
                client.publish("@msg/greenHouse/IS/CLOSE","off")
                client.publish("@msg/greenHouse/IS/CLOSE","on")
                #ClosesunscreenIN
                return True
<<<<<<< Updated upstream
            return False
        elif light > 265 : #แสงน้อย
            if ConnectDB.get_status(3,0) == 0:
                print('เปิดสแลนด้านนอก')
                client.publish("@msg/greenHouse/OS/OPEN","off")
                client.publish("@msg/greenHouse/OS/OPEN","on")
=======
            else :
                return
        elif light > 335 :
            if ConnectDB.get_status("sunscreenOUT",0) == 1:
                Mqttcon.mqttconnect("@msg/greenHouse/OS/OPEN","OFF")
                Mqttcon.mqttconnect("@msg/greenHouse/OS/OPEN","ON")
>>>>>>> Stashed changes
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status(3,0) == 1:
                if ConnectDB.get_status(4,0) == 0:
                    print('เปิดสแลนด้านใน')
                    client.publish("@msg/greenHouse/IS/OPEN","off")
                    client.publish("@msg/greenHouse/IS/OPEN","on")
                    #Closesunscreenin
                    return True
                elif ConnectDB.get_status(4,0) == 1:
                    print('เปิดไฟ')
                    client.publish("@msg/hydroponic/light/red","on")
                    client.publish("@msg/hydroponic/light/blue","on")
                    #Open light
                    return True
                else :
                    return
        return False



