import paho.mqtt.client as mqtt
class Mqttcon:
    client = None
    
    @classmethod
    def connect(cls):
        cls.client = mqtt.Client("serverHydro")                           #create client object
        cls.client.connect("192.168.31.41",1883)                                 #establish connection 
        return True  
    
    
    
    

