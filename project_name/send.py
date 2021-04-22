#!/usr/bin/env python
from mqttsend import Mqttcon
Mqttcon.connect()
client = Mqttcon.client
client.publish("@msg/greenHouse/IS/CLOSE","on")  

