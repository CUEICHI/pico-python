from machine import Pin
import utime
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)
IN5 = Pin(6, Pin.OUT)
IN6 = Pin(7, Pin.OUT)
IN7 = Pin(8, Pin.OUT)
IN8 = Pin(9, Pin.OUT)

pina = [IN1,IN2,IN3,IN4]
pinb = [IN5,IN6,IN7,IN8]
wait_us = 2000

setup = [0,0,0,0]
step1 =[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
step1_reverse =[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
step2 = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
step3 = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]
for i in range(4):
    pina[i].value(setup[i])
    pinb[i].value(setup[i])
    utime.sleep_us(wait_us)
while True:
    for step in reversed(step3):
        for i in range(4):
            pina[i].value(step[i])
            pinb[i].value(step[3-i])
            utime.sleep_us(wait_us)