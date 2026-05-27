from machine import Pin
from time import sleep

class LedLight(Pin):
def __init__(self, pin):
super().__init__(pin, Pin.OUT)

red_light = LedLight(3)

while True:
    red_light.toggle()
    sleep(1)
