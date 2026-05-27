from machine import Pin
from time import sleep, time


class LedLight(Pin):
    """LED wrapper with on/off/toggle/flash helpers."""

    def __init__(self, pin, flashing=False, debug=False):
        """Initialize a LedLight.

        Args:
            pin (int): GPIO pin number.
            flashing (bool): Enable non-blocking flashing behavior.
            debug (bool): True to print debug messages.
        """
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()

    def on(self):
        """Turn the LED on."""
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        """Turn the LED off."""
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        """Toggle the LED state."""
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        """Return LED state.

        Returns:
            int: 0 for off, 1 for on.
        """
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        """Set LED state.

        Args:
            value (int): 0 to turn on, 1 to turn off.
        """
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        """Toggle LED every 0.5s when flashing is enabled."""
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
