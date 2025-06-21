"""
A simple script to unit test hardware
"""

from machine import Pin
from machine import PWM

# Pin Documentation: https://docs.micropython.org/en/latest/library/machine.Pin.html
# PWM Documentation: https://docs.micropython.org/en/latest/library/machine.PWM.html
# Pinout: https://datasheets.raspberrypi.com/pico/Pico-R3-Pinout.png

led_traffic_red = Pin(3, Pin.OUT)
led_traffic_amber = Pin(5, Pin.OUT)
led_traffic_green = Pin(6, Pin.OUT)

led_pedestrian_red = Pin(19, Pin.OUT)
led_pedestrian_green = Pin(17, Pin.OUT)

pedestrian_button = Pin(22, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(27)
buzzer.freq(1000)


while True:

    buzzer.duty_u16(32768)

    led_traffic_red.high()
    led_traffic_amber.high()
    led_traffic_green.high()

    led_pedestrian_red.high()
    led_pedestrian_green.high()

    print(pedestrian_button.value())
