import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Relay 1
GPIO.setup(21, GPIO.OUT)
# Relay 2
GPIO.setup(26, GPIO.OUT)
# Relay 3
GPIO.setup(20, GPIO.OUT)
#Relay 4
#Relay 5
#Relay 6
#Relay 7
#Relay 8
#Relay 9
try:
    while True:
        GPIO.output(21, GPIO.HIGH)
        print('Relay 1 ON')
        time.sleep(1)
        GPIO.output(21, GPIO.LOW)
        print('Relay 1 OFF')
        time.sleep(1)
        GPIO.output(26, GPIO.HIGH)
        print('Relay 2 ON')
        time.sleep(1)
        GPIO.output(26, GPIO.LOW)
        print('Relay 2 OFF')
        time.sleep(1)
        GPIO.output(20, GPIO.HIGH)
        print('Relay 3 ON')
        time.sleep(1)
        GPIO.output(20, GPIO.LOW)
        print('Relay 3 OFF')
        time.sleep(1)
        
        
finally:
    GPIO.cleanup()