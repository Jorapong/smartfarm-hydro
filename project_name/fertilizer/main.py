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
    def process_fertilizer(self,veget_id):
        ec = ConnectDB.get_sensorvalue("ec",veget_id)
        ph = ConnectDB.get_sensorvalue("ph",veget_id)
        level = ConnectDB.get_sensorvalue("level",veget_id)
        mixer = ConnectDB.get_sensorvalue("mixer",veget_id)
        if  (mixer == 1):
            #ปล่อยนำทื้ง
            vid=1
            on_message():
                unsub(/id)
            sub(/id)
            pub
            Mqttcon.client.publish("@msg/pump/pump1","ON")
            Mqttcon.client.on_message = on_message
            Mqttcon.client.publish("@msg/pump/pump1","OFF")
        elif (mixer == 0):
            level = 
            fertilizerml=ec+ec #แก้สูตร
            waterml=ec #แก้สูตร
            Mqttcon.client.publish("@msg/fertilizer/fertilizer1/control",fertilizerml)
            Mqttcon.client.publish("@msg/fertilizer/water/control",waterml)
            Mqttcon.client.publish("@msg/pump/pump1","ON")
        return False