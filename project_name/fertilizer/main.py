from connectDB import ConnectDB
from mqttsend import Mqttcon
import json
from time import sleep
Mqttcon.connect()
ConnectDB.connect()
import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.31.41" 
client = mqtt.Client("P1")
client.username_pw_set("smartfarm", "123456788")
client.connect(broker_address)
class Fertilizer:
    @classmethod
    def process_fertilizer(self,veget):
        ec = ConnectDB.get_sensorvalue("ec",veget['sensorv_id']) #ec ที่วัดได้
        ph = ConnectDB.get_sensorvalue("ph",veget['sensorv_id']) #pH ที่วัดได้
        valueveget = ConnectDB.get_valueveget(veget['veget_id']) #ค่า ที่ต้องการ
        fertilizerintense = ConnectDB.get_fertilizer(veget['fertilizer_id']) #ความเข้มข้นปุ๋ย
        level = ConnectDB.get_sensorvalue("level",veget['veget_id']) #ระดับน้ำ
        mixer = ConnectDB.get_sensorvalue("mixer",0) #สถานะถังน้ำ
        pump1 = ConnectDB.get_sensorvalue("pump1",0) #สถานะถังน้ำ
        if  (mixer == 1 and pump1==0):
            #ปล่อยนำทื้ง
            pass
            #client.publish("@msg/pump/pump1","on")
            #client.publish("@msg/pump/pump1","off")
        elif (mixer == 0 and pump1==0):
            if(ec <= (valueveget['ec']-0.1)):
                fertilizer = (ec - valueveget['ec'])*100000 #คำนวนหาจำนวนที่ต้องใช้ปุ๋ย
                fertilizerml = fertilizer * 1000
                client.publish("@msg/fertilizer/fertilizer1/control",fertilizerml)#เติมปุ๋ยที่ยังไม่ผสม
                client.publish("@msg/pump/pump2","on")
                sleep(10)
                if(ph <= (valueveget['ph']-0.1)):#phต่ำ
                    waterml = ((fertilizerml/20)/2)#คำนวนหาน้ำที่ต้องเติมตามค่า ph
                else:
                    waterml = (fertilizerml/20)/2 #คำนวนหาน้ำที่ต้องเติม
                client.publish("@msg/fertilizer/water/control",waterml)#เติมน้ำเพื่อผสม
                client.publish("@msg/pump/pump1","on")
                client.publish("@msg/htdroponic/htdroponic2","on")
                client.publish("@msg/pump/flow2",fertilizerml)#เติมปุ๋ยที่ผสมแล้ว
                client.publish("@msg/pump/flow2",3000)#เติมน้ำล้างท่อ
                client.publish("@msg/htdroponic/htdroponic2","off")
                return True
                
            elif(ec >= (valueveget['ec']+0.1)):
                water=ec-valueveget['ec']#คำนวนปริมาณเพื่อเจือจาง
                client.publish("@msg/htdroponic/htdroponic1","on")
                client.publish("@msg/greenHouse/water","on")
                client.publish("@msg/pump/flow2",water)#เติมน้ำเพื่อนเจือจาง
                client.publish("@msg/pump/pump1","on")
                client.publish("@msg/htdroponic/htdroponic1","off")
                return True
        return False