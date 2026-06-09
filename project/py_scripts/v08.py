from led_light import LedLight
from pedestrian_button import PedestrianButton
from audio_notification import AudioNotification
from controller import PedestrianSubsystem
from time import sleep, time

ped_red = LedLight(19, True, True)
ped_green = LedLight(17, False, True)
button = PedestrianButton(22, True)
buzzer = AudioNotification(27, True)

pedestrian = PedestrianSubsystem(ped_red, ped_green, button, buzzer, True)


def Pedestrian_Subsystem_Driver():
    print("Testing Pedestrian Subsystem in 5 seconds")
    sleep(5)

    pedestrian.show_stop()
    print("Pass if: Ped Red ON, Ped Green OFF & Buzzer OFF")
    sleep(10)

    pedestrian.show_walk()
    print("Pass if: Ped Red OFF, Ped Green ON & Buzzer beeping")
    sleep(10)

    warning_start = time()
    while time() - warning_start < 10:
        pedestrian.show_warning()
        sleep(0.05)
    print("Pass if: Ped Red FLASHING, Ped Green OFF & Buzzer OFF")

    print("Press the pedestrian button within 5 seconds...")
    sleep(5)
    if pedestrian.is_button_pressed():
        print("Pass: button press detected")
    else:
        print("Fail: button press not detected")

    pedestrian.reset_button()
    if not pedestrian.is_button_pressed():
        print("Pass: button state reset")
    else:
        print("Fail: button state not reset")


Pedestrian_Subsystem_Driver()
