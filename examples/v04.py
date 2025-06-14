"""
Inhertance Example
"""

from machine import Pin
from time import sleep


class Led_Light(Pin):
    # Sub Class inherits the 'Pin' Class
    def __init__(self, pin):
        super().__init__(pin, Pin.OUT)


red_light = Led_Light(3)

while True:
    red_light.on()
    sleep(0.5)
    red_light.off()
    sleep(0.5)
    red_light.high()
    sleep(2)
    red_light.low()
    sleep(2)
    red_light.toggle()
    sleep(4)
    red_light.toggle()
    sleep(4)
