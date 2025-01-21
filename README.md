# Learn MicroPython Raspberry Pi Pico

This repository is a mini OOP based project to explicitly teach Object Oriented Paradigm programming concepts specifically in the microcontroller context.

Students will be recreating a model of the pedestrian crossing on Unwins Bridge Road out the front of Tempe High School.

![A street view image of the system we will be modeling](/images/real_world_situation.png "The traffic lights, pedestrian warning lights, pedestrian button and control system.")

From the above real world control system we will model:

- The two traffic lights which are synchronised and loop.
- The two pedestrian warning lights which are also synchronised.
- The two pedestrian buttons which break the traffic lights loop.
- The control system that manages the state of the components (large grey box).

## Wire your system

![A prototype of the model](/images/prototype_model.png "Use the below components to wire this model.")

Components

- Breadboard
- Momentary switch
- 5x LED
- 5x 220Ω resistors
- Jumper leads
- Pi Pico

## UML Diagram

```mermaid
classDiagram
    PIN <|-- StaticLight : Inheritance
    PWM <|-- FlashingLight : Inheritance
    PIN <|-- PedestrianButton : Inheritance
    StaticLight --> PedestrianCrossing : Association
    FlashingLight --> PedestrianCrossing : Association
    Button --> PedestrianCrossing : Association
    class PWM{
        int Pin
        int freq
        int duty_u16=8192
        PWM.freq(value)
    }
    class PIN{
        obj PWM
        set_duty(duty)
        get_duty()
    }
    class StaticLight{
        obj Servo
        get_pos()
        set_rot_cw(count)
        set_rot_ccw(count)
    }
    class FlashingLight{
        obj Servo
        int start_angle
        int min_set_angle
        int max_set_angle
        get_angle()
        set_angle(angle)
    }
    class Button{
        obj Servo
        int open_angle
        int closed_angle
        bool claw_state
        set_open()
        set_closed()
        get_state()
    }
    class PedestrianCrossing{
        obj Claw
        obj Base
        obj Elbow
        obj Elbow
        pick_cube()
        place_cube()
    }
```

> [!Note]
> Inheritance and association labels are note required in a UML diagram but have been added for ease of reading.

## Versions

| Version | Notes                                  |
| ------- | -------------------------------------- |
| V01.py  | Test wiring and use basic methods from |

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/TempeHS_PI_Pico_Boilerplate">TempeHS Pi Pico Boilerplate
</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/benpaddlejones">Ben Jones</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
