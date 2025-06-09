# Lecture 5

## Lecture 5 Concepts
- Multiple Inheritance
- Association


## Multiple Inheritance
Multiple Inheritance is used to inherit the properties of 
multiple classes. However, because all the classes we have designed inherit from the built-in 'machine' class you will have conflicts and errors.

This code snippet is just to demonstrate the concept and 
syntax of multiple inheritance. 

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification


class Walk_Light(Audio_Notification, Led_Light):
    def __init__(self, led_pin, buz_pin, debug):
        Led_Light.super().__init__(self, led_pin, debug)
        Audio_Notification.super().__init__(self, buz_pin, debug)

    def walk_on(self):
        if self.__debug:
            print("Beep and Light on")
        self.on()
        self.warning_on()

    def walk_off(self):
        if self.__debug:
            print("Beep and Light off")
        self.off()
        self.warning_off()
```

## Association

Association in Object-Oriented Programming (OOP) describes the relationship between two separate classes that are connected, but neither "owns" the other. It simply means that objects of one class use or interact with objects of another class.

- Association is a broad term for any relationship between classes that is not inheritance.
- It represents a "uses-a" or "knows-a" relationship.
- The lifetime of associated objects is independent—neither object controls the lifecycle of the other.

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification


class Controller:
    def __init__(self, red, green, buz, debug):
        self.__RED = red
        self.__GRN = green
        self.__BUZ = buz
        self.__debug = debug

    def walk_on(self):
        if self.__debug:
            print("Beep and Light on")
        self.__RED.off()
        self.__GRN.flash()
        self.BUZ.warning_on()

    def walk_off(self):
        if self.__debug:
            print("Beep and Light off")
        self.__RED.on()
        self.__GRN.off()
        self.BUZ.warning_off()


LED = v04_Led_Light.Led_Light(19, True)
BUZ = v06_Audio_Notification.Audio_Notification(25, True)

Controller = Controller(LED, BUZ, True)

while True:

```

```python
# Alternative association method
class Walk_Light:
    def __init__(self, led_pin, buz_pin, debug):
        self.LED = Led_Light(led_pin, debug)
        self.BUZ = Audio_Notification(buz_pin, debug)
        self.__debug = debug

    def walk_on(self):
        if self.__debug:
            print("Beep and Light on")
        self.LED.on()
        self.BUZ.warning_on()

    def walk_off(self):
        if self.__debug:
            print("Beep and Light off")
        self.LED.off()
        self.BUZ.warning_off()
```