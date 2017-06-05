# Simple demo of of the ADXL346 accelerometer library.  Will print the X, Y, Z
# Axis acceleration values every half second.
# Author: Tony DiCola
# License: Public Domain
from __future__ import print_function
import time,sys, os, thread, random, requests, smbus, math

# Import the ADXL345 module.
import Adafruit_ADXL345

# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()

# Alternatively you can specify the device address and I2C bus with parameters:
#accel = Adafruit_ADXL345.ADXL345(address=0x54, busnum=2)

norm_before = 0
print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()

    norm = math.sqrt(x*x+y*y+z*z)

    if norm_before == 0:
        norm_after = norm
    else:
        norm_after = (norm + norm_before) / 2.0
    print('{0},{1}'.format(norm, norm_after))
    norm_before = norm_after
    # Wait half a second and repeat.
    time.sleep(1.0)
