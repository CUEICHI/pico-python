import time
import machine

led1 = machine.Pin(10,machine.Pin.OUT)
led2 = machine.Pin(11,machine.Pin.OUT)
led3 = machine.Pin(12,machine.Pin.OUT)
led4 = machine.Pin(13,machine.Pin.OUT)

while True:
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    print("HELLO")
    time.sleep(1)
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    time.sleep(1)

