import paho.mqtt.client as mqtt
class Mqttcon:
    client = None
    
    def on_publish(client,userdata,result):             #create function for callback
        print("Payload published \n")
        pass
    
    @classmethod
    def mqttconnect(cls,topic,payload):
        client= mqtt.Client("serverHydro")                           #create client object
        client.on_publish = cls.on_publish                          #assign function to callback
        client.connect("127.0.0.1",1883)                                 #establish connection
        client.publish(str(topic),str(payload))  
        return True  
    
    

