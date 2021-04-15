from connectDB import ConnectDB
ConnectDB.connect()
class ConnectDB:
    _cursor = None
    @classmethod
    def connect(cls):
        mydb = MySQLdb.connect(host="localhost",user="root",password="",database="farm_db")
        cls._cursor = mydb.cursor(MySQLdb.cursors.DictCursor)
        # return mycursor
    
    @classmethod
    def get_status(cls,name):
        cls._cursor.execute("SELECT "+name+" FROM status where veget_id=")
        myresult = mycursor.fetchall()
        return myresult
    
    @classmethod
    def get_statusveget(cls,name,veget_id):
        cls._cursor.execute("SELECT "+name+" FROM status where veget_id=")
        myresult = mycursor.fetchall()
        return myresult

    @classmethod
    def get_light(cls,veget_id):
        sql = "SELECT * FROM sensor_value where sensorv_id={}".format(veget_id)
        cls._cursor.execute(sql)
        return cls._cursor.fetchone()

    @classmethod
    def get_SunscreenOstt(cls):
        cls._cursor.execute("SELECT sunscreenO FROM status")
        myresult = mycursor.fetchall()
        for row in myresult:
            if row[0]==0:
                return False
            elif row[0]==1:
                return True
        return False
    
    @classmethod
    def get_SunscreenIstt(cls):
        cls._cursor.execute("SELECT sunscreenI FROM status")
        myresult = mycursor.fetchall()
        for row in myresult:
            if row[0]==0:
                return False
            elif row[0]==1:
                return True
        return False

    @classmethod
    def get_lightstt(cls):
        cls._cursor.execute("SELECT lightstt FROM status")
        myresult = mycursor.fetchall()
        for row in myresult:
            if row[0]==0:
                return False
            elif row[0]==1:
                return True
        return False
    
        @classmethod
    def get_ec(cls):
        cls._cursor.execute("SELECT ec FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            ec = row[0]
        return ec

    @classmethod
    def get_ph(cls):
        cls._cursor.execute("SELECT ph FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            ph = row[0]
        return ph
    
    @classmethod
    def get_level(cls):
        cls._cursor.execute("SELECT level FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            level = row[0]
        return level