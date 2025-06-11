# Lecture 3

## Lecture 3 Concepts
- Abstraction
- Implement a non blocking flash method
- Complete and Unit Test led light class

## Abstraction

Abstraction in Object-Oriented Programming (OOP) is a principle that focuses on exposing only the essential features of an object while hiding the unnecessary details. The primary goal is to offer a simplified, high-level interface for interacting with complex systems, thereby making your code easier to use and understand.

### Benefits of Abstraction

- What vs. How: Abstraction tells you what an object does, not how it does it.
- Simplification: It reduces complexity by hiding implementation details.
- Interface: Abstraction is often achieved by hiding the complex implementation and providing only the interface methods or attributes.

1. Create a bank Python file in `project\lib` called `led_light.py`
2. Copy the Class only to `project\lib\led_light.py`
3. Update your Python implementation so that you can import the abstracted class and directly call its class attributes and methods.

```Python
from led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
```

## Implement a non blocking flash method

> [!Important]
> Make sure you edit the class in the `project\lib\led_light.py`, not your main.py implementation.

```python
from time import sleep, time

    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self._last_toggle_time = time()

    def flash(self):
        # Non-blocking flash: toggles LED every 0.5s for the given duration
        now = time()
        if self.__flashing and now - self._last_toggle_time >= 0.5:
            self.toggle()
            self._last_toggle_time = now

```

## Complete led light class

The `Led_Light` class extends the `machine.Pin` class to provide advanced control of an LED, including toggling, non-blocking flashing, and optional debug output.

### Constructor

```python
Led_Light(pin, flashing=False, debug=False)
```
- `pin`: The GPIO pin number the LED is connected to.
- `flashing`: Set to `True` to enable the flash method.
- `debug`: Set to `True` to enable debug print statements.

### Example Usage

```python
from led_light import Led_Light
from time import sleep

# Create a Led_Light on GPIO pin 3, with flashing and debug enabled
led = Led_Light(3, flashing=True, debug=True)

# Turn the LED on
led.on()

# Turn the LED off
led.off()

# Toggle the LED state
led.toggle()

# Set the LED state using the property (0 = ON, 1 = OFF)
led.led_light_state = 0  # Turns LED ON
led.led_light_state = 1  # Turns LED OFF

# Non-blocking flash: call repeatedly in your main loop
while True:
    led.flash()  # Will toggle every 0.5s if flashing is enabled
    sleep(0.1)
```

### Methods and Properties

- **on()**  
  Turns the LED on and prints debug info if enabled.

- **off()**  
  Turns the LED off and prints debug info if enabled.

- **toggle()**  
  Switches the LED between on and off states.

- **led_light_state** (property)  
  Gets or sets the LED state (0 = ON, 1 = OFF).

- **flash()**  
  Non-blocking: toggles the LED every 0.5 seconds if `flashing=True`. Call this method repeatedly in your main loop.

---

**Note:**  
- The LED should be wired with an appropriate resistor to the specified GPIO pin.
- The class uses the internal features of the `machine.Pin` class for output control.

### Class Unit Test

```python
from time import sleep
from led_light import Led_Light

# Replace 3 with a valid GPIO pin number for your board
led = Led_Light(3, flashing=True, debug=True)

print("Testing on()")
led.on()
sleep(0.1)
if led.value() == 1:
    print(".on() method passed")
else:
    print(".on() method failed")

print("Testing off()")
led.off()
sleep(0.1)
if led.value() == 0:
    print(".off() method passed")
else:
    print(".off() method failed")


print("Testing toggle()")
led.toggle()
sleep(0.1)
if led.value() == 1:
    print(".toggle() .on() method passed")
else:
    print(".toggle() .on() method failed")

led.toggle()
sleep(0.1)
if led.value() == 0:
    print(".toggle() .off() method passed")
else:
    print(".toggle() .off() method failed")


print("Testing led_light_state property (getter)")
state = led.led_light_state
sleep(0.1)
if state == led.value():
    print(".led_light_state passed")
else:
    print(".led_light_state getter failed")

print("Testing led_light_state property (setter) to 1 (should turn on)")
set1 = led.led_light_state = 1
set0 = led.led_light_state = 0
if set1 == 1 and set0 == 0 :
    print(".led_light_state setter passed")
else:
    print(".led_light_state setter failed")

```


### Class Implementation

```python
from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()

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
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        # method overloading polymorphism in this class
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        # method overloading polymorphism in this class
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        # Non-blocking flash: toggles LED every 0.5s for the given duration
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
```
