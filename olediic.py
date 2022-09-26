#
# OLED I2C Display Module 


from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(0,sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(1)
display.show()

