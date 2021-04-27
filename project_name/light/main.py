
from connectDB import ConnectDB
ConnectDB.connect()
from time import sleep
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
        elif light <= 90 and light >= 70:
            client.publish("@msg/greenHouse/OS/OPEN","on")
            #ClosesunscreenOUT
            print('ปิดสแลนด้านใน')
            client.publish("@msg/greenHouse/IS/CLOSE","on")
        elif light > 90 : #แสงน้อย
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

    @classmethod 
    def process_fertilizer(cls,veget):
        ConnectDB.get_values("light",veget['veget_id'])
        ec = ConnectDB.get_values("ec",veget['veget_id'])+0.1 #ec ที่วัดได้ 0.7
        ph = ConnectDB.get_values("ph",veget['veget_id']) #pH ที่วัดได้
        valueveget = ConnectDB.get_valueveget(veget['veget_id']) #ค่า ที่ต้องการ 1
        fertilizerintense = ConnectDB.get_fertilizer(veget['fertilizer_id']) #ความเข้มข้นปุ๋ย 0.1 100ml/1000
        level = ConnectDB.get_values("level",veget['veget_id']) #ระดับน้ำ
        mixer = ConnectDB.get_status(6,0) #สถานะถังน้ำ
        pump1 = ConnectDB.get_status(1,0) #สถานะถังน้ำ
        print('ค่า',ec)
        print('ค่าที่ต้องการ',valueveget['ec'])
        if(ec <= (valueveget['ec']-0.1)):
            fertilizersum = (valueveget['ec']-ec)*(100000) #คำนวนหาจำนวนที่ต้องใช้ปุ๋ย
            fertilizerpre = (fertilizersum+3000)/2
            print('ปุ๋ยที่ต้องเติม',fertilizersum)
            # client.publish("@msg/fertilizer/fertilizer1/control",fertilizerpre)#เติมปุ๋ยที่ยังไม่ผสม
            # client.publish("@msg/pump/pump2","on")
            
            print("น้ำที่ผสม",fertilizerpre)
            # client.publish("@msg/fertilizer/water/control",10000)#เติมน้ำเพื่อผสม
            # client.publish("@msg/pump/pump2","on")
            # sleep(90)
            # client.publish("@msg/pump/pump2","off")
            print("เติมน้ำเสร็จ")
            client.publish("@msg/fertilizer", "on")
            client.publish("@msg/hydroponic/hydroponic3","on")
            client.publish("@msg/pump/flow2",10000)#เติมปุ๋ยที่ผสมแล้ว
            # sleep(20)
            # client.publish("@msg/pump/flow2",5000)#เติมน้ำล้างท่อ
            # client.publish("@msg/htdroponic/htdroponic2","off")
            return True
            
        elif(ec >= (valueveget['ec']+0.1)):
            water=ec-valueveget['ec']#คำนวนปริมาณเพื่อเจือจาง
            print("เติมน้ำ",water)
            # client.publish("@msg/htdroponic/htdroponic2","on")
            # client.publish("@msg/greenHouse/water","on")
            # client.publish("@msg/pump/flow2",water)#เติมน้ำเพื่อนเจือจาง
            # client.publish("@msg/pump/pump1","on")
            # client.publish("@msg/htdroponic/htdroponic2","off")
            return True
        return False


