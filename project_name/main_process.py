#!/usr/bin/env python
import MySQLdb
import requests
from time import sleep
from fertilizer import Fertilizer
from light import Light
from connectDB import ConnectDB
ConnectDB.connect()
def main():
    while True:
        ConnectDB._cursor.execute("SELECT veget_id FROM veget")
        myresult = mycursor.fetchall()
        for veget_id in myresult:
            print('main')
            fertilizer_result = Fertilizer.process_fertilizer()
            light_result = Light.process_light(veget_id[0])
            print('fertilizer_result', fertilizer_result)
            print('light_result', light_result)

            Light.switch(1)

        sleep(3)

        print('this is main process')
        print('this is main process from Pi')



if __name__ == '__main__':
    main()
