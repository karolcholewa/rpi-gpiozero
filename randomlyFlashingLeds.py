from gpiozero import LED
from time import sleep
import random

#program1:
while True:
    
    led = LED(random.choice([17,18, 21, 25]))
    print(led)
    led.on()
    sleep(random.uniform(0.1, 0.5))
    led.off()
    sleep(random.uniform(0.1, 0.2))
    led = ''
    
# Clean up GPIO on Ctrl+C
    leds.close()
    
     