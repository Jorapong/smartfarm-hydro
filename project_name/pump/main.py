from datetime import datetime, timedelta
from threading import Event, Thread
from connectDB import ConnectDB
ConnectDB.connect()

class Pump:
    __WAIT_ABORTER = {}

    @classmethod
    def worker(cls, **kwargs):
        pump_id = kwargs.get('pump_id')
        status = cls.get_status(pump_id=pump_id)

        print(f'wait for pump {pump_id} off')
        if int(status) == 0:
            # print('yes status is 0')
            killer_func = cls.__WAIT_ABORTER.get(f'pump-{pump_id}', None)
            # print('killer_func', killer_func)
            if killer_func:
                killer_func() # real kill

            print(f'now pump {pump_id} off, done')
            print(cls.__DATA)

    @classmethod
    def wait_with_timeout(cls, func, **kwargs):
        stopped = Event()
        check_interval = kwargs.get('check_interval')
        timeout = kwargs.get('timeout')
        wait_since = datetime.now()

        def loop():
            while not stopped.wait(check_interval):  # the first call is in `interval` secs
                if timeout > 0:
                    timediff = datetime.now() - wait_since
                    if timediff.seconds >= timeout:
                        print('***** timeout *****')
                        break

                try:
                    func(**kwargs)
                except Exception as e:
                    break
                    # raise Exception(e)
                

            stopped.clear()
            #

        Thread(target=loop).start()
        return stopped.set

    @classmethod
    def control(cls, pump_id, value):
        index = next(
            (index for (index, pump) in enumerate(cls.__DATA) if pump['id'] == pump['id'] == f'pump-{pump_id}'), None
        )
        # print('index', index)
        cls.__DATA[index]['status'] = value
        #pub
        #savedb
        # esp
        return cls.__DATA[index]

    @classmethod
    def __query(cls, pump_id):
        data = filter(lambda pump: pump['id'] == f'pump-{pump_id}', cls.__DATA)
        data = list(data)
        if not len(data):
            return False
        return data[0]

    @classmethod
    def get_status(cls, pump_id):
        pump_object = ConnectDB.get_status(pump_id=pump_id,0)

        # print('pump_object', pump_object)

        if not pump_object:
            return False

        return pump_object.get('status')

    @classmethod
    def handler(cls, pump_id, value):#value= เปิด-ปิด
        
        status = ConnectDB.get_status(pump_id,0)


        if not status and type(status) is bool:
            return

        print(f'pump {pump_id} : status {status} : value {value}')

        if value != status:
            killer_func = cls.__WAIT_ABORTER.get(f'pump-{pump_id}', None)
            # find {'pump-1': object}

            if value == '1':
                if killer_func:
                    del cls.__WAIT_ABORTER[f'pump-{pump_id}']

                killer_func = cls.wait_with_timeout(
                    func=cls.worker,
                    pump_id=pump_id,
                    timeout=30,#sec
                    check_interval=1,#sec
                )
                cls.__WAIT_ABORTER[f'pump-{pump_id}'] = killer_func
                # print('thread_object', thread_object)

            elif value == '0':
                pass
                # if stopper:
                #     stopper()
                #     del cls.__WAIT_ABORTER[f'pump-{pump_id}']

            result = cls.control(pump_id=pump_id, value=value)
            print('control result', result)
            # print(cls.__DATA)
        else:
            print('device already', value)
