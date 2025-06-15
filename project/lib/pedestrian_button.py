from machine import Pin
from time import ticks_ms, ticks_diff


class Pedestrian_Button(Pin):
    """Pedestrian button class that extends machine.Pin to provide a debounced button interface.

    This class implements a button with interrupt-based detection and software debouncing.
    It maintains an internal state to track if a pedestrian is waiting after a button press.

    Args:
        pin (int): The GPIO pin number the button is connected to.
        debug (bool): Whether to print debug statements.
    """

    def __init__(self, pin, debug):
        """Initialize the Pedestrian_Button object.

        Sets up the pin as an input with pull-down resistor and configures
        an interrupt handler for rising edge detection.

        Args:
            pin (int): The GPIO pin number the button is connected to.
            debug (bool): Whether to print debug statements.
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
        """
        Get or set the current state of the pedestrian waiting flag.

        - If called with no arguments, returns the current state (getter).
        - If called with a boolean argument, sets the state (setter).

        Args:
            value (bool, optional): If provided, sets the pedestrian waiting state.

        Returns:
            bool: Current state if called without arguments.
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
        """Interrupt handler called when the button is pressed (rising edge).

        Implements software debouncing by ignoring presses that occur within
        200ms of the previous press. Sets the pedestrian_waiting flag when a
        valid button press is detected.

        Args:
            pin (Pin): The pin that triggered the interrupt.
        """
        current_time = ticks_ms()  # Get the current time in milliseconds
        if ticks_diff(current_time, self.__last_pressed) > 200:  # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
