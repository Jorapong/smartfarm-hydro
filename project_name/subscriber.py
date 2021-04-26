#!/usr/bin/env python

from datetime import datetime
import paho.mqtt.client as mqtt
from time import sleep

import settings
from pump import Pump
from connectDB import ConnectDB
ConnectDB.connect()
client = mqtt.Client('subscriber')


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe('@msg/#')


def on_subscribe(*args, **kwargs):
    print(args, kwargs)


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
        Pump.handler(pump_id=device_id,value= status)
    elif device_type=='greenHouse':
        if splited_topic[3]=='OPEN':
            starus=1
        elif splited_topic[3]=='CLOSE':
            starus=1
        if splited_topic[2] =="OS":
            ConnectDB.set_status(starus,3)
        if splited_topic[2] =="IS":
            ConnectDB.set_status(starus,4)
    elif device_type=='hydroponic':
        if splited_topic[2]=="light":
            if payload =='on':
                ConnectDB.set_status(1,5)
            if payload =='off':
                ConnectDB.set_status(0,5)
def main():
    print('__subscriber__')

    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    client.connect(**settings.MQTT)
    client.loop_forever()


if __name__ == '__main__':
    main()

