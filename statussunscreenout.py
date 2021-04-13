import MySQLdb
import paho.mqtt.client as mqtt
import sys
import time
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
topic="@msg/greenHouse/OS/OPEN"
broker_address="192.168.31.41"
def on_message(client, userdata, message):
    text = str(message.payload.decode("utf-8"))
    mycursor = mydb.cursor()
    if text=="ON" or text=="OFF":
        sql = "UPDATE status SET status=%s where status_id=%s"
        valsql = (valjs[text],valjs["1234"])
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
print("creating new instance")
client = mqtt.Client("status") #create new instance
client.username_pw_set("smartfarm", "123456788")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic",topic)
client.subscribe(topic)

while(True):
    time.sleep(2) # wait

client.loop_stop() #stop the loop
