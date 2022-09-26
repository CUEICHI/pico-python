##
##
##

from machine import Pin, PWM
from time import sleep
import random

led = [Pin(8,Pin.OUT),Pin(9,Pin.OUT),Pin(10,Pin.OUT),Pin(11,Pin.OUT)]
for i in range(4):
    led[i].value(1)

sleep(3)

while True:
    for r in range(4):
        led[r].value(1)
        sleep(0.1)
        led[r].value(0)
        sleep(0.1)

