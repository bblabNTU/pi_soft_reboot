#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pull up to high
GPIO.wait_for_edge(13, GPIO.FALLING) # when the GPIO is pulled down to GND
sleep(3) # wait to determine long press or short press
if GPIO.input(13) ==0: 
    # after 3 seconds if it is still pulled down to GND, shutdown
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
else:
    # else short press for reboot
    subprocess.call(['shutdown', '-r', 'now'], shell=False)
