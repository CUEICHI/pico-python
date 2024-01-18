
from machine import Pin
from time import sleep

f1 = Pin(0,Pin.OUT)
f2 = Pin(1,Pin.OUT)
f3 = Pin(4,Pin.OUT)
f4 = Pin(5,Pin.OUT)
f5 = Pin(6,Pin.OUT)
f6 = Pin(7,Pin.OUT)
f7 = Pin(8,Pin.OUT)
f8 = Pin(9,Pin.OUT)
l1 = Pin("LED",Pin.OUT)


for i in range(10):
    f1.value(1)
    f2.value(1)
    f3.value(1)
    f4.value(1)
    f5.value(1)
    f6.value(1)
    f7.value(1)
    f8.value(1)
    l1.value(1)
    print("# ", i )
    sleep(1)

    f1.value(0)
    f2.value(0)
    f3.value(0)
    f4.value(0)
    f5.value(0)
    f6.value(0)
    f7.value(0)
    f8.value(0)
    l1.value(0)
    sleep(1)
    
