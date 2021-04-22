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
    def process_light(cls,veget_id):
        light = ConnectDB.get_values("light",veget_id)
        print(light)
        if light < 270 : #แสงมาก
            print('ปิดไฟ')
            client.publish("@msg/hydroponic/light/all","OFF")
            if ConnectDB.get_status(4,0) == 0:
                print('ปิดสแลนด้านนอก')
                client.publish("@msg/greenHouse/OS/CLOSE","off")
                client.publish("@msg/greenHouse/OS/CLOSE","on")
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status(4,0) == 1:
                print('ปิดสแลนด้านใน')
                client.publish("@msg/greenHouse/IS/CLOSE","off")
                client.publish("@msg/greenHouse/IS/CLOSE","on")
                #ClosesunscreenIN
                return True
        elif light >285 : #แสงน้อย
            if ConnectDB.get_status(3,0) == 1:
                print('เปิดสแลนด้านนอก')
                client.publish("@msg/greenHouse/OS/OPEN","off")
                client.publish("@msg/greenHouse/OS/OPEN","on")
                #ClosesunscreenOUT
                return True
            elif ConnectDB.get_status(3,0) == 0:
                if ConnectDB.get_status(4,0) == 1:
                    print('เปิดสแลนด้านใน')
                    client.publish("@msg/greenHouse/IS/OPEN","off")
                    client.publish("@msg/greenHouse/IS/OPEN","on")
                    #Closesunscreenin
                    return True
                elif ConnectDB.get_status(4,0) == 0:
                    print('เปิดไฟ')
                    client.publish("@msg/hydroponic/light/red","off")
                    client.publish("@msg/hydroponic/light/blue","on")
                    #Open light
                    return True
        return False



