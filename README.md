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
- Soft reboot functionality 
- Soft shutdown functionality
- register the script to run on boot

## Installation

1. Wiring

&emsp; Pick a GPIO PIN (GPIO 13 for example)

&emsp; Connection: GPIO13 &mdash; power switch &mdash; GND

2. Clone the repository:
```git clone https://github.com/bblabNTU/pi_soft_reboot.git```

## Usage

1. 
```
sudo mv listen-for-shutdown.py /usr/local/bin/
sudo chmod +x /usr/local/bin/listen-for-shutdown.py
```
2. 
```
sudo mv listen-for-shutdown.sh /etc/init.d/
sudo chmod +x /etc/init.d/listen-for-shutdown.sh
```
3.
```
sudo update-rc.d listen-for-shutdown.sh defaults
```
4. 
```
sudo /etc/init.d/listen-for-shutdown.sh start
```
## Reference

1. https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
2. rather than ```init.d```, you can use [systemctl](https://segmentfault.com/a/1190000038458363)
