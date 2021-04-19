from connectDB import ConnectDB
from mqttsend import Mqttcon
import json
Mqttcon.connect()
ConnectDB.connect()
Mqttcon.client.loop_start()
Flow = None
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    if ()
class Fertilizer:
    broker="127.0.0.1"
    port=1883
    topicflow = ConnectDB.get_sensorvalue("topicflow",veget_id)
    Mqttcon.client.subscribe('@msg/evthin')


    @classmethod
    def process_fertilizer(self,veget):
        ec = ConnectDB.get_sensorvalue("ec",veget['sensorv_id']) #ec ที่วัดได้
        ph = ConnectDB.get_sensorvalue("ph",veget['sensorv_id']) #pH ที่วัดได้
        valueveget = ConnectDB.get_valueveget(veget['veget_id']) #ค่า ที่ต้องการ
        fertilizerintense = ConnectDB.get_fertilizer(veget['fertilizer_id']) #ความเข้มข้นปุ๋ย
        level = ConnectDB.get_sensorvalue("level",veget['veget_id']) #ระดับน้ำ
        mixer = ConnectDB.get_sensorvalue("mixer",0) #สถานะถังน้ำ
        if  (mixer == 1):
            #ปล่อยนำทื้ง
            Mqttcon.client.publish("@msg/pump/pump1","on")
            Mqttcon.client.on_message = on_message
            Mqttcon.client.publish("@msg/pump/pump1","off")
        elif (mixer == 0):
            if(ec <= (valueveget['ec']-1)):
                fertilizer = (ec - valueveget['ec'])level
                fertilizerml = fertilizer * 1000
                Mqttcon.client.publish("@msg/fertilizer/fertilizer1/control",fertilizerml)
                Mqttcon.client.publish("@msg/pump/pump2","on")
                waterml = (fertilizerml/20)/2
                Mqttcon.client.publish("@msg/fertilizer/water/control",waterml)
                Mqttcon.client.publish("@msg/pump/pump1","on")
            elif(ec >= (valueveget['ec']+1):
                Mqttcon.client.publish("@msg/fertilizer/fertilizer1/control",fertilizerml)
                Mqttcon.client.publish("@msg/pump/pump2","on")
                waterml = (fertilizerml/20)/2
                Mqttcon.client.publish("@msg/fertilizer/water/control",waterml)
                Mqttcon.client.publish("@msg/pump/pump1","on")
        return False