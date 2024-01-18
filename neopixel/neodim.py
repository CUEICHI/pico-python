from machine import Pin
from time import sleep
import neopixel, random

NUM = 64
neopin = Pin(7,Pin.OUT)

neo = neopixel.NeoPixel(neopin,NUM)



while True:
    color = (random.randrange(20),random.randrange(20),random.randrange(20))
    for i in range(NUM)
        neo[i]=color 
    neo.write()
    sleep(1)