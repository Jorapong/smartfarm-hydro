import time
import runpy
import MySQLdb

mydb = MySQLdb.connect(host="localhost",user="root",password="1234",database="farm_db")
mycursor = mydb.cursor()
mycursor.execute("SELECT ph,ec,light FROM sensor_value where sensorv_id=11")
myresult = mycursor.fetchall()
print(myresult)
ph=0.0
ec=0.0
light=0.0
for x in myresult:
    ph=x[0]
    ec=x[1]
    light=x[2]
sql = "UPDATE summary_value SET ph = %s,ec=%s,light=%s WHERE sammary_id=11212332"
val = (ph, ec, light)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record update.")