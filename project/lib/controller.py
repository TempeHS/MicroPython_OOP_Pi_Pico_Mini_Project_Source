from led_light import LedLight
from pedestrian_button import PedestrianButton
from audio_notification import AudioNotification
from time import sleep, time


class TrafficLightSubsystem:
    """Manage vehicle traffic lights."""

    def __init__(self, red, amber, green, debug=False):
        """Initialize a TrafficLightSubsystem.

        Args:
            red (LedLight): Red traffic light.
            amber (LedLight): Amber traffic light.
            green (LedLight): Green traffic light.
            debug (bool): True to print debug messages.
        """
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug

    def show_red(self):
        """Show red for traffic."""
        if self.__debug:
            print("Traffic: Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        """Show amber for traffic."""
        if self.__debug:
            print("Traffic: Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        """Show green for traffic."""
        if self.__debug:
            print("Traffic: Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()


class PedestrianSubsystem:
    """Manage pedestrian lights, button, and buzzer."""

    def __init__(self, red, green, button, buzzer, debug=False):
        """Initialize a PedestrianSubsystem.

        Args:
            red (LedLight): Red pedestrian light.
            green (LedLight): Green pedestrian light.
            button (PedestrianButton): Crossing request button.
            buzzer (AudioNotification): Audible notifier.
            debug (bool): True to print debug messages.
        """
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug

    def show_stop(self):
        """Show stop signal to pedestrians."""
        if self.__debug:
            print("Pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()

    def show_walk(self):
        """Show walk signal to pedestrians."""
        if self.__debug:
            print("Pedestrian: Green ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_on()

    def show_warning(self):
        """Show crossing-ending warning to pedestrians."""
        if self.__debug:
            print("Pedestrian: Warning")
        self.__red.flash()
        self.__green.off()
        self.__buzzer.warning_off()

    def is_button_pressed(self):
        """Return whether a crossing request is active.

        Returns:
            bool: True if pressed, else False.
        """
        return self.__button.button_state

    def reset_button(self):
        """Clear the crossing request state."""
        self.__button.button_state = False


class Controller:
    """Coordinate traffic and pedestrian crossing states."""

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
        """Initialize a Controller.

        Args:
            ped_red (LedLight): Red pedestrian light.
            ped_green (LedLight): Green pedestrian light.
            traffic_red (LedLight): Red traffic light.
            traffic_amber (LedLight): Amber traffic light.
            traffic_green (LedLight): Green traffic light.
            button (PedestrianButton): Pedestrian request button.
            buzzer (AudioNotification): Pedestrian buzzer.
            debug (bool): True to print debug messages.
        """
        # Initialise subsystems
        self.__traffic_lights = TrafficLightSubsystem(
            traffic_red, traffic_amber, traffic_green, debug
        )
        self.__pedestrian_signals = PedestrianSubsystem(
            ped_red, ped_green, button, buzzer, debug
        )

        # Other controller attributes
        self.__debug = debug
        self.state = "IDLE"
        self.__last_state_change = time()

    def set_idle_state(self):
        """Set IDLE outputs."""
        if self.__debug:
            print("System: IDLE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_green()

    def set_change_state(self):
        """Set CHANGE outputs."""
        if self.__debug:
            print("System: CHANGE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()

    def set_walk_state(self):
        """Set WALK outputs."""
        if self.__debug:
            print("System: WALK state")
        self.__pedestrian_signals.show_walk()
        self.__traffic_lights.show_red()

    def set_error_state(self):
        """Set ERROR outputs."""
        if self.__debug:
            print("System: ERROR state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()  # Flashing amber typically indicates malfunction

    def update(self):
        """Advance the crossing state machine."""
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

    def set_warning_state(self):
        """Set WALK_WARNING outputs."""
        if self.__debug:
            print("System: WALK WARNING state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()
