#!/usr/bin/env python
from mqttsend import Mqttcon
Mqttcon.connect()
Mqttcon.publish("msg/greenHouse/OS/CLOSE","on")  

