"""
Association & Controller States Example
"""

from project.py_scripts.LL_unit_Test import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class Controller:
    def __init__(
        self, ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug
    ):
        self.__Ped_Red = ped_red
        self.__Ped_Green = ped_green
        self.__Car_Red = car_red
        self.__Car_Amber = car_amber
        self.__Car_Green = car_green
        self.__Buzzer = buzzer
        self.__Button = button
        self.__debug = debug

    def walk_on(self):
        if self.__debug:
            print("Walking")
        self.__Ped_Red.off()
        self.__Ped_Green.on()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_on()

    def walk_warning(self):
        if self.__debug:
            print("No Walking Warning")
        self.__Ped_Red.flash()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_off()

    def walk_off(self):
        if self.__debug:
            print("No Walking")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.on()
        self.__Car_Amber.off()
        self.__Car_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()

    def change(self):
        if self.__debug:
            print("Changing")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.on()
        self.__Car_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()


debug = False

led_pedestrian_red = Led_Light(19, True, debug)
led_pedestrian_green = Led_Light(17, False, debug)
led_car_red = Led_Light(3, False, debug)
led_car_orange = Led_Light(5, False, debug)
led_car_green = Led_Light(6, False, debug)

pedestrian_button = Pedestrian_Button(22, debug)

buzzer = Audio_Notification(27, debug)

controller = Controller(
    led_pedestrian_red,
    led_pedestrian_green,
    led_car_red,
    led_car_orange,
    led_car_green,
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
