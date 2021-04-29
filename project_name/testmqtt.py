import paho.mqtt.client as mqtt #import the client1
from time import sleep
broker_address="192.168.31.41" 
client = mqtt.Client("P1")
client.username_pw_set("smartfarm", "123456788")
client.connect(broker_address)
client.publish("@msg/test","on")
print('tset1')
sleep(100)
broker_address="192.168.31.41" 
client = mqtt.Client("P1")
client.username_pw_set("smartfarm", "123456788")
client.connect(broker_address)
client.publish("@msg/test","off")
print('tset')