#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import paho.mqtt.client as mqtt
import time
import ast
import json
from datetime import datetime, date
from connectDB import ConnectDB
ConnectDB.connect()

def on_message(client, userdata, message):
    today = date.today()
    now = datetime.now()
    try:
        text = str(message.payload.decode("utf-8"))
        print("message received " ,text)  
        if message.topic == "@msg/hydro/sensor":
            valjs = ast.literal_eval(text)
            valsql = (valjs["ph"]-10,valjs["ec"]/100, valjs["lowpump"], valjs["light"], valjs["temp"], valjs["level"],valjs["Sensor"])
            print(ConnectDB.set_sensorvalue(valsql))
    except :
        print('error sensor')       
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    print("Current  =", current_time, current_date)
    
broker_address="192.168.31.50"
print("creating new instance")
client = mqtt.Client("RASPI") #create new instance
client.username_pw_set("mymqtt", "myraspi")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","@msg/hydro/sensor")
client.subscribe("@msg/hydro/sensor")

while(True):
    #print("Publishing message to topic","mynew/test")
    #client.publish("mynew/test","LEDOFF")
    time.sleep(2) # wait
client.loop_stop() #stop the loop
