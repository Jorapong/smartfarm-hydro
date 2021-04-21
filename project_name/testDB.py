#!/usr/bin/env python
import MySQLdb
import requests
from time import sleep
#from fertilizer import Fertilizer
from light import Light
from connectDB import ConnectDB
ConnectDB.connect()
ConnectDB._cursor.execute("SELECT * FROM veget")
myresult = ConnectDB._cursor.fetchall()
for value in myresult:
    print('main')
    veget_id=value['veget_id']
    print(veget_id)
print('this is main process from Pi')