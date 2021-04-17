import paho.mqtt.client as mqtt
import time
from datetime import datetime, date
from connectDB import ConnectDB

today = date.today()
now = datetime.now()
topic_list = [
    ('@msg/greenhouse/#', 0),
    # ('@msg/greenHouse/OS/OPEN', 0),
    # ('@msg/greenHouse/OS/CLOSE', 0),
    # ('@msg/greenHouse/IS/OPEN', 0),
    # ('@msg/greenHouse/IS/CLOSE', 0),
    ('@msg/hydroponic/light/red', 0),
    ('@msg/hydroponic/light/all', 0),
    ('@msg/fertilizer/bug1/control', 0),
    ('@msg/fertilizer/bug2/control', 0),
    ('@msg/fertilizer/bug3/control', 0),
    ('@msg/fertilizer/fertilizer1/control', 0),
    ('@msg/fertilizer/fertilizer2/control', 0),
    ('@msg/fertilizer/fertilizer3/control', 0),
]

def on_message(client, userdata, message):
    print("message topic=",message.topic)
    msg = str(message.payload.decode("utf-8"))
    print(msg)
    return
    if (message.topic == topic_list[0][0]):
        print("test1")
        #ConnectDB.set_status(0,"sunscreenOUT",0)
    elif (message.topic == topic_list[1][0]):
        print("test2")
        #ConnectDB.set_status(1,"sunscreenOUT",0)
    elif (message.topic == topic_list[2][0]):
        print("test3")
        #ConnectDB.set_status(1,"sunscreenIN",0)
    elif (message.topic == topic_list[4][0]):
        print("test4")
        #ConnectDB.set_status(1,"light",1111111)
    elif (message.topic == topic_list[5][0]):
        ConnectDB.set_status(0,"light",1111111)
    elif (message.topic == topic_list[6][0] 
    or message.topic == topic_list[7][0] 
    or message.topic == topic_list[8][0]):
        ConnectDB.set_status(1,"mixer",0)
    elif (message.topic == topic_list[8][0]
    or message.topic == topic_list[9][0]
    or message.topic == topic_list[10][0]):
        ConnectDB.set_status(0,"mixer",0)

    print("message received " ,msg)  
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    print("Current  =", current_time, current_date)
broker_address="127.0.0.1"
print("creating new instance")
client = mqtt.Client("RASPI") #create new instance
# client.username_pw_set("mymqtt", "myraspi")
client.on_message = on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","test")
client.subscribe(topic_list)

while(True):
    #print("Publishing message to topic","mynew/test")
    #client.publish("mynew/test","LEDOFF")
    time.sleep(2) # wait

client.loop_stop() #stop the loop
