from connectDB import ConnectDB
from mqttsend import Mqttcon
import json
Mqttcon.connect()
ConnectDB.connect()
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
            Mqttcon.client.publish("@msg/pump/pump1","on")
            Mqttcon.client.publish("@msg/pump/pump1","off")
        elif (mixer == 0 and pump1==0):
            if(ec <= (valueveget['ec']-1)):
                fertilizer = (ec - valueveget['ec'])*level #คำนวนหาจำนวนที่ต้องใช้ปุ๋ย
                fertilizerml = fertilizer * 1000
                Mqttcon.client.publish("@msg/fertilizer/fertilizer1/control",fertilizerml)#เติมปุ๋ยที่ยังไม่ผสม
                Mqttcon.client.publish("@msg/pump/pump2","on")
                if(ph <= (valueveget['ph']-1)):#phต่ำ
                    waterml = ((fertilizerml/20)/2)/(ph-valueveget['ph'])#คำนวนหาน้ำที่ต้องเติมตามค่า ph
                else:
                    waterml = (fertilizerml/20)/2 #คำนวนหาน้ำที่ต้องเติม
                Mqttcon.client.publish("@msg/fertilizer/water/control",waterml)#เติมน้ำเพื่อผสม
                Mqttcon.client.publish("@msg/pump/pump1","on")
                Mqttcon.client.publish("@msg/htdroponic/htdroponic1","on")
                Mqttcon.client.publish("@msg/greenHouse/flowfertilizer2/flow",fertilizerml)#เติมปุ๋ยที่ผสมแล้ว
                Mqttcon.client.publish("@msg/greenHouse/flowfertilizer2/flow",3000)#เติมน้ำล้างท่อ
                Mqttcon.client.publish("@msg/htdroponic/htdroponic1","off")
                return True
                
            elif(ec >= (valueveget['ec']+1)):
                water=ec-valueveget['ec']#คำนวนปริมาณเพื่อเจือจาง
                Mqttcon.client.publish("@msg/htdroponic/htdroponic1","on")
                Mqttcon.client.publish("@msg/greenHouse/water","on")
                Mqttcon.client.publish("@msg/greenHouse/flowfertilizer2/flow",water)#เติมน้ำเพื่อนเจือจาง
                Mqttcon.client.publish("@msg/pump/pump1","on")
                Mqttcon.client.publish("@msg/htdroponic/htdroponic1","off")
                return True
        return False