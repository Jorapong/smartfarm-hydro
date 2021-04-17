import MySQLdb
import requests
import time
from datetime import date
class ConnectDB:
    _cursor = None
    _mydb = None
    @classmethod
    def connect(cls):
        cls._mydb = MySQLdb.connect(host="localhost",user="root",password="",database="farm_db")
        cls._cursor = cls._mydb.cursor(MySQLdb.cursors.DictCursor)
        # return mycursor
    
    @classmethod
    def get_status(cls,name,veget_id):
        cls._cursor.execute("SELECT * FROM status where veget_id="+veget_id+" AND name ="+name)
        myresult = mycursor.fetchall()
        return myresult
    
    @classmethod
    def get_valuesensor(cls,sensor,veget_id):
        cls._cursor.execute("SELECT "+sensor+" FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            ec = row[0]
        return ec    
    
    @classmethod
    def get_values(cls,sensor,veget_id):
        cls._cursor.execute("SELECT * FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchone()
        for row in myresult:
            ec = row[0]
        return ec    
    
    @classmethod
    def set_status(cls,value,name,veget_id):
        setstatus =(value,name,veget_id)
        ConnectDB._cursor.execute("UPDATE name=%s FROM status where name =%s AND veget_id=%s",setstatus)
        ConnectDB._cursor.fetchall()
        ConnectDB._mydb.commit()
        return (ConnectDB._cursor.rowcount,"record "+name+" Update")
    
    @classmethod
    def set_sensorvalue(cls,value):
        ConnectDB._cursor.execute("UPDATE sensor_value SET ph=%s, ec=%s, flow_pump=%s, light=%s, temp=%s, level=%s where sensorv_id=%s",value)
        myresult = ConnectDB._cursor.fetchall()
        ConnectDB._mydb.commit()
        return (ConnectDB._cursor.rowcount,"record sensor_id "+value['sensor']+" Update")

    @classmethod
    def get_valueveget(cls,veget_id):
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        sql = 'select * from veget_value where veget_id={} and date <= "{}" order by date desc'.format(veget_id, current_date)
        ConnectDB._cursor.execute(sql)
        myresult = ConnectDB._cursor.fetchone()

        if myresult.get('vegetv_id',None):
            return myresult

        return False 