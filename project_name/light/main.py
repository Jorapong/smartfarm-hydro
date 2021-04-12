class Light:
    @classmethod
    def get_light(self):
        # statements
        return 100

    @classmethod
    def process_light(self, house_id):
        print('calculating houst id = {}'.format(house_id))

        value = 1  # get_api(house_id)
        light = self.get_light()

        light *= value

        if light > 1000:
            return True

        return False

    def switch(state):
        # mcu.command(state)
        pass
