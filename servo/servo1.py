from machine import PWM, Pin
import time

servo1 = PWM(Pin(15,Pin.OUT))
servo1.freq(60)

servo2 = PWM(Pin(14,Pin.OUT))
servo2.freq(60)

max_duty = 65535
dig_0 = 0.0725    #0°
dig_90 = 0.36     #90°

while True:
    servo1.duty_u16(int(max_duty*dig_0))
    servo2.duty_u16(int(max_duty*dig_90))
    print("dig1")
    print(int(max_duty*dig_0))
    print(int(max_duty*dig_90))
    time.sleep(2)
    servo1.duty_u16(int(max_duty*dig_90))
    servo2.duty_u16(int(max_duty*dig_0))
    print("dig2")
    time.sleep(2)