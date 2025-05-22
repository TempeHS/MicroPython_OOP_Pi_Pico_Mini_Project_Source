from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
import time


red_light = Led_Light.Led_Light(3, False)
ped_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

while True:
    buzzer.warning_on()
    time.sleep(1)
    red_light.led_light_state = ped_button.button_state
    buzzer.warning_off()
    time.sleep(1)
