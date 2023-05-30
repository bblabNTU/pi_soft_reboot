# pi_soft_reboot

To shutdown or reboot Raspberry Pi (4 in my case) by a momentary power switch, so you won't damage your SD card when unplugging the power supply

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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

1. Clone the repository:
```git clone https://github.com/bblabNTU/pi_soft_reboot.git```

