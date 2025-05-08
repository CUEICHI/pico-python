from machine import Pin
from time import sleep_ms

# GPIOピンの設定 (例: ピン番号 2 を入力モードに設定)
pinA = Pin(2, Pin.IN)
pinB = Pin(3, Pin.IN)
pinC = Pin(4, Pin.IN)

while True:
    # ピンの状態を読み取る (0 または 1)
    a = pinA.value()
    b = pinB.value()
    c = pinC.value()
    print(a,b,c);
    # 1秒待機
    sleep_ms(50)