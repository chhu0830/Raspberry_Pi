# Simple demo of of the ADXL346 accelerometer library.  Will print the X, Y, Z
# Axis acceleration values every half second.
# Author: Tony DiCola
# License: Public Domain
from __future__ import print_function
import time,sys, os, thread, random, requests, smbus

# Import the ADXL345 module.
import Adafruit_ADXL345

# Import BMP085 module
import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

# Import HMC5883L
bus = smbus.SMBus(1)
addrHMC = 0x1e

def read_word(address, adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr + 1)
    val = (high << 8) + low
    return val

def read_word_2c(address, adr):
    val = read_word(address, adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

# Import L3G4200D module
import smbus
import string
import math

#converts 16 bit two's compliment reading to signed int
def getSignedNumber(number):
    if number & (1 << 15):
        return number | ~65535
    else:
        return number & 65535

#open /dev/i2c-1
i2c_bus=smbus.SMBus(1)
#i2c slave address of the L3G4200D
i2c_address=0x69

#initialise the L3G4200D

#normal mode and all axes on to control reg1
i2c_bus.write_byte_data(i2c_address,0x20,0x0F)
#full 2000dps to control reg4
i2c_bus.write_byte_data(i2c_address,0x23,0x20)


# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()

# Alternatively you can specify the device address and I2C bus with parameters:
#accel = Adafruit_ADXL345.ADXL345(address=0x54, busnum=2)

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()

    #gyro.py code
    i2c_bus.write_byte(i2c_address,0x28)
    X_L = i2c_bus.read_byte(i2c_address)
    i2c_bus.write_byte(i2c_address,0x29)
    X_H = i2c_bus.read_byte(i2c_address)
    X = X_H << 8 | X_L

    i2c_bus.write_byte(i2c_address,0x2A)
    Y_L = i2c_bus.read_byte(i2c_address)
    i2c_bus.write_byte(i2c_address,0x2B)
    Y_H = i2c_bus.read_byte(i2c_address)
    Y = Y_H << 8 | Y_L

    i2c_bus.write_byte(i2c_address,0x2C)
    Z_L = i2c_bus.read_byte(i2c_address)
    i2c_bus.write_byte(i2c_address,0x2D)
    Z_H = i2c_bus.read_byte(i2c_address)
    Z = Z_H << 8 | Z_L

    X = getSignedNumber(X)
    Y = getSignedNumber(Y)
    Z = getSignedNumber(Z)
    X = (X*8.75)/1000
    Y = (Y*8.75)/1000
    Z = (Z*8.75)/1000

    #Import compass.py
    bus.write_byte_data(addrHMC, 0, 0b01110000)
    bus.write_byte_data(addrHMC, 1, 0b00100000)
    bus.write_byte_data(addrHMC, 2, 0b00000000)

    mag_x = read_word_2c(addrHMC, 3)
    mag_y = read_word_2c(addrHMC, 7)
    mag_z = read_word_2c(addrHMC, 5)

    print('ACC: x:{0} y:{1} z:{2}; '.format(x, y, z), end='')
    print('H:{0:0.2f}m; '.format(sensor.read_altitude()), end='')
    print('GYPO:x:{0} y:{1} z:{2}; '.format(X, Y, Z), end='')
    print('MAG:x:{0} y:{1} z:{2}'.format(mag_x, mag_y, mag_z))
    # Wait half a second and repeat.
    time.sleep(1.0)
