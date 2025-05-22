'''
Implement a debounced button event manager
'''

from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
import time



red_light = v04_Led_Light.Led_Light(3, False)
ped_button = Pedestrian_Button(22, True)

while True:
    time.sleep(1)
    red_light.led_light_state = ped_button.button_state
