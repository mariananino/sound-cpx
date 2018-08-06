from adafruit_circuitplayground.express import cpx
import time
import random
import microcontroller
WHITE = (50, 50, 50)
OFF   = (0,   0,  0)

# Not too bright!
cpx.pixels.brightness = 0.3
pixeln = 0
pink = (40, 0, 30)
turquiose = (0, 0, 255)
blueval = 200
yellow = 220
off = (0, 0, 0)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
    return (int(pos*3), 0, int(255 - pos*3))

# Tap twice to toggle
cpx.detect_taps = 2
while True:
    for p in range(10):
        color = wheel(25 * ((pixeln + p)%10))
        cpx.pixels[p] = [int(c * ( (10 - (pixeln+p)%10)) / 10.0) for c in color]

    # Each time 'round we tick off one pixel at a time
    if cpx.switch:      # depending on the switch we'll go clockwise
        pixeln += 1
        if pixeln > 9:
            pixeln = 0
    else:               # or counter clockwise
        pixeln -= 1
        if pixeln < 0:
            pixeln = 9

    if pixeln == 0:   # Every time we go around, print sensor data
        print("Temperature: %0.1f *C" % cpx.temperature)
        print("Light Level: %d" % cpx.light)
        x, y, z = cpx.acceleration
        print("Accelerometer: (%0.1f, %0.1f, %0.1f) m/s^2" % (x, y, z))
        print('-' * 40)


    if cpx.button_a:
        cpx.play_file("Wild Eep.wav")

    if cpx.button_b:
        cpx.play_file("Fanfare.wav")