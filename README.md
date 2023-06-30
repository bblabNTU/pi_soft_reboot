# pi_soft_reboot

To shutdown or reboot Raspberry Pi (4 in my case) by a momentary power switch, so you don't need to unplug the cord which might damage your SD card

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Reference](#reference)

## Introduction

In any case you shouldn't unplug the cord to shutdown Pi, it could lead to data corruption and SD card malfunction.

So add a power button to safely and easily shutdown, reboot, or wake up your Raspberry Pi.

Note: When we "shutdown" the Pi, Pi gets into halt state which consumes little power, and we can only disconnect the power supply in this state.

To wake Pi up from "halt", easily short GPIO3(PIN5) and GND(PIN6). However, in my project I'm using I2C which required GPIO3, so I won't elaborate the wake up function in this repo.

## Features

- Hardware Wiring
- Soft reboot by short press the power switch 
- Soft shutdown by long press the power switch
- register the script to run on boot

## Installation

1. Wiring

&emsp; Pick a GPIO PIN (GPIO 13 for example)

&emsp; Connection: GPIO13 &mdash; power switch &mdash; GND

2. Clone the repository:
```git clone https://github.com/bblabNTU/pi_soft_reboot.git```

## Prerequirement

* If you install ubuntu on rpi:
  ```
  sudo apt-get install python3-rpi.gpio
  ```

## Usage

1. Modify listen-for-shutdown.service on Line:7 :
```
ExecStart=/usr/bin/python3 <.py location>/listen-for-shutdown.py
```
2. 
```
sudo mv listen-for-shutdown.service /lib/systemd/system/listen-for-shutdown.service
```

3.
```
sudo chmod 644 /lib/systemd/system/listen-for-shutdown.service
```
4. 
```
sudo systemctl daemon-reload
sudo systemctl enable listen-for-shutdown.service
```
5.
```
sudo reboot
```
## Reference


1. https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/#crontab
2. https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
3. [systemctl](https://segmentfault.com/a/1190000038458363)
