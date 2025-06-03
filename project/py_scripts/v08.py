"""
Class association
"""

from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification


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


class Walk_Light2:
    def __init__(self, led, buz, debug):
        self.LED = led
        self.BUZ = buz
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
