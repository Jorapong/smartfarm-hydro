#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import paho.mqtt.client as mqtt
import time
from datetime import datetime, date
from connectDB import ConnectDB
ConnectDB.connect()
today = date.today()
now = datetime.now()
def on_message(client, userdata, msg):
    print(client,userdata,msg)
    topic = msg.topic

    if not topic:
        return

    splited_topic = topic.split('/')

    if splited_topic[0] != '@msg':
        print(f'we not interested in topic {splited_topic[0]}')
        return
    try:
        payload = msg.payload.decode('utf-8')
    except:
        print('decode payload error')
        return

    print(datetime.now(), '#', topic, payload)

    device_type = splited_topic[1]
    value = payload

    if device_type == 'pump':
        if splited_topic[2]=="pump1":
            device_id = 1
        elif splited_topic[2]=="pump2":
            device_id = 2
        if(value == 'on'):
            status = 1
        else:
            status = 0
        ConnectDB.set_status(status,device_id)
    elif device_type=='greenHouse':
        if splited_topic[3]=='OPEN':
            status=1
        elif splited_topic[3]=='CLOSE':
            status=1
        if splited_topic[2] =="OS":
            ConnectDB.set_status(status,3)
        if splited_topic[2] =="IS":
            ConnectDB.set_status(status,4)
    elif device_type=='hydroponic':
        if splited_topic[2]=="light":
            if payload =='on':
                ConnectDB.set_status(1,5)
            if payload =='off':
                ConnectDB.set_status(0,5)
broker_address="192.168.31.41"
print("creating new instance")
client = mqtt.Client("RASPI") #create new instance
client.username_pw_set("smartfarm", "123456788")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","@msg/#")
client.subscribe("@msg/#")

while(True):
    #print("Publishing message to topic","mynew/test")
    #client.publish("mynew/test","LEDOFF")
    time.sleep(2) # wait

client.loop_stop() #stop the loop
