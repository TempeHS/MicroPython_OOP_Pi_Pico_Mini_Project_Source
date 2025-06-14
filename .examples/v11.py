"""
Extend Led_light
"""

from project.py_scripts.LL_unit_Test import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    red_light.flash()
    sleep(0.1)
