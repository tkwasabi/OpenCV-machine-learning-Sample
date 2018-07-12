#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

GPIO.setmode(GPIO.BOARD)


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

sw1 = 0
sw2 = 0
try:
    while True:
        time.sleep(3)

        if sw1 == 1:
            pwm.set_pwm(1, 0, 600)
            sw1 = 0
        else:
            pwm.set_pwm(1, 0, 375)
            sw1 = 1

        if sw2 == 1:
            pwm.set_pwm(0, 0, 600)
            sw2 = 0
        else:
            pwm.set_pwm(0, 0, 375)
            sw2 = 1


except KeyboardInterrupt:
    pass