from connectDB import ConnectDB
ConnectDB.connect()
class Fertilizer:
    broker="127.0.0.1"
    port=1883
    @classmethod
    def process_fertilizer(self,veget_id):
        ec = ConnectDB.get_sensorvalue("ec",veget_id)
        ph = ConnectDB.get_sensorvalue("ph",veget_id)
        level = ConnectDB.get_sensorvalue("level",veget_id)
        
        return False
