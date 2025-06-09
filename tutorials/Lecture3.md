# Lecture 3

## Lecture 2 Concepts
- Encapsulation
- Setters & Getters
- Abstraction
- Extend LED functionality
- Complete led light class

## Encapsulation
Encapsulation restricts direct access to some of an object's components (attributes or methods), which means that the internal representation of an object is hidden from the outside. This is typically achieved by making certain attributes or methods private (i.e., not accessible from outside the class) and providing public methods (such as getters and setters) to access or modify those private members.

### Benefits of Encapsulation:

- Data Hiding: Internal object details are hidden, exposing only what is necessary.
- Improved Security: Prevents external code from directly modifying internal state in unexpected ways.
- Modularity: Each object manages its own state and behaviour, making code more modular and easier to maintain.
- Flexibility: Implementation can change without affecting code that uses the object, as long as the public interface remains the same.

```python
while True:
    print(red_light.led_light_state) # Allowed
    red_light.led_light_state = 1 # Allowed
    print(f"Not allowed: {red_light.__pin} ???") # Not allowed, should raise AttributeError
```
> [!Note]
> In Python, identifiers (variable or method names) that start with double underscores (e.g., `__my_var`) are not truly private in the sense of other languages like C# or C++. Instead, Python uses a mechanism called name mangling. When you define a variable with double underscores, Python changes its name internally to `_ClassName__my_var`. This means it is harder (but not impossible) to access it from outside the class.

## Setters & Getters

Setters and getters are special methods used in object-oriented programming to access (get) or modify (set) the values of private or protected attributes of a class. They help encapsulate the internal state of an object, providing controlled access.

### Getter

- A getter is a method that retrieves (gets) the value of a private attribute.
- It allows you to read the value without providing direct access to the underlying variable.

### Setter

- A setter is a method that sets (updates) the value of a private attribute.
- It allows you to validate or restrict changes before updating the attribute.

```python
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
```

### Why Use Setters & Getters
- Encapsulation: Protects the internal state of the object.
- Validation: Allows you to add checks before changing values.
- Abstraction: Hides implementation details from users of the class.

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

## Extend the functionality of the led_light class

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
        self._last_toggle_time = time()

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
        if self.__flashing and now - self._last_toggle_time >= 0.5:
            self.toggle()
            self._last_toggle_time = now
```