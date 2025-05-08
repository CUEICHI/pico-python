import machine
import neopixel
import time
import random

# NeoPixel のデータピンを GP16 に設定
pin = machine.Pin(16, machine.Pin.OUT)

# 接続している NeoPixel LED の個数
NUM_PIXELS = 25

# NeoPixel オブジェクトの生成
np = neopixel.NeoPixel(pin, NUM_PIXELS)

while True:
    # すべてのLEDをランダムな色に設定
    for i in range(NUM_PIXELS):
        r = random.getrandbits(8)  # 0〜255 のランダム値
        g = random.getrandbits(8)
        b = random.getrandbits(8)
        np[i] = (r>>5, g>>5, b>>5)
    
    # 設定した色をLEDに反映
    np.write()
    
    # ウェイト (点滅速度の調整)
    time.sleep(0.1)