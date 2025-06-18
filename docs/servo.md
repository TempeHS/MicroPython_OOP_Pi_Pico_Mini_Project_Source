# Servo Class

The `Servo` class provides an interface for controlling standard hobby servo motors using PWM signals on the Raspberry Pi Pico. It allows you to set the servo angle, control the duty cycle directly, and safely stop or deinitialize the servo.

## Constructor

```python
Servo(pwm, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
```
- `pwm` (`PWM`): A `machine.PWM` object for the servo control pin.
- `min_us` (`int`, optional): Minimum pulse width in microseconds (default: 500).
- `max_us` (`int`, optional): Maximum pulse width in microseconds (default: 2500).
- `dead_zone_us` (`int`, optional): Pulse width for the servo's neutral position (default: 1500).
- `freq` (`int`, optional): PWM frequency in Hz (default: 50).

## Example Usage

```python
from machine import Pin, PWM
from servo import Servo
from time import sleep

# Create a PWM object on GPIO 16
pwm = PWM(Pin(16))
servo = Servo(pwm, freq=50)

# Move servo to 0, 90, and 180 degrees
servo.set_angle(0)
sleep(1)
servo.set_angle(90)
sleep(1)
servo.set_angle(180)
sleep(1)

# Stop the servo (move to neutral position)
servo.stop()

# Deinitialize when done
servo.deinit()
```

## Methods

- **set_angle(angle)**  
  Set the servo to a specific angle (0–180 degrees).

- **set_duty(duty_us)**  
  Set the PWM pulse width in microseconds directly.

- **get_duty()**  
  Get the current PWM pulse width in microseconds.

- **stop()**  
  Move the servo to the neutral (dead zone) position.

- **deinit()**  
  Deinitialize the PWM object to free hardware resources.

---

**Notes:**  
- The servo must be powered appropriately; do not power directly from the Pico's 3.3V pin if your servo draws significant current.
- The control pin must support PWM output.
- Typical servos expect a 50Hz PWM signal with pulse widths between 500μs (0°) and 2500μs (180°).

## Class Unit Test

```python
from machine import Pin, PWM
from servo import Servo
from time import sleep

pwm = PWM(Pin(16))
servo = Servo(pwm)

print("Testing set_angle()")
for angle in [0, 90, 180, 90, 0]:
    servo.set_angle(angle)
    print(f"Set angle to {angle}°; duty = {servo.get_duty()}us")
    sleep(1)

print("Testing stop()")
servo.stop()
print(f"Servo stopped at duty = {servo.get_duty()}us")

servo.deinit()
print("Servo deinitialized.")
```

## Class Implementation

```python
from machine import PWM

class Servo:
    """Servo Class for controlling pulse density modulation servos.

    This class provides an interface for controlling servo motors using PWM signals.
    It handles the conversion between angles (0-180 degrees) and pulse widths.

    Args:
        pwm (PWM): A PWM object to control the servo.
        min_us (int, optional): Minimum pulse width in microseconds. Defaults to 500.
        max_us (int, optional): Maximum pulse width in microseconds. Defaults to 2500.
        dead_zone_us (int, optional): Pulse width for the servo's neutral position. Defaults to 1500.
        freq (int, optional): PWM frequency in Hz. Defaults to 50.
    """

    def __init__(
        self,
        pwm: PWM,
        min_us=500,
        max_us=2500,
        dead_zone_us=1500,
        freq=50,
    ):
        self.pwm = pwm
        self.pwm.freq(freq)
        self._move_period_ms = 1000 // freq
        min_us = min_us if min_us > 0 else 0
        max_us = max_us if min_us < max_us < (1000 // freq) * 1000 else 0
        self._curr_duty = 0
        self.dead_zone_us = dead_zone_us

    def set_duty(self, duty_us: int):
        self._curr_duty = duty_us
        self.pwm.duty_ns(duty_us * 1000)

    def set_angle(self, angle: int):
        angle = min(max(angle, 0), 180)
        duty_us = int(500 + (angle / 180) * 2000)
        self.set_duty(duty_us)

    def get_duty(self) -> int:
        return self._curr_duty

    def stop(self):
        self.set_duty(self.dead_zone_us)

    def deinit(self):
        self.pwm.deinit()
```