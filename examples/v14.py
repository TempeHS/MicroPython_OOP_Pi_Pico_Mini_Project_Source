"""
Manual Unit Test for Audio_Notification Class
"""

from time import sleep
from audio_notification import Audio_Notification

# Replace 18 with the GPIO pin your buzzer is connected to
buzzer = Audio_Notification(18, debug=True)

print("Testing beep()")
buzzer.beep(freq=1000, duration=200)
print("Did you hear a beep? (Check your buzzer)")

print("Testing warning_on() (should beep every ~0.5s for 2 seconds)")
start = buzzer._last_toggle_time
for _ in range(5):
    buzzer.warning_on()
    sleep(0.5)

print("Testing warning_off() (should silence the buzzer)")
buzzer.warning_off()
print("Buzzer should now be off.")

print("Manual test complete.")
