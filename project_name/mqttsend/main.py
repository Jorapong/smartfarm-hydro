import paho.mqtt.client as mqtt
class Mqttcon:
    client = None
    broker_address="192.168.31.41" 
    @classmethod
    def connect(cls):
        cls.client = mqtt.Client("serverHydro")                           #create client object
        cls.client.connect(cls.broker_address)                                 #establish connection
        cls.client.username_pw_set("smartfarm", "123456788")
        return True  
        
    @classmethod
    def publish(cls,topic,msg):
        cls.client.publish(topic,msg)
        return True
    
    

