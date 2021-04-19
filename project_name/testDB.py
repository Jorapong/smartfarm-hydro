#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from connectDB import ConnectDB
ConnectDB.connect()
print(ConnectDB.get_fertilizer(1))