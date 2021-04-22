#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import MySQLdb
import requests
from time import sleep
#from fertilizer import Fertilizer
from light import Light
from connectDB import ConnectDB
ConnectDB.connect()
def main():
    while True:
        ConnectDB._cursor.execute("SELECT * FROM veget")
        myresult = ConnectDB._cursor.fetchall()
        for value in myresult:
            print('main')
            veget_id=value['veget_id']
            # fertilizer_result = Fertilizer.process_fertilizer()
            light_result = Light.process_light(veget_id)
            #print('fertilizer_result', fertilizer_result)
            print('light_result', light_result)
        print('this is main process from Pi')
        sleep(60)

if __name__ == '__main__':
    main()
