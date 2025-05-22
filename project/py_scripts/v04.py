'''
Implement a on/off LED controller
Abstraction as simple interface hides (facade design pattern)
The complexity of the implementation of the class 'Led_Light' in the module 'led_light.py'
'''

from led_light import Led_Light
import time

red_light = Led_Light(3, True)

while True:
    red_light.toggle()
    time.sleep(0.5)
