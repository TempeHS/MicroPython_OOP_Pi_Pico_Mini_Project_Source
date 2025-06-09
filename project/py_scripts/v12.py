"""
Lecture 3 - Completed Led_light Implementation
"""

from led_light import Led_Light
from time import sleep

# Create a Led_Light on GPIO pin 3, with flashing and debug enabled
led = Led_Light(3, flashing=True, debug=True)

# Turn the LED on
led.on()

# Turn the LED off
led.off()

# Toggle the LED state
led.toggle()

# Set the LED state using the property (0 = ON, 1 = OFF)
led.led_light_state = 0  # Turns LED ON
led.led_light_state = 1  # Turns LED OFF

# Non-blocking flash: call repeatedly in your main loop
while True:
    led.flash()  # Will toggle every 0.5s if flashing is enabled
    sleep(0.1)
