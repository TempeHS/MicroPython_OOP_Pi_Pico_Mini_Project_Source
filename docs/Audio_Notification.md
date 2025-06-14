# Audio_Notification Class

The `Audio_Notification`  extends the `machine.PWM`  to provide an interface for controlling a piezo buzzer or speaker, with optional debug output. It supports warning beeps and custom tones.

## Constructor

```python
Audio_Notification(pin, debug=False)
```
- `pin`: The GPIO pin number the buzzer is connected to.
- `debug`: Set to `True` to enable debug print statements.

## Example Usage

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

## Methods

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

## Class Unit test

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

## Class Implementation

```python
from machine import Pin, PWM
from time import sleep, time


class Audio_Notification(PWM):
    """
    Audio_Notification extends PWM to provide an interface for controlling a piezo buzzer.

    This class provides methods for generating warning beeps and custom tones
    with optional debug output.

    Args:
        pin (int): The GPIO pin number to which the buzzer is connected
        debug (bool, optional): Enable debug print statements. Defaults to False.
    """

    def __init__(self, pin, debug=False):
        """
        Initialize the Audio_Notification object.

        Args:
            pin (int): The GPIO pin number to which the buzzer is connected
            debug (bool, optional): Enable debug print statements. Defaults to False.
        """
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)  # Start with buzzer off
        self.__last_toggle_time = time()

    def warning_on(self):
        """
        Sound a warning beep if 0.5 seconds have elapsed since the last beep.

        This method is designed to be called repeatedly in a main loop to
        create a periodic warning sound.
        """
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self.__last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now

    def warning_off(self):
        """
        Turn off the buzzer sound.

        This stops any active buzzer output by setting the duty cycle to 0.
        """
        if self.__debug:
            print("Warning off")
        self.duty_u16(0)  # Turn off sound

    def beep(self, freq=1000, duration=500):
        """
        Generate a beep at the specified frequency and duration.

        Note: This is a blocking method that will pause program execution
        for the duration of the beep.

        Args:
            freq (int, optional): Frequency in Hz. Defaults to 1000.
            duration (int, optional): Duration in milliseconds. Defaults to 500.
        """
        self.freq(freq)
        self.duty_u16(32768)  # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0)  # Turn off after beep
        if self.__debug:
            print("Beep")
```