from machine import Pin
from time import ticks_ms, ticks_diff


class PedestrianButton(Pin):
    """Debounced pedestrian request button."""

    def __init__(self, pin, debug):
        """Initialize a PedestrianButton.

        Args:
            pin (int): GPIO pin number.
            debug (bool): True to print debug messages.
        """
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = ticks_ms()  # Track the last time the button was pressed
        self.__pedestrian_waiting = False
        self.irq(
            trigger=Pin.IRQ_RISING, handler=self.callback
        )  # Set up interrupt on rising edge

    def button_state(self, value=None):
        """Get or set the waiting state.

        Args:
            value (bool, optional): New waiting state.

        Returns:
            bool: Current waiting state when called as getter.
        """
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
            return self.__pedestrian_waiting
        else:
            self.__pedestrian_waiting = bool(
                value
            )  # Convert to boolean to ensure proper type
            if self.__debug:
                print(
                    f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}"
                )

    def callback(self, pin):
        """Handle button interrupt with debounce.

        Args:
            pin (Pin): Pin that triggered the interrupt.
        """
        current_time = ticks_ms()  # Get the current time in milliseconds
        if ticks_diff(current_time, self.__last_pressed) > 200:  # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
