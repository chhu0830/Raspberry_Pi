import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)



while True:
    for i in range(0,3):
        print("LED is short")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)    
        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
    for i in range(0,3):
        print("LED is long")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(3)    
        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1) 
    for i in range(0,3):
        print("LED is short2")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)    
        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

GPIO.cleanup()

