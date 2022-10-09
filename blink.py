import time
import machine

led = machine.Pin(14,machine.Pin.OUT)


while True:
    led.value(0)
    print("HELLO")
    time.sleep(1)
    led.value(1)
    time.sleep(1)