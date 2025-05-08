import machine
import neopixel
import time
import math

# NeoPixel のピン設定 (GP16 を使用)
pin = machine.Pin(16, machine.Pin.OUT)

# NeoPixel LED の個数
NUM_PIXELS = 25

# NeoPixel オブジェクトの生成
np = neopixel.NeoPixel(pin, NUM_PIXELS)

def hsv_to_rgb(h, s, v):
    """
    HSV(色相H, 彩度S, 明度V) を RGB に変換する関数
    H: 0.0～360.0
    S: 0.0～1.0
    V: 0.0～1.0
    戻り値: (r, g, b) それぞれ 0～255
    """
    # Hを360で割った小数などの処理で誤差が出やすいためfloatを扱う
    h = float(h)
    s = float(s)
    v = float(v)

    c = v * s
    x = c * (1 - abs((h / 60.0) % 2 - 1))
    m = v - c

    # 一旦 0～1 の範囲で RGB を算出し、あとで 0～255 にスケーリング
    if 0 <= h < 60:
        r, g, b = (c, x, 0)
    elif 60 <= h < 120:
        r, g, b = (x, c, 0)
    elif 120 <= h < 180:
        r, g, b = (0, c, x)
    elif 180 <= h < 240:
        r, g, b = (0, x, c)
    elif 240 <= h < 300:
        r, g, b = (x, 0, c)
    else:  # 300 <= h < 360
        r, g, b = (c, 0, x)

    # m を足して [0,1]範囲にし、さらに 0～255 に拡大
    r = int((r + m) * 64)
    g = int((g + m) * 64)
    b = int((b + m) * 64)

    return (r, g, b)

def color_wheel():
    """
    NeoPixel を色相環に沿って変化させる無限ループ。
    """
    # オフセット（全体の色合いを回転させるための値）
    hue_offset = 0
    
    while True:
        for i in range(NUM_PIXELS):
            # 各LEDごとに、色相を少しずつずらして割り振る
            hue = (i * (360 / NUM_PIXELS) + hue_offset) % 360
            r, g, b = hsv_to_rgb(hue, 1.0, 1.0)  # 彩度=1.0, 明度=1.0 でビビッドな色
            np[i] = (r, g, b)
        
        # 実際に LED を更新
        np.write()
        
        # オフセットを少しずつ増やして色を回転させる
        hue_offset = (hue_offset + 2) % 360
        
        # 更新のスピードを調整 (0.05～0.2 あたりをお好みで)
        time.sleep(0.02)

# メイン実行
color_wheel()