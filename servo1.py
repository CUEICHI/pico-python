from machine import PWM, Pin
import time

servo1 = PWM(Pin(1,Pin.OUT))
servo1.freq(60)

servo2 = PWM(Pin(2,Pin.OUT))
servo2.freq(60)

max_duty = 65535
dig_0 = 0.0725    #0°
dig_90 = 0.18     #90°

while True:
    servo1.duty_u16(int(max_duty*dig_0))
    servo2.duty_u16(int(max_duty*dig_90))
    time.sleep(1)
    servo1.duty_u16(int(max_duty*dig_90))
    servo2.duty_u16(int(max_duty*dig_0))
    time.sleep(1)