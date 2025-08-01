# Controller Class

The `Controller` class acts as a **Facade** for the traffic and pedestrian crossing system. It provides a simplified interface to the underlying subsystems that manage traffic lights and pedestrian signals, and implements a state machine to control the crossing sequence and timing.

## Constructor

```python
Controller(
    ped_red,
    ped_green,
    traffic_red,
    traffic_amber,
    traffic_green,
    button,
    buzzer,
    debug=False
)
```
- `ped_red` (`Led_Light`): Red pedestrian light
- `ped_green` (`Led_Light`): Green pedestrian light
- `traffic_red` (`Led_Light`): Red traffic light
- `traffic_amber` (`Led_Light`): Amber traffic light
- `traffic_green` (`Led_Light`): Green traffic light
- `button` (`Pedestrian_Button`): Pedestrian crossing button
- `buzzer` (`Audio_Notification`): Crossing buzzer
- `debug` (`bool`, optional): Enable debug output (default `False`)

## Example Usage

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import Controller
import time

traffic_red = Led_Light(3, debug=False)
traffic_amber = Led_Light(5, debug=False)
traffic_green = Led_Light(7, debug=False)
ped_red = Led_Light(17, debug=False)
ped_green = Led_Light(19, debug=False)
button = Pedestrian_Button(22, debug=False)
buzzer = Audio_Notification(27, debug=False)

controller = Controller(
    ped_red, ped_green, traffic_red, traffic_amber, traffic_green,
    button, buzzer, debug=True
)

while True:
    controller.update()
    time.sleep(0.1)
```

## Methods

- **set_idle_state()**: Set the system to idle state: traffic flows, pedestrians stopped.
- **set_change_state()**: Transition to stop traffic: amber light for vehicles, pedestrians wait.
- **set_walk_state()**: Allow pedestrians to cross: red light for vehicles, green for pedestrians.
- **set_warning_state()**: Warn pedestrians crossing time is ending: red traffic light, flashing pedestrian signal.
- **set_error_state()**: Set an error state: amber traffic light, pedestrian "don't walk" signal.
- **update()**: Advance the state machine according to timing and button input. Should be called in the main loop.

## State Machine Logic

- **IDLE**: Traffic flows, pedestrians wait (default state)
- **CHANGE**: Amber light for vehicles, prepares to stop traffic
- **WALK**: Red light for vehicles, green light/buzzer for pedestrians to cross
- **WALK_WARNING**: Red traffic light, pedestrian warning (flashing light, buzzer off)
- **IDLE**: Returns to idle after crossing

## Subsystems

**TrafficLightSubsystem**  
Manages vehicle traffic signals.  
Methods: `show_red()`, `show_amber()`, `show_green()`

**PedestrianSubsystem**  
Manages pedestrian signals, button input, and audio notifications.  
Methods: `show_stop()`, `show_walk()`, `show_warning()`, `is_button_pressed()`, `reset_button()`

## Class Unit Test

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import Controller
from time import sleep

traffic_red = Led_Light(3, debug=True)
traffic_amber = Led_Light(5, debug=True)
traffic_green = Led_Light(7, debug=True)
ped_red = Led_Light(17, debug=True)
ped_green = Led_Light(19, debug=True)
button = Pedestrian_Button(22, debug=True)
buzzer = Audio_Notification(27, debug=True)

controller = Controller(
    ped_red, ped_green, traffic_red, traffic_amber, traffic_green,
    button, buzzer, debug=True
)

print("Testing initial state (should be IDLE)")
if controller.state == "IDLE":
    print("Initial state test passed")
else:
    print("Initial state test failed")

print("Testing state cycle - press the button within 5 seconds")
sleep(5)

print("Running through complete state cycle...")
for _ in range(25):
    controller.update()
    print(f"Current state: {controller.state}")
    sleep(1)

print("Manual test complete - verify state transitions in debug output.")
```

## Class Implementation

