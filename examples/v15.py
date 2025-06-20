"""
Association & Controller States Example
"""

from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class Controller:
    def __init__(
        self, ped_red, ped_green, traffic_red, traffic_amber, traffic_green, button, buzzer, debug
    ):
        self.__Ped_Red = ped_red
        self.__Ped_Green = ped_green
        self.__traffic_Red = traffic_red
        self.__traffic_Amber = traffic_amber
        self.__traffic_Green = traffic_green
        self.__Buzzer = buzzer
        self.__Button = button
        self.__debug = debug

    def walk_on(self):
        if self.__debug:
            print("Walking")
        self.__Ped_Red.off()
        self.__Ped_Green.on()
        self.__traffic_Green.off()
        self.__traffic_Amber.off()
        self.__traffic_Red.on()
        self.__Buzzer.warning_on()

    def walk_warning(self):
        if self.__debug:
            print("No Walking Warning")
        self.__Ped_Red.flash()
        self.__Ped_Green.off()
        self.__traffic_Green.off()
        self.__traffic_Amber.off()
        self.__traffic_Red.on()
        self.__Buzzer.warning_off()

    def walk_off(self):
        if self.__debug:
            print("No Walking")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__traffic_Green.on()
        self.__traffic_Amber.off()
        self.__traffic_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()

    def change(self):
        if self.__debug:
            print("Changing")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__traffic_Green.off()
        self.__traffic_Amber.on()
        self.__traffic_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()


debug = False

led_pedestrian_red = Led_Light(19, True, debug)
led_pedestrian_green = Led_Light(17, False, debug)
led_traffic_red = Led_Light(3, False, debug)
led_traffic_amber = Led_Light(5, False, debug)
led_traffic_green = Led_Light(6, False, debug)

pedestrian_button = Pedestrian_Button(22, debug)

buzzer = Audio_Notification(27, debug)

controller = Controller(
    led_pedestrian_red,
    led_pedestrian_green,
    led_traffic_red,
    led_traffic_amber,
    led_traffic_green,
    pedestrian_button,
    buzzer,
    True,
)

while True:
    controller.walk_off()
    sleep(3)
    controller.change()
    sleep(3)
    controller.walk_on()
    sleep(3)
    controller.walk_warning()
    sleep(3)
