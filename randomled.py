from machine import PWM, Pin
from time import sleep
import random
lpin = Pin('LED',Pin.OUT)
led = PWM(lpin)
led.freq(100)

while True:
    cnt = int(65535*random.random()/100 )
    led.duty_u16(cnt)
    print(cnt)
    sleep(1)
 