import paho.mqtt.client as mqtt #import the client1



def sendmqtt(cls,topic,msg):
    broker_address="192.168.31.41" 
    client = mqtt.Client("P1")
    client.username_pw_set("smartfarm", "123456788")
    client.connect(broker_address)
    client.publish(topic,msg)
    return True


sendmqtt("@msg/gg","test")