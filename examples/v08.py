"""
Encapsulation Example
RUN AS PYTHON NOT MICROPYTHON
"""

class Led_Light():
    def __init__(self, pin, flashing=False, debug=False):
        self.debug = debug #PUBLIC attribute
        self.__pin = pin #Encapsulated PRIVATE attribute

red_light = Led_Light(3, False, False)

try:
    print(red_light.debug)
    print("SUCCESS: Accessed a public attribute")
except AttributeError:
    print("ERROR: AttributeError not expected!")

try:
    print(red_light.__pin)
    print("ERROR: Accessed private attribute when it should be hidden!")
except AttributeError:
    print("SUCCESS: AttributeError raised as expected")