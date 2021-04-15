from connectDB import ConnectDB
ConnectDB.connect()
class Fertilizer:

    @classmethod
    def process_fertilizer(self,veget_id):
        ec = self.get_ec(veget_id)
        ph = self.get_ph(veget_id)
        level = seft.get_level(veget_id)
        return ec * ph
