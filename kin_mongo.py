#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymongo
from pymongo import MongoClient
import json

client = MongoClient('127.0.0.1', 27017)
db = client['domingo']
db.create_collection('client_info_all', {'autoIndexId':True})

c_info_all = db['client_info_all']
c_info_all.create_index('g_uid', unique=True)



