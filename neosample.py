import machine, neopixel, random, time

neopin = machine.Pin(0,machine.Pin.OUT)
np = neopixel.NeoPixel(neopin,60)

np.fill((0,0,0))
np.write()

for i in range(1000):
    i = random.randrange(60)
    np[i] = (random.randrange(30),random.randrange(30),random.randrange(30))
    np.write()
time.sleep(2)
np.fill((0,0,0))
np.write()


