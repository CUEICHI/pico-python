import machine, neopixel, random, time


LEDNUM = 64
neopin = machine.Pin(0,machine.Pin.OUT)
np = neopixel.NeoPixel(neopin,LEDNUM)

np.fill((0,0,0))
np.write()

for i in range(1000):
    i = random.randrange(LEDNUM)
    np[i] = (random.randrange(30),random.randrange(30),random.randrange(30))
    np.write()
    time.sleep_ms(50)
time.sleep(2)
np.fill((0,0,0))
np.write()


