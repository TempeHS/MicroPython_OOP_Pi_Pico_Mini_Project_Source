from machine import Pin
import time

class Pedestrian_Button(Pin):
    # child class inherits the parent 'Pin' class

    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0  # Track the last time the button was pressed
        self.button_state
        self.pedestrian_waiting = False
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback) # Set up interrupt on rising edge

    def callback(self, pin):
        current_time = time.ticks_ms()  # Get the current time in milliseconds
        if time.ticks_diff(current_time, self.__last_pressed) > 200:  # 200ms debounce delay
            self.__last_pressed = current_time
            self.pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")

    @property
    def button_state(self):
        self.__button_state = self.value()
        if self.__debug:
            print(f"Button connected to Pin {self.__pin} is {self.__button_state}")
        return self.__button_state
