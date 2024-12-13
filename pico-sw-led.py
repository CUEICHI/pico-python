from machine import Pin
from time import sleep

led = Pin(0,Pin.OUT)
sw = Pin(17,Pin.IN,Pin.PULL_UP)
tgl = 1

while True:
    if sw.value() ==0:
        tgl = tgl * -1
        while sw.value()==0:
            sleep(0.01)

    if tgl ==1:
        led.value(0)
    else:
        led.value(1)





