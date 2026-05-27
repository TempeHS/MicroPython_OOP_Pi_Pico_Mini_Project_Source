from machine import Pin, PWM
from time import sleep, time


class AudioNotification(PWM):
    """PWM-based piezo buzzer helper."""

    def __init__(self, pin, debug=False):
        """Initialize an AudioNotification.

        Args:
            pin (int): GPIO pin number for the buzzer.
            debug (bool): True to print debug messages.
        """
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)  # Start with buzzer off
        self.__last_toggle_time = time()

    def warning_on(self):
        """Play periodic warning beeps."""
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self.__last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now

    def warning_off(self):
        """Stop buzzer output."""
        if self.__debug:
            print("Warning off")
        self.duty_u16(0)  # Turn off sound

    def beep(self, freq=1000, duration=500):
        """Play a blocking tone.

        Args:
            freq (int): Tone frequency in Hz.
            duration (int): Tone duration in milliseconds.
        """
        self.freq(freq)
        self.duty_u16(32768)  # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0)  # Turn off after beep
        if self.__debug:
            print("Beep")
