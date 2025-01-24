from machine import Pin


class Pedestrian_Button(Pin):
    # child class inherits the parent 'Pin' class

    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.button_state
        self.pedestrian_waiting = False
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    def callback(self, pin):
        self.pedestrian_waiting = True

    @property
    def button_state(self):
        Pedestrian_Button = 1
        self.__button_state = self.value()
        print(self.__button_state)
        if True:
            print(f"Button connected to Pin {self.__pin} is {self.__button_state}")
        return self.__button_state
