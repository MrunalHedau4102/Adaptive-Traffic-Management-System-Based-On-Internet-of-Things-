import RPi.GPIO as GPIO
import time
import traffic_switching_new as t
counter=t.main()
GPIO.setmode(GPIO.BCM)

# Relay 1
GPIO.setup(21, GPIO.OUT) #Red=21
# Relay 2
GPIO.setup(26, GPIO.OUT) #green_sound
# Relay 3
GPIO.setup(20, GPIO.OUT) #yellow

GPIO.setup(16, GPIO.OUT) #Red
# Relay 2
GPIO.setup(19, GPIO.OUT) #green
# Relay 3
GPIO.setup(13, GPIO.OUT) #yellow


try:
    n=5
    while True:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        
        print('Relay 1 ON')
        time.sleep(counter)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        print('Relay 1 OFF')
        
        GPIO.output(20, GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
    
        print('Relay 2 ON')
        time.sleep(counter)
        
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        print('Relay 2 OFF')
        
        
        GPIO.output(21, GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
       
        
        print('Relay 2 ON')
        time.sleep(counter)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        print('Relay 2 OFF')
        
finally:
    GPIO.cleanup()
