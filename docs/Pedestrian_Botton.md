# Pedestrian_Button Class

The `Pedestrian_Button` class extends the `machine.Pin` class to provide a debounced button interface specifically designed for pedestrian crossing systems. It uses interrupt-based detection and software debouncing to reliably capture button presses.

## Constructor

```python
Pedestrian_Button(pin, debug=False)
```
- `pin` (`int`): The GPIO pin number the button is connected to.
- `debug` (`bool`, optional): Enable debug print statements. Defaults to False.

## Example Usage

```python
from pedestrian_button import Pedestrian_Button
from time import sleep

# Create a Pedestrian_Button on GPIO pin 22 with debug enabled
button = Pedestrian_Button(22, debug=True)

# Main loop
while True:
    # Check if button has been pressed
    if button.button_state():
        print("Pedestrian waiting - processing crossing request")
        # Process crossing request
        
        # Reset the button state after handling
        button.button_state(False)
    
    sleep(0.1)  # Small delay to prevent busy waiting
```

## Methods

- **button_state(value=None)**  
  Multi-purpose method that acts as both getter and setter for the pedestrian waiting state.
  - When called with no arguments: Returns the current waiting state
  - When called with a boolean argument: Sets the waiting state
  
- **callback(pin)**  
  Internal interrupt handler that's called when the button is pressed.
  Implements software debouncing (200ms) and sets the pedestrian waiting flag.

## Notes

- The button should be connected between the specified GPIO pin and 3.3V.
- The class uses the internal pull-down resistor configuration.
- Debouncing prevents multiple rapid detections from a single button press.
- The interrupt triggers on the rising edge (when button is pressed).

## Class Unit Test

```python
from pedestrian_button import Pedestrian_Button
from time import sleep

# Create button with debug enabled
button = Pedestrian_Button(22, debug=True)

print("Testing initial state (should be False)")
if button.button_state() == False:
    print("Initial state test passed")
else:
    print("Initial state test failed")

print("Testing manual state setting")
button.button_state(True)
if button.button_state() == True:
    print("Manual state setting test passed")
else:
    print("Manual state setting test failed")

print("Press the button within 5 seconds to test interrupt...")
sleep(5)

if button.button_state():
    print("Button press detected - interrupt test passed")
else:
    print("No button press detected")

print("Testing state reset")
button.button_state(False)
if button.button_state() == False:
    print("State reset test passed")
else:
    print("State reset test failed")
```

## Class Implementation

```python
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
```