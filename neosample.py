import machine, neopixel, random, time


LEDNUM = 12
neopin = machine.Pin(4,machine.Pin.OUT)
np = neopixel.NeoPixel(neopin,LEDNUM)

np.fill((0,0,0))
np.write()

print("start")
for i in range(100):
    i = random.randrange(LEDNUM)
    np[i] = (random.randrange(30),random.randrange(30),random.randrange(30))
    np.write()
    time.sleep_ms(10)
time.sleep(2)
np.fill((0,0,0))
np.write()
print("en d")

