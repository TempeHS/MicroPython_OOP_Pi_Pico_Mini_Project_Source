from machine import PWM


class Servo:
    """Control a servo motor using PWM pulse widths."""

    def __init__(
        self,
        pwm: PWM,
        min_us=500,
        max_us=2500,
        dead_zone_us=1500,
        freq=50,
    ):
        """Initialize a Servo instance.

        Args:
            pwm (PWM): PWM object used to drive the servo.
            min_us (int): Minimum pulse width in microseconds.
            max_us (int): Maximum pulse width in microseconds.
            dead_zone_us (int): Neutral pulse width in microseconds.
            freq (int): PWM frequency in Hz.
        """
        self.pwm = pwm
        self.pwm.freq(freq)
        self._move_period_ms = 1000 // freq
        min_us = min_us if min_us > 0 else 0
        max_us = max_us if min_us < max_us < (1000 // freq) * 1000 else 0
        self._curr_duty = 0
        self.dead_zone_us = dead_zone_us

    def set_duty(self, duty_us: int):
        """Set PWM pulse width.

        Args:
            duty_us (int): Pulse width in microseconds.
        """
        self._curr_duty = duty_us
        self.pwm.duty_ns(duty_us * 1000)

    def set_angle(self, angle: int):
        """Set servo angle.

        Args:
            angle (int): Target angle in degrees. Clamped to 0-180.
        """
        angle = min(max(angle, 0), 180)
        duty_us = int(500 + (angle / 180) * 2000)
        self.set_duty(duty_us)

    def get_duty(self) -> int:
        """Return current pulse width.

        Returns:
            int: Pulse width in microseconds.
        """
        return self._curr_duty

    def stop(self):
        """Move the servo to its neutral position."""
        self.set_duty(self.dead_zone_us)

    def deinit(self):
        """Release the underlying PWM resource."""
        self.pwm.deinit()
