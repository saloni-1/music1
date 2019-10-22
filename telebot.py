import sys
import time
from time import sleep
import random
import datetime
import telepot
import RPi.GPIO as GPIO
try:
    now=datetime.datetime.now()
    GPIO.setwarnings (False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22,False)
    def handle(msg):
        chat_id=msg['chat']['id']
        command=msg['text']
        print('Got command: %s'% command)
        if command=='Hi':
            bot.sendMessage(chat_id,str("Hi! CSC"))
        elif command=='aur batao':
            bot.sendMessage(chat_id,str("Hi! CfgzdfSFSC"))
        elif command=='file':
             bot.sendDocument(chat_id,document=open('/home/pi/telebot.py'))
        elif command=='time':
             bot.sendMessage(chat_id,str(now.hour)+str(":")+str(now.minute))
        elif command=='logo':
              bot.sendphoto(chat_it,photo="http://www.iotleague.com/wp-content/uploads/2015/11/Iot.png")
        elif command=='ON':
            GPIO.output(22, True)
            print("LED ON")
            sleep(1)
            GPIO.output(22, False)
            GPIO.cleanup
        elif command=='OFF':
            GPIO.output(22, False)
            print("LED OFF")
            sleep(1)  
    bot=telepot.Bot('969540077:AAF9qo60W6scHUgIopGZs6m6wOcLP-UQfqs')
    bot.message_loop(handle)
    print('I am listening..')
    while 1:
            time.sleep(5)
finally:
         GPIO.cleanup()
