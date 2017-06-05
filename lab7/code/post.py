import os
import pygame
import time

import sys
import Adafruit_DHT
import requests

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
sensor = sensor_args['11']
pin = 4

h1, t1 = Adafruit_DHT.read_retry(sensor, pin)

payload = {
        'sensor': 1,
        'Temp': 10.0,
        'Humi': 10.0
        }

r = requests.post(localhost, data=payload)
# r = requests.post('http://10.0.1.33', data=payload)
