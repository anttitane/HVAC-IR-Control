#!/usr/bin/env python

#============================================================================================================================
# Anttitane 27.9.2021
#
# This program sends IR commands to Mitsubishi MSZ-FD25 using 
# Raspberry Pi with IR led in pin 23.
# https://github.com/Anttitane/HVAC-IR-Control
#
# Usage "sudo python ilp_commander.py -m 'cooling/heating' -t 'temperature in deg C' -f 'fanspeed: low, med, high, auto'
# Example: sudo python ilp_commander.py -m cooling -t 21 -f high
#============================================================================================================================

import time
import datetime
import argparse
from hvac_ircontrol.ir_sender import LogLevel
from hvac_ircontrol.mitsubishi import Mitsubishi, ClimateMode, FanMode, VanneVerticalMode, VanneHorizontalMode, ISeeMode, AreaMode, PowerfulMode

# Argument parser for command line inputs
ap = argparse.ArgumentParser()
# Mode selection
ap.add_argument("-m", "--mode", required=True,
    help="input mode, choose cooling or heating")
# Temperature selection
ap.add_argument("-t", "--temperature", required=True,
    help="Input temperature in deg C (eg. 23), min 16, max 31. Choose 0 (zero) to power off.")
# Fan speed selection 
ap.add_argument("-f", "--FanSpeed", required=False, default="FanMode.Auto",
    help="Fan speed, eg. low, med, high, auto")

args = vars(ap.parse_args())

HVAC = Mitsubishi(23, LogLevel.ErrorsOnly) # (GPIO pin number, Log level)

# Print user inputs
print("---------------------------------------------")
print("Operation mode is {}".format(args["mode"]))
print("Temperature is {}".format(args["temperature"]))
print("Fan speed is {}".format(args["FanSpeed"]))
print("---------------------------------------------")

# Set fan speed mode 
if args['FanSpeed'] == "low":
   FanSpeedSelection = FanMode.Speed1
elif args['FanSpeed'] == "med":
   FanSpeedSelection = FanMode.Speed2
elif args['FanSpeed'] == "high":
   FanSpeedSelection = FanMode.Speed3
else:
   FanSpeedSelection = FanMode.Auto

# Power of if temperature is 0
if args['temperature'] == "0":
   print("Powering off...")
   HVAC.power_off()

# Cooling mode
if args['mode'] == "cooling" and args['temperature'] > "0":
    print("Sending command...")
    HVAC.send_command(
        climate_mode = ClimateMode.Cold,
        temperature = int(args['temperature']),
        fan_mode = FanSpeedSelection,
        vanne_vertical_mode = VanneVerticalMode.Top,
        vanne_horizontal_mode = VanneHorizontalMode.MiddleRight,
        isee_mode = ISeeMode.ISeeOff,
        area_mode = AreaMode.Full,
        powerful = PowerfulMode.PowerfulOff #Plasma on/off?
        )

# Heating mode
if args['mode'] == "heating" and args['temperature'] > "0":
    print("Sending command...")
    HVAC.send_command(
        climate_mode = ClimateMode.Hot,
        temperature = int(args['temperature']),
        fan_mode = FanSpeedSelection,
        vanne_vertical_mode = VanneVerticalMode.MiddleTop,
        vanne_horizontal_mode = VanneHorizontalMode.MiddleRight,
        isee_mode = ISeeMode.ISeeOff,
        area_mode = AreaMode.Full,
        powerful = PowerfulMode.PowerfulOff #Plasma on/off?
        )
