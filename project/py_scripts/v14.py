"""
Lecture 4 - Completed Audio_Notification Implementation
"""

from audio_notification import Audio_Notification
import time

# Create an Audio_Notification on GPIO pin 15 with debug enabled
buzzer = Audio_Notification(27, debug=True)

while True:
    # Sound a warning beep (non-blocking, call repeatedly in your loop)
    buzzer.warning_on()
