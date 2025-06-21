"""
Instantiation Example
"""
from machine import Pin
from time import sleep

led_traffic_red = Pin(3, Pin.OUT)
led_traffic_amber = Pin(5, Pin.OUT)
led_traffic_green = Pin(6, Pin.OUT)

while True:
    led_traffic_red.toggle()
    led_traffic_amber.toggle()
    led_traffic_green.toggle()
    sleep(1)
