import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
ledPin=17
ledPin1=27
ledPin2=22
GPIO.setup(ledPin,GPIO.OUT)
GPIO.output(ledPin,False)
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.output(ledPin1,False)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.output(ledPin2,False)
try:
    while True:
        GPIO.output(ledPin, True)
        print("LED ON")
        sleep(1)
        GPIO.output(ledPin, False)
        print("LED OFF")
        sleep(1)

        GPIO.output(ledPin1, True)
        print("LED ON")
        sleep(1)
        GPIO.output(ledPin1, False)
        print("LED OFF")
        sleep(1)

        GPIO.output(ledPin2, True)
        print("LED ON")
        sleep(1)
        GPIO.output(ledPin2, False)
        print("LED OFF")
        sleep(1)

finally:
    GPIO.output(ledPin, False)
    GPIO.output(ledPin1, False)
    GPIO.output(ledPin2, False)
    GPIO.cleanup
