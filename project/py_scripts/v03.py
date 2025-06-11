"""
Lecture 1 - Instantiation
"""

from machine import Pin
from time import sleep

led_car_red = Pin(3, Pin.OUT)
led_car_orange = Pin(5, Pin.OUT)
led_car_green = Pin(6, Pin.OUT)

while True:
    led_car_red.toggle()
    sleep(1)
