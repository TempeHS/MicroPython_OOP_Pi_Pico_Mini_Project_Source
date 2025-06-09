# Lecture 3

## Lecture 2 Concepts
- Encapsulation
- Setters & Getters
- Abstraction
- Extend LED functionality

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
> Make sur eyou now edit the class in the `project\lib\led_light.py` not your main python implementation.

```python
    def flash(self, duration=5):
        # Method to flash the LED on and off every 0.5 seconds for a given duration
        if self.__flashing:
            if self.__debug:
                print(f"LED connected to Pin {self.__pin} is flashing for {duration} seconds")
            end_time = time() + duration
            while time() < end_time:
                self.toggle()
                sleep(0.5)  # Delay for 0.5 seconds

    def on_for(self, duration):
        # Turns the LED on for a specified duration (in seconds) and then turns it off.
        self.on()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is ON for {duration} seconds")
        sleep(duration)
        self.off()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is OFF after {duration} seconds")
```
