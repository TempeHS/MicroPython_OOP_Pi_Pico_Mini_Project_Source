from machine import Pin


class Pedestrian_Button(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, pull_up=True):
        super().__init__(pin)
        self.button_state

    @property
    def button_state(self):
        # method overloading polymorphism in this class
        print("Button is pressed" if self.value() else "Button is not pressed")
        return self.value()
