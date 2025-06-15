# Lecture 5

## Lecture 5 Concepts
- [Class Overview](#class-overview)
- [Create Files](#create-files)
- [Imports and Constructor](#imports-and-constructor)
- [Create a Single Beep](#create-a-single-beep)
- [Implement a Non Blocking Audio Notification](#implement-a-non-blocking-audio-notification)
- [Turn Audio Notification Off](#turn-audio-notification-off)

## Class Overview

The Audio_Notification extends the machine.PWM to provide an interface for controlling a piezo buzzer or speaker, with optional debug output. It supports warning beeps and custom tones.

## Create Files

1. Create a Python file in `project\lib` called `audio_notification.py`
2. Create a Python file in `project\py_scripts` called `v06.py`

## Imports and Constructor

In your `audio_notification.py` include your imports, define the class and configure the initialiser with the paramters pin and debug. Add the required parameters to store time and hold state when the button has been pressed.

```python
from machine import Pin, PWM
from time import sleep, time


class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)  # Start with buzzer off
        self.__last_toggle_time = time()
```
## Create a Single Beep

```python
    def beep(self, freq=1000, duration=500):
        self.freq(freq)
        self.duty_u16(32768)  # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0)  # Turn off after beep
        if self.__debug:
            print("Beep")
```
## Implement a Non Blocking Audio Notification

```python
    def warning_on(self):
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self.__last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now
```
## Turn Audio Notification Off

```python
    def warning_off(self):
        if self.__debug:
            print("Warning off")
        self.duty_u16(0)  # Turn off sound
```

