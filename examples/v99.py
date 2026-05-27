"""
Completed system ready for System Testing
"""

from led_light import LedLight
from pedestrian_button import PedestrianButton
from audio_notification import AudioNotification
from controller import Controller
from time import sleep, time

debug = False

led_pedestrian_red = LedLight(19, True, debug)
led_pedestrian_green = LedLight(17, False, debug)
led_traffic_red = LedLight(3, False, debug)
led_traffic_amber = LedLight(5, False, debug)
led_traffic_green = LedLight(6, False, debug)
pedestrian_button = PedestrianButton(22, debug)
buzzer = AudioNotification(27, debug)

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
