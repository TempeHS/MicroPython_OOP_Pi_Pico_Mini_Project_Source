"""
Lecture 2 - Polymorphism WET v DRY
"""

from machine import Pin
from time import sleep


class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overriding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the parent class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

red_light = Led_Light(3, False, True)

while True:
    red_light.toggle()
    sleep(1)
