'''
Implement a debounced button event manager that inherits Pin class
'''

from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from time import sleep



red_light = Led_Light(3, False)
ped_button = Pedestrian_Button(22, True)

while True:
    sleep(1)
    red_light.led_light_state = ped_button.button_state
