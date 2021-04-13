import MySQLdb
import paho.mqtt.client as mqtt
import sys
import time
import json
import ast
from datetime import datetime, date

today = date.today()
now = datetime.now()
mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    password="1234",
    database="farm_db"
)
def on_message(client, userdata, message):
    text = str(message.payload.decode("utf-8"))
    text2=text.split("/")
    print(text2)
    if text2[0] == "Sensor":
        valjs = ast.literal_eval(text2[1])
        mycursor = mydb.cursor()
        sql = "UPDATE sensor_value SET ph=%s, ec=%s, flow_pump=%s, light=%s, temp=%s, level=%s where sensorv_id=%s"
        valsql = (valjs["ph"],valjs["ec"], valjs["flowpump"], valjs["light"], valjs["temp"], valjs["level"],valjs["Sensor"])
        print(valsql)
        mycursor.execute(sql, valsql)
        mydb.commit()
        print(mycursor.rowcount, "record updated.")
    print("message received " ,text)  
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    print("Current  =", current_time, current_date)
broker_address="192.168.31.49"
print("creating new instance")
client = mqtt.Client("RASPI") #create new instance
client.username_pw_set("mymqtt", "myraspi")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","hidro/sensor")
client.subscribe("hidro/sensor")

while(True):
    #print("Publishing message to topic","mynew/test")
    #client.publish("mynew/test","LEDOFF")
    time.sleep(4) # wait

client.loop_stop() #stop the loop
