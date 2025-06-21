from time import sleep
from led_light import Led_Light

# Replace 3 with a valid GPIO pin number for your board
led = Led_Light(3, flashing=True, debug=True)

print("Testing on()")
led.on()
sleep(0.1)
if led.value() == 1:
    print(".on() method passed")
else:
    print(".on() method failed")

print("Testing off()")
led.off()
sleep(0.1)
if led.value() == 0:
    print(".off() method passed")
else:
    print(".off() method failed")


print("Testing toggle()")
led.toggle()
sleep(0.1)
if led.value() == 1:
    print(".toggle() .on() method passed")
else:
    print(".toggle() .on() method failed")

led.toggle()
sleep(0.1)
if led.value() == 0:
    print(".toggle() .off() method passed")
else:
    print(".toggle() .off() method failed")


print("Testing led_light_state property (getter)")
state = led.led_light_state
sleep(0.1)
if state == led.value():
    print(".led_light_state passed")
else:
    print(".led_light_state getter failed")

print("Testing led_light_state property (setter) to 1 (should turn on)")
set1 = led.led_light_state = 1
set0 = led.led_light_state = 0
if set1 == 1 and set0 == 0:
    print(".led_light_state setter passed")
else:
    print(".led_light_state setter failed")
