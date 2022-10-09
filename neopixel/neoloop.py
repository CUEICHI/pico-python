from machine import Pin
from time import sleep
import neopixel

NUM = 24
neopin = Pin(7,Pin.OUT)

neo = neopixel.NeoPixel(neopin,NUM)
x=0
while True:
    x = x +1 
    i = x %24 
    print(i)
    if i==0:
        neo[23]=(20,0,20)
        neo[22]=(5,0,5)
        neo[21]=(0,0,0)
    if i==1:
        neo[0]=(20,0,20)
        neo[23]=(5,0,5)
        neo[22]=(0,0,0)
    if i==2:
        neo[1]=(20,0,20)
        neo[0]=(5,0,5)
        neo[23]=(0,0,0)
    else:
        neo[i-1]=(20,0,20)
        neo[i-2]=(5,0,5)
        neo[i-3]=(0,0,0)
    neo[i] = (50,0,50)
    neo.write()
    sleep(.03)
