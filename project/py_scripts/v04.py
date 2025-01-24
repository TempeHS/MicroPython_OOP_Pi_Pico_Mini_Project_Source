import v04_Led_Light
import time

# Abstraction as simple interface hides (facade design pattern)
# the complexity of the implementation of the class 'Led_Light' in the module 'v04_Led_Light'

red_light = Led_Light(3, True)

while True:
    red_light.toggle()
    time.sleep(0.5)
