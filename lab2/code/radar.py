#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

import sys
import time

import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
v = 343
TRIGGER_PIN = 18
ECHO_PIN = 16
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end - pulse_start
    d = t*v
    d = d/2
    return d*100

def led(t):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(t)    
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(t)
    
# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    v += (temperature - 20) * 0.6
    dis = measure()
    print(dis)
    if dis<15:
        led(0.5)
    elif dis<30:
        led(1.0) 
    else:
        time.sleep(1)
