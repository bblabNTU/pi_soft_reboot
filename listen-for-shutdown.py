#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(13, GPIO.FALLING)
sleep(3)
if GPIO.input(13) ==0:
    #still pressed, shutdown pi
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
else:
    subprocess.call(['shutdown', '-r', 'now'], shell=False)
