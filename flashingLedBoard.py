from gpiozero import LEDBoard
from time import sleep
from signal import pause
import random

leds = LEDBoard(22,23,24,26,27, pwm=True)

try:
    while True:
        for x in range(10):
            a = random.randint(0,4)
            b = random.randint(0,4)
            c = random.randint(0,4)
            d = random.randint(0,4)
            e = random.randint(0,4)
            print(a, b, c, d, e)
            leds.on(a, b, c, d, e)
            sleep(random.uniform(0.1, 0.25))
            leds.off(a, b, c, e, d)
            sleep(random.uniform(0.05, 0.1))
        print("end of cycle")
        sleep(0.2)
        print("turn on each separately")
        for x in range(5):
            print(x)
            leds.toggle(x)
            sleep(0.2)
        print("turn off each separately")
        for y in range(4, 0, -1):
            print(y)
            leds.toggle(y)
            sleep(0.2)
        leds.off()    
        print("blink 3 times all leds")
        for x in range(3):
            sleep(random.uniform(0.1, 0.5))
            leds.on()
            sleep(random.uniform(0.1, 0.5))
            leds.off()
        sleep(random.uniform(0.1, 0.5))
        
except KeyboardInterrupt:
    # Clean up GPIO on script interruption
    leds.off()
    leds.close()
    print("end of code")