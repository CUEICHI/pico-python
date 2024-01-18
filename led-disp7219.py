from machine import Pin, SPI
import max7219
from time import sleep
import math

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

num_of_matrix = 20
display = max7219.Matrix8x8(spi,cs,num_of_matrix)

display.brightness(15)

#scrolling_message = "Tokyo University of Technology, School of Media Science    "
scrolling_message = "BABEL "#
length = len(scrolling_message)
column = (length * 8)
message_repeat = math.ceil(num_of_matrix / length) 
    
while True:
    for x in range(num_of_matrix * 8, - (column - (num_of_matrix * 8)), -1):
        display.fill(0)

        display.text(scrolling_message * (message_repeat + 1) ,x - column * (message_repeat),0,1)
        display.show()
        sleep(0.01 )