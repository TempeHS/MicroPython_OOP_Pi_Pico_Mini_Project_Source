# Learn MicroPython Raspberry Pi Pico

This repository is a template for mechatronics development using Pi Pico. The repository is pre-configured for VSCode and has a Pi Pico project rep-configured, including servo library/examples and libraries for PiicoDev sensors. A folder of MicroPython firmware, including brick recovery firmware, is provided for easy access. A folder of basic PiicoDev sensor examples is provided with links to more examples. The `main.py` has been preconfigured to be beginner friendly including debugging hints.

## Setup your Pi Pico and VSCode for development

### How to Sideload Firmware to Hardware

1. Disconnect Pi Pico
2. Hold <kbd>Bootsel</kbd> button
3. Connect Pi Pico to USB
4. Sideload the [correct firmware](_Firmware) to the RP1-RP2 drive that appears
5. <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> or <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
6. Select **MicroPico: Connect**

> [!Note]
> Bootloaders for all MicroPython compatible controllers source here: [https://micropython.org/download/](https://micropython.org/download/)

### Upload your project

The Project folder is already configured and setup with the following features:

1. All PiicoDev libraries are pre-installed
2. A custom Servo library is pre-installed
3. You can add other libraries to the [project/lib](project/lib) folder
4. You can create Python Scripts in the [project/py_script](project/py_script) folder and change the import parameter in [project/main.py](project/main.py) to run your script.
5. Blink is loaded by default and several example versions of servo control have been added.
6. V02-V05 demonstrates different ways to use the servo library, including different approaches to state engines and servo smoothing.
7. Change the `file_name` variable in main.py to select which file in py_scripts you want to run.

#### Steps to upload and run
1. Right click the EXPLORER window and choose _upload project to pico_ or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> or <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and select **MicroPico: Upload Project to Pico**.
2. If leaving Pico Pi connected to USB, you will need to manually run the `main.py` by right-clicking the `main.py` file in the EXPLORER window and choosing _Run current file on pico_.

> [!Important]
>
> ## Reserved Pins
>  |Pin|Use|Reason|
> |---|---|---|
> |GP0|TX|Used by Pi Pico for Serial communication and is often noisy|
> |GP1|RX|Used by Pi Pico for Serial communication and is often noisy|
> |GP4|Pull down input|Configured in `main.py` as a stop loop, ground the pin to stop the while True: loop|
> |GP11|I2C SDA|Used by PiicoDev for I2C communication|
> |GP12|I2C SCL|Used by PiicoDev for I2C communication|

## PiicoDev Components Available at Tempe High School

- [P1 Precision Temperature Sensor](https://github.com/CoreElectronics/CE-PiicoDev-TMP117-MicroPython-Module) - [example code](/examples/P1.py)
- [P2 Atmospheric Sensor](https://github.com/CoreElectronics/CE-PiicoDev-BME280-MicroPython-Module)- [example code](/examples/P2.py)
- [P10 Colour sensor](https://github.com/CoreElectronics/CE-PiicoDev-VEML6040-MicroPython-Module)
- [P13 RGB LED](https://github.com/CoreElectronics/CE-PiicoDev-RGB-LED-MicroPython-Module) - [Example Code](/examples/P13.py)
- [P14 OLED](https://github.com/CoreElectronics/CE-PiicoDev-SSD1306-MicroPython-Module) - [Example Code](/examples/P14.py)
- [P26 3-Axis Accelerometer](https://github.com/CoreElectronics/CE-PiicoDev-Accelerometer-LIS3DH-MicroPython-Module) - [example code](/examples/P26.py)
- [P30 Ultrasonic Ranger](https://github.com/CoreElectronics/CE-PiicoDev-Ultrasonic-Rangefinder-MicroPython-Module) - [example code](/examples/P30.py)

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/TempeHS_PI_Pico_Boilerplate">TempeHS Pi Pico Boilerplate
</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/benpaddlejones">Ben Jones</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
