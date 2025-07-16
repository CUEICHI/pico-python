from machine import Pin
import time

# --- ピン割り当て（例: GP14=A 相、GP15=B 相）---
pinA = Pin(2, Pin.IN, Pin.PULL_UP)
pinB = Pin(3, Pin.IN, Pin.PULL_UP)
sw   = Pin(4, Pin.IN, Pin.PULL_UP)

# 前回の A 相の状態を記憶
last_state = pinA.value()

def rotary_irq(pin):
    global last_state
    current_state = pinA.value()
    # A 相の立ち上がりを検出
    if last_state == 0 and current_state == 1:
        # B 相の状態で回転方向を判定
        if pinB.value() == 0:
            print('H')  # B=0 → 右回転
        else:
            print('L')  # B=1 → 左回転
    last_state = current_state

def sw_input(pin):
    time.sleep_ms(20)
    if sw.value() == 0:
        print("C")

# 割り込み設定：A 相の立ち上がりのみでも可
pinA.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=rotary_irq)
sw.irq(trigger=Pin.IRQ_FALLING, handler=sw_input)

# メインループは何もしない（割り込み動作）
while True:
    time.sleep(1)

