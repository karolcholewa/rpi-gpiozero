from gpiozero import LED
from time import sleep
import random

while True:
    led = LED(random.choice([17, 18, 25]))
    print(led)
#     print(random.getstate())
    led.on()
    sleep(random.uniform(0.1, 0.5))
    led.off()
    sleep(random.uniform(0.1, 0.1))
    led = ''
