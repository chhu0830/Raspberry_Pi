import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This must match in the Arduino Sketch
SLAVE_ADDRESS = 0x04

def request_reading():
    t = bus.read_byte(SLAVE_ADDRESS)
    h = bus.read_byte(SLAVE_ADDRESS)
    m = bus.read_byte(SLAVE_ADDRESS)
    # reading = bus.read_byte(SLAVE_ADDRESS)
    print 'Temp: %.2f, Humi: %.2f, Mois: %d' % (t, h, m)
    if m > 50:
        bus.write_byte(SLAVE_ADDRESS, ord('l'))
    else:
        bus.write_byte(SLAVE_ADDRESS, ord('x'))



while True:
    '''
    command = raw_input("Enter command: l - toggle LED, r - read A0 ")
    if command == 'l' :
        bus.write_byte(SLAVE_ADDRESS, ord('l'))
    elif command == 'r' :
        request_reading()
    '''
    request_reading()
    time.sleep(2)
