from machine import Pin,PWM
from time import sleep, sleep_ms,sleep_us

led = [Pin(0,Pin.OUT), Pin(1,Pin.OUT) ]
sol = Pin(9,Pin.OUT)

for i in range(20):
    led[1].value(0)
    sleep_ms(5)
    led[1].value(1)
    sleep_ms(100)

led[0].value(1)

