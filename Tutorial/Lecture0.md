# Lecture 0

## Lecture 0 Concepts

- Introduction Projects
- Prototyping & Unit Testing in Wokwi
- Physically Wiring

## Introduction Projects

The Introduction projects should be completed before starting the OOP Mini Project. Ultimately, students should have a basic understanding of the following concepts: different sensors and actuators, wiring a breadboard, Unit Testing, and debugging software and hardware.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1px;">
  <figure style="text-align: center;">
    <img src="../introduction_projects/images/blink_led.png" alt="Blink LED" width="200"/>
    <figcaption>Blink LED</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="../introduction_projects/images/digital_sensor.png" alt="Digital Sensor" width="200"/>
    <figcaption>Digital Sensor</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="../introduction_projects/images/analog_sensor.png" alt="Analog Sensor" width="200"/>
    <figcaption>Analog Sensor</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="../introduction_projects/images/servo_control.png" alt="Servo Control" width="200"/>
    <figcaption>Servo Control</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="../introduction_projects/images/ultrasonic_sensor.png" alt="Ultrasonic Sensor" width="200"/>
    <figcaption>Ultrasonic Sensor</figcaption>
  </figure>
  <figure style="text-align: center;">
    <img src="../introduction_projects/images/I2C_module.png" alt="I2C Module" width="200"/>
    <figcaption>I2C Module</figcaption>
  </figure>
</div>

## Wokwi

Wokwi is an online Electronics simulator. You can use it to simulate Arduino, ESP32, STM32, and many other popular boards, parts and sensors. We will be using it for Pi Pico, you can also use the integrated IDE.

Students can sign up or in with OAuth using either their School Google Account or GitHub account.

1. [Wokwi](https://wokwi.com/)
2. [Wokwi Introduction Video](https://www.youtube.com/watch?v=s4QKFw8fh-4)
3. [Wokwi Pi Pico Docs](https://docs.wokwi.com/parts/wokwi-pi-pico)

> [!Note]
> Students using Wokwi should start with [Template Wokwi Project](https://wokwi.com/projects/433242006092880897).

### Wokwi Prototype

![Wokwi Prototype](/images/prototype_model.png)

### Wokwi Unit Testing

First students should copy the provided script [v02.py](..\project\py_scripts\v02.py) into the terminal. 

1. All 5 LEDs should illuminate.
2. The buzzer should emit animated musical note on screen and if volume is turned up a constant tone.
3. The momentary switch should return `1` to the IDE terminal when closed (pressed) and 0 when not closed (depressed).

## Physical Wiring

Watch the [Pi Pico Breadboard Introduction Video](https://www.youtube.com/watch?v=Ex7AJll-FsM). Students should wire their board, then unit test using the provided script [v02.py](..\project\py_scripts\v02.py). 

### Physical Prototype

![Physical Prototype](/images/prototype_model.png)

### Physical Unit Testing

1. All 5 LEDs should illuminate.
2. The buzzer should emit a constant tone.
3. The momentary switch should return `1` to the IDE terminal when closed (pressed) and 0 when not closed (depressed).
