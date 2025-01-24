import v08_Association_Examples
import v04_Led_Light
import v06_Audio_Notification

test = v08_Association_Examples.Walk_Light(17, 27, True)

LED = v04_Led_Light.Led_Light(19, True)
BUZ = v06_Audio_Notification.Audio_Notification(25, True)

test2 = v08_Association_Examples.Walk_Light2(LED, BUZ, True)

while True:
    test2.walk_on()
    test.walk_on()
    print(1)
    time.sleep(1)
    test.walk_off()
    test2.walk_off()
    time.sleep(1)
