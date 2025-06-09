"""
Lecture 4 - Completed Pedestrian_Button Implementation
"""

from pedestrian_button import Pedestrian_Button
import time

# Create a Pedestrian_Button on GPIO pin 14 with debug enabled
button = Pedestrian_Button(22, debug=True)

while True:
    # Check if the button has been pressed (pedestrian waiting)
    if button.button_state:
        print("Pedestrian button pressed!")
        # Reset the waiting state after handling
        button.button_state = False
    time.sleep(0.1)
