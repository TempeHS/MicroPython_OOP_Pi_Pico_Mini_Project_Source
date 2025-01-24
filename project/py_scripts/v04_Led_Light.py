from machine import Pin


class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin

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
