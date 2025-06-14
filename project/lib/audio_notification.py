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
