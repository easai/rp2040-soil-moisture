# RP2040-Zero Soil Moisture Program

This repository documents a MicroPython workflow for the RP2040-Zero board.  
It is intended for soil moisture monitoring projects and demonstrates how to calibrate sensors, store thresholds, and run programs autonomously after reset.

## Overview

The RP2040-Zero is a compact microcontroller board based on the Raspberry Pi RP2040 chip.  
By flashing MicroPython firmware, the board can execute Python scripts directly.  
This project focuses on soil moisture sensing and persistent program execution.

## Features

- Reads soil moisture sensor values through the analog-to-digital converter
- Provides calibration logic for dry and wet soil conditions
- Stores threshold values for autonomous operation
- Runs automatically when saved as `main.py` on the device
- Supports interactive REPL testing for debugging

## Requirements

- RP2040-Zero board
- Capacitive soil moisture sensor
- MicroPython firmware for RP2040
- Thonny IDE or mpremote for file upload

## Installation

1. Flash MicroPython firmware onto the RP2040-Zero  
   Hold BOOTSEL while plugging in the board  
   Copy the MicroPython UF2 file to the USB drive  
   The board will reboot into MicroPython

2. Connect the board to your computer

3. Open Thonny IDE  
   Go to Tools → Options → Interpreter  
   Select MicroPython (Raspberry Pi Pico/RP2040)  
   Choose the correct port

4. Save the program to the board  
   File → Save As…  
   Select MicroPython device  
   Name the file `main.py`

5. Reset the board. The program will run automatically.

## Usage

- Connect the soil moisture sensor to the RP2040-Zero
- Adjust calibration values in the program if needed
- Monitor sensor readings via REPL or by storing thresholds
- The board will run autonomously after reset

## Notes

- Mu Editor can be used for REPL testing but does not support saving files to RP2040-Zero
- Thonny or mpremote is recommended for uploading files
- Ensure the program is named `main.py` for automatic execution
- Use REPL for debugging and calibration before final deployment

## License

This project is released under the MIT License.
