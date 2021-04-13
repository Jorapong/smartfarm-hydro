#!/usr/bin/python
#-*-coding:utf-8 -*-
import requests
import json
import MySQLdb
import time
mydb = MySQLdb.connect(host="localhost",user="root",password="1234",database="farm_db")
mycursor = mydb.cursor()
mycursor.execute("SELECT light FROM sensor_value")
myresult = mycursor.fetchall()
for x in myresult:
    print("light value :"+str(x[0]))
    if x[0] > 300:
        print('เปิดไฟ')
        url = 'https://api.netpie.io/v2/device/message?topic=hydroponic1/light/blue'
        data = "on"
        headers = {'Authorization': 'Device d14597cd-eeb5-4e8e-b737-75a33fdc1f3d:XB3k4zGfKjvHXazRXu8fa8fiZ2hsZq6c', "Content-Type": "text/plain", data:data}
        response = requests.put(url, data=data, headers=headers)
        print(response.text)
        url = 'https://api.netpie.io/v2/device/message?topic=hydroponic1/light/red'
        data = "on"
        headers = {'Authorization': 'Device d14597cd-eeb5-4e8e-b737-75a33fdc1f3d:XB3k4zGfKjvHXazRXu8fa8fiZ2hsZq6c', "Content-Type": "text/plain", data:data}
        response = requests.put(url, data=data, headers=headers)
        print(response.text)
    elif x[0] < 300:
        print("ปิดไฟ")
        url = 'https://api.netpie.io/v2/device/message?topic=hydroponic1/light/blue'
        data = "off"
        headers = {'Authorization': 'Device d14597cd-eeb5-4e8e-b737-75a33fdc1f3d:XB3k4zGfKjvHXazRXu8fa8fiZ2hsZq6c', "Content-Type": "text/plain", data:data}
        response = requests.put(url, data=data, headers=headers)
        print(response.text)
        url = 'https://api.netpie.io/v2/device/message?topic=hydroponic1/light/red'
        data = "off"
        headers = {'Authorization': 'Device d14597cd-eeb5-4e8e-b737-75a33fdc1f3d:XB3k4zGfKjvHXazRXu8fa8fiZ2hsZq6c', "Content-Type": "text/plain", data:data}
        response = requests.put(url, data=data, headers=headers)
        print(response.text)
    elif x[0] < 300:
        print("ปิดสแลน")

    