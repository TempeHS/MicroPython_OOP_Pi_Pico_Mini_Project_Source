import v04_Led_Light
import v05_Pedestrian_Button
import v06_Audio_Notification

import time

# Abstraction as simple interface hides (farcarde design pattern)
# the complexity of the implementation of the class 'Led_Light' in the module 'v04_Led_Light'

red_light = v04_Led_Light.Led_Light(3, False)
ped_button = v05_Pedestrian_Button.Pedestrian_Button(22, True)
buzzer = v06_Audio_Notification.Audio_Notification(27, True)

while True:
    buzzer.warning_on()
    time.sleep(1)
    red_light.led_light_state = ped_button.button_state
    buzzer.warning_off()
    time.sleep(1)
