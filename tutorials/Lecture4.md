# Lecture 4

## Lecture 4 Concepts
- Implement an advanced button
- Unit test the predestrian button class
- Implement audio notification class
- Unit test the audio notification class

## Advanced Button (with Debouncing and Interrupt)

The `Pedestrian_Button` class extends the `machine.Pin` class to provide a debounced, interrupt-driven interface for a pedestrian button, with optional debug output.

### Constructor

```python
Pedestrian_Button(pin, debug=False)
```
- `pin`: The GPIO pin number the button is connected to.
- `debug`: Set to `True` to enable debug print statements.

### Example Usage

```python
from pedestrian_button import Pedestrian_Button
import time

# Create a Pedestrian_Button on GPIO pin 14 with debug enabled
button = Pedestrian_Button(22, debug=True)

while True:
    # Check if the button has been pressed (pedestrian waiting)
    if button.button_state:
        print("Pedestrian button pressed!")
        # Reset the waiting state after handling
        button.button_state = False
    time.sleep(0.1)
```

### Methods and Properties

- **button_state** (property)  
  - Gets: Returns `True` if the button is pressed or has been pressed since last reset, `False` otherwise. Prints debug info if enabled.
  - Sets: Allows manual reset of the internal waiting state.

- **callback(pin)**  
  Interrupt handler called on button press (rising edge). Handles debouncing and sets the waiting state.

---

**Notes:**  
- The button should be wired between the specified GPIO pin and GND.
- The class uses the internal pull-down resistor and sets up an interrupt for rising edge detection.
- Debouncing is handled in software (200ms).

### Class Unit Test

```python
from time import sleep
from pedestrian_button import Pedestrian_Button

# Replace 22 with the GPIO pin your button is connected to
button = Pedestrian_Button(22, debug=True)

print("Testing initial button_state (should be False if not pressed)")
initial_state = button.button_state
if initial_state is False:
    print("Initial .button_state passed")
else:
    print("Initial .button_state failed")

print("Please press and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    if button.button_state:
        pressed = True
        break
    sleep(0.1)

if pressed:
    print("Button press detected: .button_state passed")
else:
    print("Button press not detected: .button_state failed")

print("Testing button_state setter (reset to False)")
button.button_state = False
sleep(0.1)
if button.button_state is False:
    print(".button_state setter passed")
else:
    print(".button_state setter failed")

print("Manual test complete.")
```
### Class Implementation

```python
from machine import Pin
import time


class Pedestrian_Button(Pin):
    # child class inherits the parent 'Pin' class

    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0  # Track the last time the button was pressed
        self.__pedestrian_waiting = False
        self.button_state
        self.irq(
            trigger=Pin.IRQ_RISING, handler=self.callback
        )  # Set up interrupt on rising edge

    @property
    def button_state(self):
        if self.__debug:
            print(
                f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
            )
        return self.__pedestrian_waiting

    @button_state.setter
    def button_state(self, value):
        self.__pedestrian_waiting = value
        if self.__debug:
            print(f"Button state on Pin {self.__pin} set to {value}")

    def callback(self, pin):
        current_time = time.ticks_ms()  # Get the current time in milliseconds
        if (
            time.ticks_diff(current_time, self.__last_pressed) > 200
        ):  # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
```

## Audio Notification

The `Audio_Notification` class extends the `machine.PWM` class to provide an interface for controlling a piezo buzzer or speaker, with optional debug output. It supports warning beeps and custom tones.

### Constructor

```python
Audio_Notification(pin, debug=False)
```
- `pin`: The GPIO pin number the buzzer is connected to.
- `debug`: Set to `True` to enable debug print statements.

### Example Usage

```python
from audio_notification import Audio_Notification
import time

# Create an Audio_Notification on GPIO pin 15 with debug enabled
buzzer = Audio_Notification(27, debug=True)

# Sound a warning beep (non-blocking, call repeatedly in your loop)
buzzer.warning_on()

# Turn off the buzzer
buzzer.warning_off()

# Make a custom beep: 2kHz for 1 second
buzzer.beep(freq=2000, duration=1000)
```

### Methods

- **warning_on()**  
  Sounds a warning beep (500 Hz, 100 ms) if at least 0.5 seconds have passed since the last beep. Prints debug info if enabled.

- **warning_off()**  
  Turns off the buzzer and prints debug info if enabled.

- **beep(freq=1000, duration=500)**  
  Produces a beep at the specified frequency (Hz) and duration (ms).

---

**Notes:**  
- Use a passive piezo buzzer for best results with PWM.
- The pin must support PWM output on your board.
- Call `warning_on()` repeatedly in your main loop for periodic beeping.

### Class Unit test

```python
from time import sleep
from audio_notification import Audio_Notification

# Replace 18 with the GPIO pin your buzzer is connected to
buzzer = Audio_Notification(18, debug=True)

print("Testing beep()")
buzzer.beep(freq=1000, duration=200)
print("Did you hear a beep? (Check your buzzer)")

print("Testing warning_on() (should beep every ~0.5s for 2 seconds)")
start = buzzer._last_toggle_time
for _ in range(5):
    buzzer.warning_on()
    sleep(0.5)

print("Testing warning_off() (should silence the buzzer)")
buzzer.warning_off()
print("Buzzer should now be off.")

print("Manual test complete.")
```

### Class Implementation

```python
from machine import Pin, PWM
from time import sleep, time


class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)  # Start with buzzer off
        self._last_toggle_time = time()

    def warning_on(self):
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self._last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self._last_toggle_time = now

    def warning_off(self):
        if self.__debug:
            print("Warning off")
        self.duty_u16(0)  # Turn off sound

    def beep(self, freq=1000, duration=500):
        self.freq(freq)
        self.duty_u16(32768)  # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0)  # Turn off after beep

```