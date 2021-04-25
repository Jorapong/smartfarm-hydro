#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import paho.mqtt.client as mqtt
import time
from datetime import datetime, date
from connectDB import ConnectDB
ConnectDB.connect()
today = date.today()
now = datetime.now()
topic_list = [
    ('@msg/#', 0),
    ('@msg/hydroponic/light/#', 0),
    ('@msg/fertilizer/bug1/control', 0),
    ('@msg/fertilizer/bug2/control', 0),
    ('@msg/fertilizer/bug3/control', 0),
    ('@msg/fertilizer/fertilizer1/control', 0),
    ('@msg/fertilizer/fertilizer2/control', 0),
    ('@msg/fertilizer/fertilizer3/control', 0)
]

def on_message(client, userdata, message):
    try:
        msg = str(message.payload.decode("utf-8"))
        if (message.topic == '@msg/greenHouse/OS/OPEN'):
            ConnectDB.set_status(1,3)

        elif (message.topic == '@msg/greenHouse/OS/CLOSE'):
            ConnectDB.set_status(0,3)

        elif (message.topic == '@msg/greenHouse/IS/OPEN'):
            ConnectDB.set_status(1,4)

        elif (message.topic == '@msg/greenHouse/IS/CLOSE'):
            ConnectDB.set_status(0,4)

        elif (message.topic == topic_list[1][0]and msg=="on"):
            ConnectDB.set_status(1,5)

        elif (message.topic == topic_list[1][0]and msg=="off"):
            ConnectDB.set_status(0,5)

        elif (message.topic == topic_list[2][0] 
        or message.topic == topic_list[3][0] 
        or message.topic == topic_list[4][0]):
            ConnectDB.set_status(1,6)

        elif (message.topic == topic_list[5][0]
        or message.topic == topic_list[6][0]
        or message.topic == topic_list[7][0]):
            ConnectDB.set_status(0,6)

        elif (message.topic == '@msg/pump/pump1' and msg=="on"):
            ConnectDB.set_status(1,1)

        elif (message.topic == '@msg/pump/pump1' and msg=="off"):
            ConnectDB.set_status(0,1)

        elif (message.topic == '@msg/pump/pump2' and msg=="on"):
            ConnectDB.set_status(1,2)

        elif (message.topic == '@msg/pump/pump2' and msg=="off"):
            ConnectDB.set_status(0,2)
            
        print("message received " ,msg)  
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)
        current_time = now.strftime("%H:%M:%S")
        current_date = today.strftime("%d/%m/%Y")
        print("Current  =", current_time, current_date)
    broker_address="192.168.31.41"
    print("creating new instance")
    client = mqtt.Client("RASPI") #create new instance
    client.username_pw_set("smartfarm", "123456788")
    client.on_message = on_message #attach function to callback
    print("connecting to broker")
    client.connect(broker_address) #connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","test")
    client.subscribe(topic_list)
    except:
        print("error M qtt")

while(True):
    #print("Publishing message to topic","mynew/test")
    #client.publish("mynew/test","LEDOFF")
    time.sleep(2) # wait

client.loop_stop() #stop the loop
