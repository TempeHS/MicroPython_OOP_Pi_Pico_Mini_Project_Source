"""
Lecture 3 - Extend Led_light class
"""

from led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    red_light.flash()
    sleep(0.1)
