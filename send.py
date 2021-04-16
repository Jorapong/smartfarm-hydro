import paho.mqtt.client as mqtt
broker="127.0.0.1"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= mqtt.Client("test1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
client1.publish("hidro/sensor","on")    
client1.publish("test/test2","off")    
client1.publish("test/test2","onn")    

