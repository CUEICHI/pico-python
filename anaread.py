from machine import ADC, Pin
import time

adcpin = [26, 27, 28, 29]  # ADCピンのリスト（PicoのADC0〜ADC3に対応）

adc = []
# ADCピンの設定（GPIO26はADC0に対応）
for i,p in enumerate(adcpin):
    adc.append( ADC(Pin(p)) )

while True:
    for i in range(len(adc)):
        value = adc[i].read_u16()  # 16ビットの値（0〜65535）を取得
        voltage = value * 3.3 / 65535  # 電圧に変換（PicoのADCは3.3V基準）
        print(i, "Raw value:", value, " -> Voltage:", round(voltage, 2), "V")
        #print(int(value/256))
    time.sleep(0.5)