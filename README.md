# HVAC IR Control


## Introduction
HVAC IR Control aims to facilitate control of your Mitsubishi MSZ or MFZ (ILP or ilmalämpöpumppu in Finnish) HVAC emulating the IR code using a Raspberry Pi. 

## Project background
This repository is a fork from Ericmas001. 
I have developed a simple solution for sending commands to Mitsubishi MSZ using Raspberry Pi. By executing a command line command you can send heat/cool/power off command with temperature and fan speed settings to the Mitsubishi. You can automate these functions by using eg. Home Assistant and MQTT.

## Hardware
Examples for building a Raspberry Pi IR sender can be found from here:
https://www.raspberry-pi-geek.com/Archive/2015/10/Raspberry-Pi-IR-remote

## ilp_control.py usage
Usage: sudo python ilp_commander.py -m 'cooling/heating' -t 'temperature in deg C' -f 'fanspeed: low, med, high, auto'
       
       To power of set temperature to 0
       
Example: sudo python ilp_commander.py -m cooling -t 21 -f high
