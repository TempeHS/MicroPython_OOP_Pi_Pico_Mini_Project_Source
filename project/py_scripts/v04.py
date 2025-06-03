'''
Implement a on/off LED controller
Abstraction as simple interface hides (facade design pattern)
The complexity of the implementation of the class 'Led_Light' in the module 'led_light.py'
'''

from led_light import Led_Light
from time import sleep

red_light = Led_Light(25, True, True)

while True:
    red_light.toggle()
    sleep(0.5)
