from led_light import LedLight
from controller import TrafficLightSubsystem
from time import sleep

red = LedLight(3, False, True)
amber = LedLight(5, False, True)
green = LedLight(6, False, True)

light = TrafficLightSubsystem(red, amber, green, True) 


def Traffic_Subsystem_Driver():
    print("Testing Traffic Light in 5 seconds")
    sleep(5)
    light.show_red()
    print("Pass if: Red ON, Amber OFF & Green OFF")
    sleep(10)
    # Complete implementation

Traffic_Subsystem_Driver()

    

