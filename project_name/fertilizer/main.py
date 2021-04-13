class Fertilizer:
    @classmethod
    def get_ec(self):
        mycursor = ConnectDB.mycursor()
        mycursor.execute("SELECT ec FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            ec = row[0]
        return ec

    @classmethod
    def get_ph(self):
        mycursor = ConnectDB.mycursor()
        mycursor.execute("SELECT ph FROM sensor_value where veget_id="+veget_id)
        myresult = mycursor.fetchall()
        for row in myresult:
            ph = row[0]
        return ph

    @classmethod
    def process_fertilizer(self,veget_id):

        ec = self.get_ec(veget_id)
        ph = self.get_ph(veget_id)

        return ec * ph
