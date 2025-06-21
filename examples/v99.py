"""
Completed system ready for System Testing
"""

from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import Controller
from time import sleep, time

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
    controller.update()
    sleep(0.1)
