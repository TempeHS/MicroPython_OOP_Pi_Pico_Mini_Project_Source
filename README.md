# MicroPython OOP Pi Pico Mini Project

This repository is a series of introduction tasks to teach students the basics of Pi Pico and common mechatronic components. Then students will create a mini OOP based project to explicitly teach Object Oriented Paradigm (OOP) programming concepts specifically in the microcontroller context.

Students will be recreating a model of the pedestrian crossing on Unwins Bridge Road out the front of Tempe High School.

## Tutorials

| Tutorial | OOP/Pi Pico Concepts Covered |
| --- | --- |
| [Lecture0](tutorials\Lecture0.md) | • Introduction Projects<br>• Wokwi<br>• Wire your system |
| [Lecture1](tutorials\Lecture1.md) | • Unit Testing<br>• UML Class Diagrams<br>• Generalisation<br>• Super/Sub Classes<br>• Instantiation |
| [Lecture2](tutorials\Lecture2.md) | • Overriding Polymorphism<br>• DRY<br>• Encapsulation<br>• Setter and Getters<br>• Overloading Polymorphism  |
| [Lecture3](tutorials\Lecture3.md) | • Abstraction<br>• Non-Blocking |
| [Lecture4](tutorials\Lecture4.md) | • Pull Down Button<br>• Interrupts |
| [Lecture5](tutorials\Lecture5.md) | • PWM<br>• Stubs and Drivers |
| [Lecture6](tutorials\Lecture6.md) | • Multiple Inheritance<br>• Association<br>• Facade pattern<br>• Subsystems |
| [Lecture7](tutorials\Lecture7.md) | • Open & Closed Loop Control Systems<br>• State Machine |

<hr>

## Introduction to Pi Pico & Common Mechatronic Commonents

Students will follow text-based instructions to build simple Pi Pico circuits and implement straightforward procedural programs to test their functionality. These activities will help students understand basic hardware connections and programming concepts while reinforcing their debugging skills.

