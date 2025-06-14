from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class Controller:
    """
    Controller Class manages the traffic light and pedestrian crossing system state machine.

    This class coordinates the LEDs, buzzer, and button input to manage the sequence
    of traffic and pedestrian signals based on button presses and timing.

    Args:
        ped_red (Led_Light): Red pedestrian LED
        ped_green (Led_Light): Green pedestrian LED
        car_red (Led_Light): Red traffic LED
        car_amber (Led_Light): Amber traffic LED
        car_green (Led_Light): Green traffic LED
        button (Pedestrian_Button): Pedestrian button input
        buzzer (Audio_Notification): Buzzer for pedestrian signals
        debug (bool): Enable debug print statements
    """

    def __init__(
        self, ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug
    ):
        """
        Initialize the Controller with all required hardware components.

        Args:
            ped_red (Led_Light): Red pedestrian LED
            ped_green (Led_Light): Green pedestrian LED
            car_red (Led_Light): Red traffic LED
            car_amber (Led_Light): Amber traffic LED
            car_green (Led_Light): Green traffic LED
            button (Pedestrian_Button): Pedestrian button input
            buzzer (Audio_Notification): Buzzer for pedestrian signals
            debug (bool): Enable debug print statements
        """
        self.__Ped_Red = ped_red
        self.__Ped_Green = ped_green
        self.__Car_Red = car_red
        self.__Car_Amber = car_amber
        self.__Car_Green = car_green
        self.__Buzzer = buzzer
        self.__Button = button
        self.__debug = debug
        self.state = "IDLE"
        self.__last_state_change = time()

    def walk(self):
        """
        Activate the pedestrian walk signal.

        Turns on pedestrian green light, car red light, and warning buzzer.
        Turns off pedestrian red light, car amber and green lights.
        """
        if self.__debug:
            print("Walking")
        self.__Ped_Red.off()
        self.__Ped_Green.on()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_on()

    def walk_warning(self):
        """
        Activate the pedestrian warning signal.

        Flashes pedestrian red light and keeps car red light on.
        Turns off pedestrian green light, car amber and green lights, and buzzer.
        """
        if self.__debug:
            print("No Walking Warning")
        self.__Ped_Red.flash()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_off()

    def idle(self):
        """
        Set the system to idle state.

        Turns on pedestrian red light and car green light.
        Turns off pedestrian green light, car amber and red lights, and buzzer.
        """
        if self.__debug:
            print("No Walking")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.on()
        self.__Car_Amber.off()
        self.__Car_Red.off()
        self.__Buzzer.warning_off()

    def change(self):
        """
        Change the traffic lights from green to amber.

        Turns on pedestrian red light and car amber light.
        Turns off pedestrian green light, car green and red lights, and buzzer.
        """
        if self.__debug:
            print("Changing")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.on()
        self.__Car_Red.off()
        self.__Buzzer.warning_off()

    def update(self):
        """
        Update the state machine based on current state and conditions.

        This method should be called repeatedly in the main program loop to
        handle state transitions based on button presses and timing.
        """
        current_time = time()
        elapsed = current_time - self.__last_state_change

        if self.state == "IDLE":
            if self.__Button.button_state and elapsed > 5:  # Min 5s between crossings
                self.state = "CHANGE"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to CHANGE")
            self.idle()

        elif self.state == "CHANGE":
            if elapsed > 5:  # 5 seconds of amber light
                self.state = "WALK"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to WALK")
            self.change()

        elif self.state == "WALK":
            if elapsed > 5:  # Walk signal for 5 seconds
                if self.__debug:
                    print("Switching to WALK WARNING")
                self.state = "WALK_WARNING"
                self.__last_state_change = current_time
            self.walk()

        elif self.state == "WALK_WARNING":
            if elapsed > 5:  # Walk signal for 5 seconds
                if self.__debug:
                    print("Returning to IDLE")
                self.state = "IDLE"
                self.__last_state_change = current_time
                self.__Button.button_state = False
            self.walk_warning()

        else:  # error state
            self.__Ped_Red.on()
            self.__Ped_Green.off()
            self.__Car_Green.off()
            self.__Car_Amber.toggle()
            self.__Car_Red.off()
            self.__Ped_Green.off()
            sleep(1)
