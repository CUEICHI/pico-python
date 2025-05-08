from machine import Pin
from time import sleep,sleep_ms,sleep_us

sol1 = Pin(12,Pin.OUT)
led = Pin("LED",Pin.OUT)

print("START")
for i in range(20):
    sol1.value(0)
    led.value(0)
    print("OFF")
    sleep(1)
    sol1.value(1)
    led.value(1)
    print("ON")
    sleep(1)

sol1.value(0)
led.value(0)
print("FINISH")
