import requests
import json
import MySQLdb
import time
mydb = MySQLdb.connect(host="localhost",user="root",password="",database="farm_db")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM status")
myresult = mycursor.fetchall()
for i in myresult:
    print (i)