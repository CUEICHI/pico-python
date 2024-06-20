from machine import Pin, SPI
import max7219 as max7219
from time import sleep

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi, cs,12)

display.brightness(3)

while True:

    display.fill(0)
    display.text('PICO ON AIR',0,0,1)
    display.show()
    sleep(1)

    display.fill(0)
    display.text('HELLO WORLD',0,0,1)
    display.show()
    sleep(1)

    display.fill(0)
    display.text('ABCDEFGHIJK',0,0,1)
    display.show()
    sleep(1)