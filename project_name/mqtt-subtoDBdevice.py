import paho.mqtt.client as mqtt
import time
from datetime import datetime, date
from connectDB import ConnectDB

today = date.today()
now = datetime.now()
topic_list = [
    ('@msg/greenHouse/OS/OPEN', 0),
    ('@msg/greenHouse/OS/CLOSE', 0),
    ('@msg/greenHouse/IS/OPEN', 0),
    ('@msg/greenHouse/IS/CLOSE', 0),
    ('@msg/hydroponic/light/red', 0),
    ('@msg/hydroponic/light/all', 0)
]

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    if (message.topic == topic_list[0][0]): 
        ConnectDB.set_status(0,"sunscreenOUT",0)
    elif (message.topic == topic_list[1][1]):
        ConnectDB.set_status(1,"sunscreenOUT",0)
    elif (message.topic == topic_list[2][2]):
        ConnectDB.set_status(0,"sunscreenIN",0)
    elif (message.topic == topic_list[3][3]):
        ConnectDB.set_status(1,"sunscreenIN",0)
    elif (message.topic == topic_list[4][4]):
        ConnectDB.set_status(1,"light",1111111)
    elif (message.topic == topic_list[5][5]):
        ConnectDB.set_status(0,"light",1111111)
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
client.on_message=on_message #attach function to callback
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
