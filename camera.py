from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
sleep(2)
camera.capture('newImage1.jpg')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
sleep(0.1)
print ("LED off")
GPIO.output(18,GPIO.LOW)
GPIO.setwarnings(False)
camera.stop_preview()
