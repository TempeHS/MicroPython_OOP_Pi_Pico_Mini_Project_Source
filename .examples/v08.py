"""
Encapsulation Example
"""

from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    # Sub Class inherits the Super 'Pin' Class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overriding polymorphism of the Super Class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        # method overriding polymorphism of the Super Class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        # method overriding polymorphism of the Super Class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        # method overloading polymorphism in this Class
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        # method overloading polymorphism in this Class
        if value == 1:
            self.off()
        elif value == 0:
            self.on()


red_light = Led_Light(3, False, False)

while True:
    print(red_light.led_light_state)  # Allowed
    red_light.led_light_state = 1  # Allowed
    print(
        f"Not allowed: {red_light.__pin} ???"
    )  # Not allowed, should raise AttributeError
