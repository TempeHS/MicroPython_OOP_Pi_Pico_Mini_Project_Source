"""
Abstraction Example
"""

from led_light import LedLight
from time import sleep

red_light = LedLight(3, True, True)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
