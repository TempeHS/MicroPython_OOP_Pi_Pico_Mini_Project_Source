"""
Lecture 4 - Manually unit test Pedestrian_Button Implementation
"""

from time import sleep
from pedestrian_button import Pedestrian_Button

# Replace 22 with the GPIO pin your button is connected to
button = Pedestrian_Button(22, debug=True)

print("Testing initial button_state (should be False if not pressed)")
initial_state = button.button_state
if initial_state is False:
    print("Initial .button_state passed")
else:
    print("Initial .button_state failed")

print("Please press and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    if button.button_state:
        pressed = True
        break
    sleep(0.1)

if pressed:
    print("Button press detected: .button_state passed")
else:
    print("Button press not detected: .button_state failed")

print("Testing button_state setter (reset to False)")
button.button_state = False
sleep(0.1)
if button.button_state is False:
    print(".button_state setter passed")
else:
    print(".button_state setter failed")

print("Manual test complete.")