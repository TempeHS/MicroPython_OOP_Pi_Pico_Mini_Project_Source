from machine import Pin, PWM
from time import sleep

class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)  # Start with buzzer off

    def warning_on(self):
        if self.__debug:
            print("Warning on")
        # Generate 3 beeps
        for _ in range(3):
            self.beep(freq=1500, duration=100)
            sleep(0.1)

    def warning_off(self):
        if self.__debug:
            print("Warning off")
        self.duty_u16(0)  # Turn off sound

    def beep(self, freq=1000, duration=500):
        """
        Generate a beep on a piezo buzzer.

        :param freq: frequency in Hz
        :param duration: duration in milliseconds
        """
        self.freq(freq)
        self.duty_u16(32768)  # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0)  # Turn off after beep