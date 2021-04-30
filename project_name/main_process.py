#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from time import sleep
# from fertilizer import Fertilizer
from light import Light
from connectDB import ConnectDB
ConnectDB.connect()
def main():
    while True:
        # try :
        ConnectDB._cursor.execute("SELECT * FROM veget")
        myresult = ConnectDB._cursor.fetchall()
        for value in myresult:
            print('main')
            veget_id=value['veget_id']
            print('light work')
            light_result = Light.process_light(veget_id)
            print('fertilizer work')
            # fertilizer_result = Light.process_fertilizer(value)
            print('light_result', light_result)
            # print('fertilizer_result', fertilizer_result)
            sleep(60*10)
        print('this is main process from Pi')
            
        # except:
        #     print('error main process')
if __name__ == '__main__':
    main()
