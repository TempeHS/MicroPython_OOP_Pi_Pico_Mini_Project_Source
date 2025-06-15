# Lecture 8

## Lecture 7 concepts

- [What Are Stubs and Drivers?](#what-are-stubs-and-drivers)
- [Why Use Stubs and Drivers?](#why-use-stubs-and-drivers)
- [Simple Example](#simple-example)
  - [Stub Example](#stub-example)
  - [Driver Example](#driver-example)
- [How to Use Them Together](#how-to-use-them-together)

## What Are Stubs and Drivers? 

Imagine you're building a puzzle:
- A **stub** is a fake puzzle piece you use temporarily
- A **driver** is a simple tool to check if your real pieces fit together

Definitions
A **stub** is a simplified version that replaces a real lower component so it doesn't need to be full implemented.
A **driver** is a simple program in a higher system that tests a lower component without fully implementing the higher system.

## Why Use Stubs and Drivers?

1. **Test in parts**: Check each piece of your code separately
2. **No dependencies**: Test without needing everything to be finished
3. **Controlled testing**: Create specific test scenarios easily
4. **Faster development**: Don't need to wait for other parts to be done

This simple approach helps you build and test your code without needing to complete your system!

## Simple Example

Let's say we have a simple traffic light system:

```python
# traffic_light.py
class TrafficLight:
    def __init__(self):
        self.color = "red"
    
    def change_color(self):
        if self.color == "red":
            self.color = "green"
        elif self.color == "green":
            self.color = "yellow"
        else:
            self.color = "red"
    
    def get_color(self):
        return self.color
```

### Stub Example

Remember a **stub** is a simplified version that replaces a real lower component so it doesn't need to be full implemented.

```python
# traffic_light_stub.py
class TrafficLightStub:
    def __init__(self):
        self.color = "red"
    
    def change_color(self):
        # Just pretend to change color - always return green for testing
        self.color = "green"
    
    def get_color(self):
        return self.color
```

### Driver Example

Remember a **driver** is a simple program in a higher system that tests a lower component without fully implementing the higher system.

```python
# traffic_light_driver.py

# Import the real component we want to test
from traffic_light import TrafficLight

def test_traffic_light():
    print("Testing Traffic Light...")
    
    # Create the traffic light
    light = TrafficLight()
    
    # Test initial state
    print(f"Initial color: {light.get_color()}")
    
    # Test color change
    light.change_color()
    print(f"After first change: {light.get_color()}")
    
    light.change_color()
    print(f"After second change: {light.get_color()}")
    
    light.change_color()
    print(f"After third change: {light.get_color()}")
    
    print("Test complete!")

# Run the test
test_traffic_light()
```

## How to Use Them Together

You can use the stub to test other parts of your system:

```python
# car_driver.py
from traffic_light_stub import TrafficLightStub

def test_car_behavior():
    print("Testing car behavior at traffic light...")
    
    # Create the stub traffic light
    light = TrafficLightStub()
    
    # Test car behavior
    print(f"Light is {light.get_color()}")
    
    if light.get_color() == "red":
        print("Car stops")
    else:
        print("Car drives")
    
    # Change the light
    light.change_color()
    print(f"Light changed to {light.get_color()}")
    
    if light.get_color() == "red":
        print("Car stops")
    else:
        print("Car drives")
    
    print("Test complete!")

# Run the test
test_car_behavior()
```