```python
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class TrafficLightSubsystem:
    """
    Manages traffic light signals for vehicles.

    This subsystem controls the red, amber, and green traffic lights
    that regulate vehicle traffic at a pedestrian crossing.

    Attributes:
        __red (Led_Light): Red traffic light for vehicles
        __amber (Led_Light): Amber traffic light for vehicles
        __green (Led_Light): Green traffic light for vehicles
        __debug (bool): Whether to print debug statements
    """

    def __init__(self, red, amber, green, debug=False):
        """
        Initialize the traffic light subsystem.

        Args:
            red (Led_Light): Red traffic light for vehicles
            amber (Led_Light): Amber traffic light for vehicles
            green (Led_Light): Green traffic light for vehicles
            debug (bool, optional): Enable debug output. Defaults to False.
        """
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug

    def show_red(self):
        """
        Activate the red traffic light and deactivate others.

        Signals vehicles to stop at the crossing.
        """
        if self.__debug:
            print("Traffic: Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        """
        Activate the amber traffic light and deactivate others.

        Signals vehicles to prepare to stop or proceed with caution.
        """
        if self.__debug:
            print("Traffic: Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        """
        Activate the green traffic light and deactivate others.

        Signals vehicles that they may proceed through the crossing.
        """
        if self.__debug:
            print("Traffic: Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()


class PedestrianSubsystem:
    """
    Manages pedestrian signals, crossing button, and audio notifications.

    This subsystem controls the red/green pedestrian lights, crossing button,
    and buzzer that together form the pedestrian interface of the crossing.

    Attributes:
        __red (Led_Light): Red pedestrian light (don't walk)
        __green (Led_Light): Green pedestrian light (walk)
        __button (Pedestrian_Button): Button for pedestrians to request crossing
        __buzzer (Audio_Notification): Audible notification device
        __debug (bool): Whether to print debug statements
    """

    def __init__(self, red, green, button, buzzer, debug=False):
        """
        Initialize the pedestrian subsystem.

        Args:
            red (Led_Light): Red pedestrian light (don't walk)
            green (Led_Light): Green pedestrian light (walk)
            button (Pedestrian_Button): Crossing request button
            buzzer (Audio_Notification): Audible notification device
            debug (bool, optional): Enable debug output. Defaults to False.
        """
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug

    def show_stop(self):
        """
        Show 'don't walk' signal to pedestrians.

        Activates the red pedestrian light, deactivates green light,
        and turns off the warning buzzer.
        """
        if self.__debug:
            print("Pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()

    def show_walk(self):
        """
        Show 'walk' signal to pedestrians.

        Activates the green pedestrian light, deactivates red light,
        and turns on the crossing buzzer.
        """
        if self.__debug:
            print("Pedestrian: Green ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_on()

    def show_warning(self):
        """
        Show warning signal to pedestrians that crossing time is ending.

        Flashes the red light, turns off green light, and disables buzzer.
        """
        if self.__debug:
            print("Pedestrian: Warning")
        self.__red.flash()
        self.__green.off()
        self.__buzzer.warning_off()

    def is_button_pressed(self):
        """
        Check if the pedestrian crossing button has been pressed.

        Returns:
            bool: True if button is pressed, False otherwise.
        """
        return self.__button.button_state

    def reset_button(self):
        """
        Reset the pedestrian crossing button state.

        Called after the crossing cycle completes to reset for next use.
        """
        self.__button.button_state = False


class Controller:
    """
    Facade for the traffic and pedestrian crossing system.

    Provides a simplified interface to the complex subsystems that manage
    traffic lights and pedestrian signals. Implements a state machine to
    control the crossing sequence and timing.

    Attributes:
        __traffic_lights (TrafficLightSubsystem): Manages vehicle traffic signals
        __pedestrian_signals (PedestrianSubsystem): Manages pedestrian signals
        __debug (bool): Whether to print debug statements
        state (str): Current state of the crossing system
        __last_state_change (float): Timestamp of the last state transition
    """

    def __init__(
        self,
        ped_red,
        ped_green,
        traffic_red,
        traffic_amber,
        traffic_green,
        button,
        buzzer,
        debug=False,
    ):
        """
        Initialize the crossing controller.

        Args:
            ped_red (Led_Light): Red pedestrian light
            ped_green (Led_Light): Green pedestrian light
            traffic_red (Led_Light): Red traffic light
            traffic_amber (Led_Light): Amber traffic light
            traffic_green (Led_Light): Green traffic light
            button (Pedestrian_Button): Pedestrian crossing button
            buzzer (Audio_Notification): Crossing buzzer
            debug (bool, optional): Enable debug output. Defaults to False.
        """
        # Initialize subsystems
        self.__traffic_lights = TrafficLightSubsystem(
            traffic_red, traffic_amber, traffic_green, debug
        )
        self.__pedestrian_signals = PedestrianSubsystem(
            ped_red, ped_green, button, buzzer, debug
        )

        # Other controller properties
        self.__debug = debug
        self.state = "IDLE"
        self.__last_state_change = time()

    def set_idle_state(self):
        """
        Set system to idle state with traffic flowing and pedestrians stopped.

        This is the default state when no pedestrian is waiting to cross.
        """
        if self.__debug:
            print("System: IDLE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_green()

    def set_change_state(self):
        """
        Set system to changing state - preparing to stop traffic.

        This transition state displays amber light to warn vehicles to slow down.
        """
        if self.__debug:
            print("System: CHANGE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()

    def set_walk_state(self):
        """
        Set system to walk state - allowing pedestrians to cross.

        Stops vehicle traffic with red light and signals pedestrians it's safe to cross.
        """
        if self.__debug:
            print("System: WALK state")
        self.__pedestrian_signals.show_walk()
        self.__traffic_lights.show_red()

    def set_warning_state(self):
        """
        Set system to warning state - indicating walk signal ending soon.

        Warns pedestrians that crossing time is ending while keeping traffic stopped.
        """
        if self.__debug:
            print("System: WALK WARNING state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()

    def set_error_state(self):
        """
        Set system to error state.

        This state is activated when an unexpected condition occurs.
        Shows amber traffic light and don't walk pedestrian signal.
        """
        if self.__debug:
            print("System: ERROR state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()  # Flashing amber typically indicates malfunction

    def update(self):
        """
        Update the state machine based on current state and conditions.

        This is the main interface method that clients call to operate the entire system.
        It manages state transitions based on timing and pedestrian button input.

        The system cycles through the following states:
        - IDLE: Normal operation, traffic flowing
        - CHANGE: Transitioning to stop traffic (amber light)
        - WALK: Pedestrians crossing (red traffic light, green pedestrian light)
        - WALK_WARNING: Warning that walk cycle is ending
        - Back to IDLE
        """
        current_time = time()
        elapsed = current_time - self.__last_state_change

        if self.state == "IDLE":
            if self.__pedestrian_signals.is_button_pressed() and elapsed > 5:
                self.state = "CHANGE"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to CHANGE")
            self.set_idle_state()

        elif self.state == "CHANGE":
            if elapsed > 5:
                self.state = "WALK"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to WALK")
            self.set_change_state()

        elif self.state == "WALK":
            if elapsed > 5:
                self.state = "WALK_WARNING"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to WALK WARNING")
            self.set_walk_state()

        elif self.state == "WALK_WARNING":
            if elapsed > 5:
                self.state = "IDLE"
                self.__last_state_change = current_time
                self.__pedestrian_signals.reset_button()
                if self.__debug:
                    print("Returning to IDLE")
            self.set_warning_state()

        else:  # error state
            self.set_error_state()
            sleep(1)
```