import machine, neopixel, random, time

neopin = machine.Pin(15,machine.Pin.OUT)
LEDNUM = 60
MAXLED = 20
np = neopixel.NeoPixel(neopin,LEDNUM)

np.fill((0,0,0))
np.write()
time.sleep(1)

for i in range(500):
    i = random.randrange(LEDNUM)
    np[i] = (random.randrange(MAXLED),random.randrange(MAXLED),random.randrange(MAXLED))
    np.write()
    time.sleep(0.01)
time.sleep(2)
np.fill((0,0,0))
np.write()


