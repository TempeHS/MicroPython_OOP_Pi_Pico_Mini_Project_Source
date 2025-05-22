from machine import Pin
import time

class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overiding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        # method overiding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        # method overiding polymorphism of the parent class
        if self.value():
            self.on()
        else:
            self.off()

    @property
    def led_light_state(self):
        # method overloading polymorphism in this class
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        # method overloading polymorphism in this class
        if value == 0:
            self.off()
        elif value == 1:
            self.on()

    def flash(self, duration=5):
        # Method to flash the LED on and off every 0.5 seconds for a given duration
        if self.__flashing:
            end_time = time.time() + duration
            while time.time() < end_time:
                self.toggle()
                time.sleep(0.5)  # Delay for 0.5 seconds

    def on_for(self, duration):
        # Turns the LED on for a specified duration (in seconds) and then turns it off.
        self.on()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is ON for {duration} seconds")
        time.sleep(duration)
        self.off()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is OFF after {duration} seconds")