class Fertilizer:
    @classmethod
    def get_ec(self):
        # statements
        return 1.5

    @classmethod
    def get_ph(self):
        return 5.5

    @classmethod
    def process_fertilizer(self):
        ec = self.get_ec()
        ph = self.get_ph()

        return ec * ph
