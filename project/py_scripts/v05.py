import v04_Led_Light
import v05_Pedestrian_Button

# Abstraction as simple interface hides (farcarde design pattern)
# the complexity of the implementation of the class 'Led_Light' in the module 'v04_Led_Light'

while True:
    red_light = v04_Led_Light.Led_Light(25)
    ped_button = v05_Pedestrian_Button.Button()
    red_light.state = 

