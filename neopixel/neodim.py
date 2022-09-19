from machine import Pin
from time import sleep
import neopixel, random

NUM = 24
neopin = Pin(0,Pin.OUT)

neo = neopixel.NeoPixel(neopin,NUM)


color = (random.randrange(100),random.randrange(100),random.randrange(100))

while True:
    neo.fill(color)
    neo.write()
    color = (int(color[0]/2),int(color[1]/2), int(color[2]/2))
    if color[0]<1:
        break
    sleep(0.1)