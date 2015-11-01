#!/usr/bin/env python

#wget "http://soundbible.com/grab.php?id=1540&type=wav" -O error.wav
#wget "http://soundbible.com/grab.php?id=1003&type=wav" -O success.wav

#curl -X POST -H "Content-type: application/json" -d '{"button": 34}' https://buttons-clicker.appspot.com/api/clicks

import pygame


import RPi.GPIO as GPIO
import time
import urllib2
import json

pygame.init()
error_sound = pygame.mixer.Sound("error.wav")
success_sound = pygame.mixer.Sound("success.wav")

GPIO.setmode(GPIO.BCM)

SWITCH1 = 23
SWITCH2 = 24
SWITCH3 = 25
  
GPIO.setup(SWITCH1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


handler = urllib2.HTTPSHandler(debuglevel=0)
opener = urllib2.build_opener(handler)
def request(button_no):
	data = {"button": button_no}
	try:
          opener.open(urllib2.Request("https://buttons-clicker.appspot.com/api/clicks", json.dumps(data), {"Content-Type": "application/json"}))
		success_sound.play()
    except urllib2.HTTPError, e:
    	error_sound.play()
    	print e

def call(channel, func):
	if not GPIO.input(channel):
		return
	time.sleep(0.3)
	while GPIO.input(channel):
		time.sleep(0.1)
	func()
	time.sleep(0.3)

while True:
  call(SWITCH1, lambda: request(1))
  call(SWITCH2, lambda: request(2))
  call(SWITCH3, lambda: request(3))
