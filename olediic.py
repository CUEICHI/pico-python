from machine import Pin, I2C
import ssd1306

#
# I2Cの設定です。
# 識別するID(0), SDA(16), SCL(17)を設定します
#
i2c = I2C(0, sda=Pin(4), scl=Pin(5) )

#
# デバイスのアドレスを取得します
# 0x30(60)でない場合はライブラリの修正が必要です。
#
addr = i2c.scan()
print( "address is :" + str(addr) )

#
# ディスプレイを設定します
# 使用するディスプレイの縦・横のサイズ、I2Cの変数を渡します
#
display = ssd1306.SSD1306_I2C(128, 64, i2c)

#　テキスト表示を設定します
display.text('Display Test', 0, 0, 1)

# 横線を設定します
display.hline(10, 10, 20, 1)

# 縦線を設定します
display.vline(10, 10, 20, 1)

# 斜め線を設定します
display.line(10, 10, 30, 30, 1)

# 四角系を設定します(塗りつぶしなし)
display.rect(10, 40, 10, 10, 1)

# 四角形を設定します(塗りつぶしあり) 
display.fill_rect(30, 40, 10, 10, 1)

# 明暗の反転を設定します
#display.invert(1) 

# 設定した内容をディスプレイに表示します
display.show()
