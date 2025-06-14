from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    """LED Light Class that extends machine.Pin to provide higher-level LED control.

    This class provides methods to control an LED including on, off, toggle, and non-blocking flashing.
    It extends the machine.Pin class functionality, overriding and adding methods specific to LED control.

    Args:
        pin (int): The GPIO pin number the LED is connected to.
        flashing (bool, optional): Whether to enable flashing capability. Defaults to False.
        debug (bool, optional): Whether to print debug statements. Defaults to False.
    """

    def __init__(self, pin, flashing=False, debug=False):
        """Initialize the Led_Light object.

        Args:
            pin (int): The GPIO pin number the LED is connected to.
            flashing (bool, optional): Whether to enable flashing capability. Defaults to False.
            debug (bool, optional): Whether to print debug statements. Defaults to False.
        """
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()

    def on(self):
        """Turn the LED on.

        Overrides the Pin.on() method to provide additional debug output.
        """
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        """Turn the LED off.

        Overrides the Pin.off() method to provide additional debug output.
        """
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        """Toggle the LED between on and off states.

        If the LED is off, turns it on. If the LED is on, turns it off.
        """
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        """Get the current state of the LED.

        Returns:
            int: 0 if the LED is off, 1 if the LED is on.
        """
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        """Set the state of the LED.

        Args:
            value (int): 0 turns the LED on, 1 turns the LED off.
        """
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        """Non-blocking flash: toggles LED every 0.5 seconds.

        This method should be called repeatedly in the main loop.
        The LED will toggle only if flashing is enabled and 0.5 seconds
        have elapsed since the last toggle.
        """
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
