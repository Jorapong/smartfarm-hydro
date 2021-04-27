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
        if light < 70 : #แสงมาก
            print('ปิดไฟ')
            client.publish("@msg/hydroponic/lsight/all","off")
            print('ปิดสแลนด้านนอก')
            client.publish("@msg/greenHouse/OS/CLOSE","on")
            #ClosesunscreenOUT
            print('ปิดสแลนด้านใน')
            client.publish("@msg/greenHouse/IS/CLOSE","on")
            #ClosesunscreenIN
            return True
        elif light < 80:
            client.publish("@msg/greenHouse/OS/OPEN","off")
            #ClosesunscreenOUT
            print('ปิดสแลนด้านใน')
            client.publish("@msg/greenHouse/IS/CLOSE","on")
        elif light > 100 : #แสงน้อย
            print('เปิดสแลนด้านนอก')
            client.publish("@msg/greenHouse/OS/OPEN","on")
            #ClosesunscreenOUT
            print('เปิดสแลนด้านใน')
            client.publish("@msg/greenHouse/IS/OPEN","on")
            #Closesunscreenin
            print('เปิดไฟ')
            client.publish("@msg/hydroponic/light/red","on")
            client.publish("@msg/hydroponic/light/blue","on")
        return True



