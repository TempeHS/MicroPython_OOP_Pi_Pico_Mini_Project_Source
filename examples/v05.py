"""
Overriding Polymorphism Example
"""

from machine import Pin
from time import sleep


class Led_Light(Pin):
    # Sub Class inherits the 'Pin' Class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overriding polymorphism of the Super Class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the Super Class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")


red_light = Led_Light(3)

while True:
    red_light.on()
    sleep(1)
    red_light.off()
    sleep(1)
