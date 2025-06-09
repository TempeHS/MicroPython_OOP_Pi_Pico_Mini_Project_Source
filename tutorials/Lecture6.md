import v08_Association_Examples
import v04_Led_Light
import v06_Audio_Notification
from machine import RTC

rtc = RTC()

LED = v04_Led_Light.Led_Light(19, True)
BUZ = v06_Audio_Notification.Audio_Notification(25, True)

test = v08_Association_Examples.Walk_Light(17, 27, True)

test2 = v08_Association_Examples.Walk_Light2(LED, BUZ, True)

time_last_change = rtc.datetime()
machine_state = 1
state_1_time = 3
state_1_state = 500
state_2_time = 6
state_2_state = 1000
state_3_time = 9
state_3_state = 1500
state_4_time = 12
state_4_state = 2000


while True:
    time_now = rtc.datetime()

    if machine_state == 1:
        my_servo.set_duty(state_1_state)
        if time_now[6] - time_last_change[6] >= state_1_time:
            machine_state = 2
    elif machine_state == 2:
        my_servo.set_duty(state_2_state)
        if time_now[6] - time_last_change[6] >= state_2_time:
            machine_state = 3
    elif machine_state == 3:
        my_servo.set_duty(state_3_state)
        if time_now[6] - time_last_change[6] >= state_3_time:
            machine_state = 4
    elif machine_state == 4:
        my_servo.set_duty(state_4_state)
        if time_now[6] - time_last_change[6] >= state_4_time:
            time_last_change = rtc.datetime()
            machine_state = 1
