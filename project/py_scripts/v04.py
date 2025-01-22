import v04_Led_Light

# Abstraction as simple interface hides (facade design pattern)
# the complexity of the implementation of the class 'Led_Light' in the module 'v04_Led_Light'

while True:
    red_light = v04_Led_Light.Led_Light(25)
    red_light.on()
    print(red_light.led_light_state)