All projects can be physically wired and tested (see [components list](#components-required)) or simulated and programmed in the IDE of [Wokwi](https://wokwi.com/).

### Projects

1. [Connect and control a LED](introduction_projects/1.blink_led.md)
2. [Connect a digital sensor that controls the LEDs](introduction_projects/2.digital_sensor.md)
3. [Connect a analog sensor that controls the LEDs](introduction_projects/3.analog_sensor.md)
4. [Control the brightness of the LED with Pulse Width Modulation](introduction_projects/4.pulse_width_modulation.md)
5. [Connect and control a servo motor](introduction_projects/5.servo_control.md)
6. [Connect and read a ultrasonic sensor use it to control the servo motor](introduction_projects/6.ultrasonic_sensor.md)
7. [Connect and control a I2C 16x2 LCD Display](introduction_projects/7.I2C_module.md)

### Components Required

> [!Note]
> Students can build using physical components or prototype using this [Template Wokwi Project](https://wokwi.com/projects/433242006092880897).

- Breadboard
- Jumper leads
- Pi Pico
- 1x LED
- 1x 130Ω resistors
- 1x Potentiometer or analog sensor
- 1x Momentary switch or digital sensor
- 1x Servo motor
- 1x Ultrasonic sensor
- 1x 2IC 16x2 LCD Display

### Pin Allocation

| Pin  |                        |
| ---- | ---------------------- |
| GP0  | SDA                    |
| GP1  | SCL                    |
| GP4  | Keyboard Interrupt     |
| GP10 | Servo Motor Signal     |
| GP11 | Ultrasonic Echo Signal |
| GP12 | Ultrasonic Trig Signal |
| GP13 | Digital Sensor Signal  |
| GP15 | External LED           |
| GP25 | Inbuilt LED            |
| GP26 | Analog Sensor Signal   |
| AGND | Analog Ground          |
| GND  | Ground                 |
| 3V3  | 3V Power               |
| VBUS | 5V Power               |

<hr>

## OOP Mini Project

Students will follow text and video-based lectures to develop a pedestrian and traffic controller system using the Pi Pico. Through this system, they will learn a range of Object-Oriented Programming (OOP) concepts and practices, including encapsulation, inheritance, polymorphism, and abstraction. Additionally, students will explore hardware integration concepts such as GPIO pin control, PWM signals, and interrupt handling.

The lectures will guide them through building subsystems like traffic lights and pedestrian signals, implementing state machines, and understanding open-loop and closed-loop control systems. By the end of the course, students will have gained practical experience in designing, testing, and debugging both software and hardware components.

All projects can be physically wired and tested (see [components list](#components)) or simulated and programmed in the IDE of [Wokwi](https://wokwi.com/).

![A street view image of the system we will be modeling](/images/real_world_situation.png "The traffic lights, pedestrian warning lights, pedestrian button and control system.")

### Final Product

![Video of Final Project in Operations](/images/demonstration.gif)

### Wire your system

![A prototype of the model](/images/prototype_model.png "Use the below components to wire this model.")

### Components

> [!Note]
> Students can build using physical components or prototype using this [Template Wokwi Project](https://wokwi.com/projects/433242006092880897).

- Breadboard
- Jumper leads
- Pi Pico
- 1x Momentary switch
- 5x LED
- 1x Piezo buzzer
- 5x 130Ω resistors

### Pin allocation

| Pin  |                      |
| ---- | -------------------- |
| GP3  | Red LED              |
| GP4  | Keyboard Interrupt   |
| GP5  | Amber LED            |
| GP7  | Red LED              |
| GP17 | Flashing Green LED   |
| GP19 | Flashing Red LED     |
| GP22 | Button signal        |
| GP27 | Piezo Buzzer         |
| GND  | Circuit Ground       |
| 3V3  | Button logic voltage |

### Final UML Diagram

```mermaid
classDiagram
    class Pin {
        -__pin: int
        +__init__(pin: int)
        +value()
        +high()
        +low()
        +on()
        +off()
        +toggle()
    }

    class PWM {
        -__pin: int
        +__init__(pin: int)
        +freq(freq: int)
        +duty_u16(duty: int)
    }

    class Led_Light {
        - __debug: bool
        - __pin: int
        - __flashing: int
        - __last_toggle_time: float
        + Led_Light(pin, flashing=False, debug=False)
        + on()
        + off()
        + toggle()
        + flash()
        + led_light_state
        + led_light_state(value)
    }
    Pin <|-- Led_Light : Inheritance

    class Pedestrian_Button {
        - __pin: int
        - __debug: bool
        - __last_pressed: int
        - __pedestrian_waiting: bool
        + Pedestrian_Button(pin, debug)
        + button_state() : bool
        + button_state(value)
        + callback(pin)
    }
    Pin <|-- Pedestrian_Button : Inheritance

    class Audio_Notification {
        - __debug: bool
        - __last_toggle_time: floot
        - __pin: int
        + Audio_Notification(pin, debug=False)
        + warning_on()
        + warning_off()
        + beep(freq=1000, duration=500)
    }
    PWM <|-- Audio_Notification : Inheritance

    class TrafficLightSubsystem {
        -__red: Led_Light
        -__amber: Led_Light
        -__green: Led_Light
        -__debug: bool
        +__init__(red: Led_Light, amber: Led_Light, green: Led_Light, debug: bool)
        +show_red()
        +show_amber()
        +show_green()
    }
    Led_Light --> TrafficLightSubsystem : Association

    class PedestrianSubsystem {
        -__red: Led_Light
        -__green: Led_Light
        -__button: Pedestrian_Button
        -__buzzer: Audio_Notification
        -__debug: bool
        +__init__(red: Led_Light, green: Led_Light, button: Pedestrian_Button, buzzer: Audio_Notification, debug: bool)
        +show_stop()
        +show_walk()
        +show_warning()
        +is_button_pressed() bool
        +reset_button()
    }
    Led_Light --> PedestrianSubsystem : Association
    Audio_Notification --> PedestrianSubsystem : Association
    Pedestrian_Button --> PedestrianSubsystem : Association

    class Controller {
        -__traffic_lights: TrafficLightSubsystem
        -__pedestrian_signals: PedestrianSubsystem
        -__debug: bool
        -__last_state_change: float
        +state: string
        +__init__(ped_red: Led_Light, ped_green: Led_Light, traffic_red: Led_Light, traffic_amber: Led_Light, traffic_green: Led_Light, button: Pedestrian_Button, buzzer: Audio_Notification, debug: bool)
        +set_idle_state()
        +set_change_state()
        +set_walk_state() 
        +set_warning_state()
        +set_error_state()
        +update()
    }  

    TrafficLightSubsystem --o Controller : Contains
    PedestrianSubsystem --o Controller : Contains   
```

## Script Versions Provided

| Version | Notes                                                                                                                     |
| ------- | ------------------------------------------------------------------------------------------------------------------------- |
| v01.py  | Basic "Blink" Program (the Hello World of mechatronics) for Unit Testing the Microcontroller.                                                                  |
| v02.py  | Unit Test for wiring and use basic methods from Super `Pin` and `PWM` .                                                                |

##

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/MicroPython_OOP_Pi_Pico_Mini_Project_Source">MicroPython_OOP_Pi_Pico_Mini_Project_Source
</a> and <a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/MicroPython_OOP_Pi_Pico_Mini_Project_Template">MicroPython_OOP_Pi_Pico_Mini_Project_Template
</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/benpaddlejones">Ben Jones</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
