import paho.mqtt.client as mqtt
class Mqttcon:
    client = None
    @classmethod
    def connect(cls):
        cls.client = mqtt.Client("serverHydro")
        cls.client.connect("192.168.31.41")
        cls.client.username_pw_set("smartfarm", "123456788")
        return True  
        
    @classmethod
    def publish(cls,topic,msg):
        cls.client.publish(topic,msg)
        return True
    
    

