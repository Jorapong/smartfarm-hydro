#!/usr/bin/env python
from connectDB import ConnectDB
ConnectDB.connect()
print(ConnectDB.get_light(11111111)['ph'])

