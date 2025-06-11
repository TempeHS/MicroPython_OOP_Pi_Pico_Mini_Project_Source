# Lecture 2

## Lecture 2 Concepts
- Overriding Polymorphism
- DRY
- Encapsulation
- Setters & Getters
- Overloading Polymorphism

## Overriding Polymorphism

**Polymorphism means “many forms.”**

Polymorphism Overriding occurs when a child class (subclass) provides a new implementation for a method it inherits from its parent class (superclass).

The method in the child class has the same name and parameters as the one in the parent class. When the method is called on an object of the child class, Python (or any object-oriented language) uses the child’s version, even if the object is referenced using the parent type.

```python
from machine import Pin
from time import sleep

class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overriding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the parent class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
           self.off()


red_light = Led_Light(3, False, False)

while True:
    red_light.on()
    sleep(1)
    red_light.off()
    sleep(1)
```

## DRY

The DRY pattern stands for "**Don't Repeat Yourself**"; it is a fundamental principle of programming aimed at reducing repetition of code and logic. This is to avoid duplicating code, logic, or data.

### Why Use DRY?
- Maintainability: When logic is defined in only one place, updates or bug fixes are only needed once.
- Readability: The code is easier to read and understand because there is less repetition.
- Consistency: Reduces the risk of inconsistencies and errors that can occur when updating duplicated code in multiple places.

```python
##### WET #####
    def on(self):
        # method overriding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the parent class
        if self.value() == 0:
            self.high()
            if self.__debug:
                print(f"LED connected to Pin {self.__pin} is high")
        elif self.value() == 1:
           self.low()
            if self.__debug:
                print(f"LED connected to Pin {self.__pin} is low")

##### DRY #####
    def on(self):
        # method overriding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the parent class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
           self.off()

```
## Encapsulation
Encapsulation restricts direct access to some of an object's components (such as attributes or methods), meaning the internal representation of the object is hidden from the outside. This is typically achieved by making certain attributes or methods private (i.e., inaccessible from outside the class) and providing public methods (such as getters and setters) to access or modify those private members.

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

## Overloading Polymorphism

**Polymorphism means “many forms.”**

Overloading occurs when a child (subclass) and/or parent (superclass) have multiple methods with the same name but different parameters (number or type).

When you call the method, depending on the parameters passed, the corresponding method is executed.

Because Python is dynamically typed, it does not support overloaded polymorphism, as the last definition of a method overwrites any previous ones.

```pseudocode
Class Led_Light inherits from Pin:
    Method __init__(pin, flashing = False, debug = False):
        Call parent class (Pin) constructor with pin and output mode
        SET led_light_state (property, see below)
        PRIVATE SET debug attribute to debug
        PRIVATE SET pin attribute to pin
        PRIVATE SET flashing attribute to flashing

    METHOD on():
        SET the pin high
        If debug is enabled:
            Print "LED connected to Pin [pin number] is [led_light_state]"

    METHOD off():
        SET the pin low
        IF debug is enabled:
            Print "LED connected to Pin [pin number] is [led_light_state]"

    METHOD toggle():
        IF pin value is 0:
            CALL on()
        ELSE if pin value is 1:
            CALL off()

    METHOD led_light_state ():
        RETURN the pin's current value

    METHOD led_light_state (value):
       IF value is 1:
            CALL off()
        ELSE IF value is 0:
            CALL on()
```

> [!Note]
> The Following Implementation is not technically Polymorphism; it is just a demonstration of the idea that the same method can be called with different parameters.

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

    def on(self):
        # method overriding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        # method overriding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        # method overriding polymorphism of the parent class
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


red_light = Led_Light(3, False, False)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
```
