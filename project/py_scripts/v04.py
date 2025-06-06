'''
Abstraction as simple interface hides (facade design pattern)
The complexity of the implementation of the class 'Led_Light' in the module 'led_light.py'
Extend the implementation to provide on for duration and flash for duration methods
'''

from led_light import Led_Light
from time import sleep

red_light = Led_Light(25, True, True)

while True:
    red_light.toggle()
    sleep(0.5)
