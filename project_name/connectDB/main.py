import MySQLdb
import requests
import time
from datetime import date
class ConnectDB:
    _cursor = None
    _mydb = None
    @classmethod
    def connect(cls):
        cls._mydb = MySQLdb.connect(host="localhost",user="root",password="1234",database="farm_db")
        cls._cursor = cls._mydb.cursor(MySQLdb.cursors.DictCursor)
        # return mycursor
    
    @classmethod
    def get_status(cls,name,veget_id):
        cls._cursor.execute("SELECT * FROM status where veget_id="+veget_id+" AND name ="+name)
        myresult = cls._cursor.fetchall()
        return myresult    
    
    @classmethod
    def get_values(cls,value,veget_id):
        sql ="SELECT {} FROM sensor_value where veget_id={}".format(value,veget_id)
        cls._cursor.execute(sql)
        myresult = cls._cursor.fetchone()
        return myresult[value]    
    
    @classmethod
    def set_status(cls,value,name,veget_id):
        setstatus =(value,name,veget_id)
        cls._cursor.execute("UPDATE name=%s FROM status where name =%s AND veget_id=%s",setstatus)
        cls._cursor.fetchall()
        cls._mydb.commit()
        return (ConnectDB._cursor.rowcount,"record "+name+" Update")
    
    @classmethod
    def set_sensorvalue(cls,value):
        cls._cursor.execute("UPDATE sensor_value SET ph=%s, ec=%s, flow_pump=%s, light=%s, temp=%s, level=%s where sensorv_id=%s",value)
        myresult = cls._cursor.fetchall()
        cls._mydb.commit()
        return (ConnectDB._cursor.rowcount,"record sensor_id "+str(value[6])+" Update")

    @classmethod
    def get_valueveget(cls,veget_id):
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        sql = 'select * from veget_value where veget_id={} and date <= "{}" order by date desc'.format(veget_id, current_date)
        cls._cursor.execute(sql)
        myresult = ConnectDB._cursor.fetchone()
        if myresult.get('vegetv_id',None):
            return myresult
        return False 

    @classmethod
    def get_fertilizer(cls,fertilizer_id):
        sql = "SELECT * FROM fertilizer where fertilizer_id={}".format(fertilizer_id)
        cls._cursor.execute(sql)
        myresult = cls._cursor.fetchone()
        return myresult  
