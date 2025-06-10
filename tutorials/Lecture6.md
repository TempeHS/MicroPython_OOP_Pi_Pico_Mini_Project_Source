# Lecture 5

## Lecture 5 concepts

- Open & Closed Loop Control Systems
- Open Loop State Machine

## Open & Closed Loop Control Systems

Open and closed loop control systems are two fundamental types of control systems used in engineering, automation, robotics, and other fields to manage the behavior of devices or processes.

### Open Loop

An open loop control system is a type of system in which the control action is independent of the desired output or the actual system output.

How it works:

- The system receives an input (command or reference signal).
- The controller processes this input and sends a control signal to the actuator.
- The actuator executes the control action, affecting the system or process.
- There is no feedback mechanism to compare the output with the input.

Example:

A microwave oven: You set the cooking time, and the microwave runs for that duration regardless of how hot the food actually gets.

### Closed Loop

A closed loop control system (also called a feedback control system) is a system in which the control action is dependent on the desired output and the actual system output.

How it works:

- The system receives an input (desired value or setpoint).
- The controller processes this input and sends a control signal to the actuator.
- The actuator operates on the system.
- A sensor measures the actual output.
- The output is fed back and compared with the input (setpoint).
- The difference (error) is used to adjust the control action to reduce the error.

Example:

A home thermostat: The home owner sets a desired temperature. The system measures the actual room temperature and adjusts the heater/cooler to reach and maintain the desired temperature. As the system gets closer (or overshoots) to the desired temperature it adjusts the output.

## State Machine

A state machine (also known as a finite state machine or FSM) is a computational model used to design and describe systems that can be in one of a finite number of states at any given time. It transitions between these states in response to external inputs or events such as time, button presses of sensor values.

Key concepts:

- States: Distinct modes or conditions in which the system can exist.
- Transitions: Rules that define how and when the system moves from one state to another, often triggered by events or inputs.
- Events/Inputs: External actions or signals that cause state transitions.
- A State Machince can be open or closed

## Implement a Open Loop State Machine

## Usage: Controller Class (State Machine Example)

The `Controller` class manages the state machine for a pedestrian crossing system, coordinating LEDs, buzzer, and button input. It handles the sequence of traffic and pedestrian signals based on button presses and timing.

### Constructor

```python
Controller(
    ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug
)
```
- `ped_red`, `ped_green`, `car_red`, `car_amber`, `car_green`: Instances of `Led_Light` for each light.
- `button`: An instance of `Pedestrian_Button`.
- `buzzer`: An instance of `Audio_Notification`.
- `debug`: Set to `True` to enable debug print statements.

### Example Usage

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import Controller
from time import sleep

# Instantiate hardware objects
ped_red = Led_Light(19)
ped_green = Led_Light(17, flashing=True)
car_red = Led_Light(3)
car_amber = Led_Light(5)
car_green = Led_Light(6)
button = Pedestrian_Button(22)
buzzer = Audio_Notification(27)

# Create the controller
controller = Controller(
    ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug=True
)

# Main loop
while True:
    controller.update()
    sleep(0.1)
```

### Methods

- **walk_on()**  
  Activates the pedestrian walk signal, turns on the green pedestrian LED, and sounds the buzzer.

- **walk_warning()**  
  Activates the warning state (flashing red pedestrian LED, buzzer off).

- **walk_off()**  
  Deactivates the pedestrian walk signal, turns on the red pedestrian LED, and turns off the buzzer.

- **change()**  
  Changes the traffic lights to amber for cars, preparing for pedestrian crossing.

- **update()**  
  Runs the state machine. Call this method repeatedly (e.g., in a loop) to process button presses and manage signal timing.

### State Machine Overview

- **IDLE**: Waiting for a pedestrian button press.
- **CAR_AMBER**: Amber light for cars, preparing to stop traffic.
- **WALK_ON**: Pedestrian walk signal active, buzzer sounds.
- **WALK_WARNING**: Pedestrian warning state (flashing red, buzzer off).
- **Transitions**: Each state transitions automatically after a set time or event.

---

**Note:**  
- The controller expects the hardware classes (`Led_Light`, `Pedestrian_Button`, `Audio_Notification`) to be implemented and working.
- The button's `button_state` property is set by the button's interrupt handler when pressed.
- Timing and state transitions are handled automatically by the `update()` method.

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class Controller:
    def __init__(
        self, ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug
    ):
        self.__Ped_Red = ped_red
        self.__Ped_Green = ped_green
        self.__Car_Red = car_red
        self.__Car_Amber = car_amber
        self.__Car_Green = car_green
        self.__Buzzer = buzzer
        self.__Button = button
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()

    def walk_on(self):
        if self.__debug:
            print("Walking")
        self.__Ped_Red.off()
        self.__Ped_Green.on()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_on()

    def walk_warning(self):
        if self.__debug:
            print("No Walking Warning")
        self.__Ped_Red.flash()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_off()
        
    def walk_off(self):
        if self.__debug:
            print("No Walking")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.on()
        self.__Car_Amber.off()
        self.__Car_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()

    def change(self):
        if self.__debug:
            print("Changing")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.on()
        self.__Car_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()

    def update(self):
        # State machine logic
        if self.state == "IDLE":
            if self.__Button.button_state:
                if self.__debug:
                    print("Pedestrian waiting detected, switching to CAR_AMBER")
                self.state = "CAR_AMBER"
                self.last_state_change = time()
                self.change()
            else:
                self.walk_off()
        elif self.state == "CAR_AMBER":
            # Wait 10 seconds before allowing walk
            self.change()
            if time() - self.last_state_change > 5:
                if self.__debug:
                    print("Switching to WALK_ON")
                self.state = "WALK_ON"
                self.last_state_change = time()
                self.walk_on()
        elif self.state == "WALK_ON":
            # Walk signal for 5 seconds
            self.walk_on()
            if time() - self.last_state_change > 5:
                if self.__debug:
                    print("Switching to No Walk Warning")
                self.state = "WALK_WARNING"
                self.last_state_change = time()
                self.walk_warning()
        elif self.state == "WALK_WARNING":
            # Walk signal for 5 seconds
            self.walk_warning()
            if time() - self.last_state_change > 5:
                if self.__debug:
                    print("Returning to IDLE")
                self.state = "IDLE"
                self.last_state_change = time()
                self.walk_off()
                self.__Button.button_state = False
        else:  # error
            self.__Ped_Red.on()
            self.__Ped_Green.off()
            self.__Car_Green.off()
            self.__Car_Amber.toggle()
            self.__Car_Red.off()
            self.__Ped_Green.off()
            sleep(1)
```