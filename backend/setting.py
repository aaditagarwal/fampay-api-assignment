import os
import sys
import json

try:
    with open('config.json', 'r') as conf:
        config = json.load(conf)
except:
    with open(sys.argv[1], 'r') as conf:
        config = json.load(conf)

#Hosted URL
HOST_PORT = config.get('HOST_PORT')
HOST_URL = config.get('HOST_URL')

#Time before starting server
SHORT_SLEEP = config.get('SHORT_SLEEP')

#Polling Interval
LONG_SLEEP = config.get('LONG_SLEEP')