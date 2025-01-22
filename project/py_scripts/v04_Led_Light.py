from machine import Pin


class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, state=0):
        super().__init__(pin)
        self.led_light_state = state

    def on(self):
        # method overiding polymorphism of the parent class
        self.__led_light_state = 1
        self.high()

    def off(self):
        # method overiding polymorphism of the parent class
        self.__led_light_state = 0
        self.low()

    def toggle(self):
        # method overiding polymorphism of the parent class
        if self.__led_light_state:
            self.off()
        else:
            self.on()

    @property
    def led_light_state(self):
        # method overloading polymorphism in this class
        return self.__led_light_state

    @led_light_state.setter
    def led_light_state(self, value):
        # method overloading polymorphism in this class
        if value == 0 or value == 1:
            self.__led_light_state = value
            if self.__led_light_state:
                self.on()
            else:
                self.off()
