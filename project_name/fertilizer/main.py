from connectDB import ConnectDB
from mqttsend import Mqttcon

ConnectDB.connect()
class Fertilizer:
    broker="127.0.0.1"
    port=1883
    @classmethod
    def process_fertilizer(self,veget_id):
        ec = ConnectDB.get_sensorvalue("ec",veget_id)
        ph = ConnectDB.get_sensorvalue("ph",veget_id)
        level = ConnectDB.get_sensorvalue("level",veget_id)
        mixer = ConnectDB.get_sensorvalue("mixer",veget_id)
        if  (mixer == 1):
            #ปล่อยนำทื้ง
            Mqttcon.mqttconnect("@msg/pump/pump1","ON")
            Mqttcon.mqttconnect("@msg/pump/pump1","OFF")
        elif (mixer == 0):
            level = 
            fertilizerml=ec+ec #แก้สูตร
            waterml=ec #แก้สูตร
            Mqttcon.mqttconnect("@msg/fertilizer/fertilizer1/control",fertilizerml)
            Mqttcon.mqttconnect("@msg/fertilizer/water/control",waterml)
            Mqttcon.mqttconnect("@msg/pump/pump1","ON")
        return False
