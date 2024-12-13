from time import sleep_ms
from machine import Pin

led = Pin('LED',Pin.OUT)


while True:
    led.value(1)
    #print("HELLO")
    sleep_ms(10)

    led.value(0)
    #print("World!")
    sleep_ms(500)
