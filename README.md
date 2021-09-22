# HVAC IR Control


## Introduction
HVAC IR Control aims to facilitate control of your Mitsubishi MSZ (ILP or ilmalämpöpumppu in Finnish) HVAC emulating the IR code using a Raspberry Pi. 

## Project background
This repository is a fork from Ericmas001. 
I have developed a simple solution for sending commands to Mitsubishi MSZ using Raspberry Pi. By executing a command line command you can sen heat/cool/power off command with temperature and fan speed settings to the Mitsubishi. You can automate these functions by using eg. Home Assistant and MQTT.

# Overview of features

## Mitsubishi Inverter HVAC

There are two functions that you may use to control HVAC from mitsubishi. 
The function to send configuration is:

```
void sendHvacMitsubishi(
 HvacMode                  HVAC_Mode,           // Example HVAC_HOT  HvacMitsubishiMode
 int                       HVAC_Temp,           // Example 21  (°c)
 HvacFanMode               HVAC_FanMode,        // Example FAN_SPEED_AUTO  HvacMitsubishiFanMode
 HvacVanneMode             HVAC_VanneMode,      // Example VANNE_AUTO_MOVE  HvacMitsubishiVanneMode
 int                       OFF                  // Example false (Request Turn On = False)
);
```
new function with enhanced function:
```
void sendHvacMitsubishiFD(
 HvacMode                  HVAC_Mode,           // Example HVAC_HOT  HvacMitsubishiMode
 int                       HVAC_Temp,           // Example 21  (°c)
 HvacFanMode               HVAC_FanMode,        // Example FAN_SPEED_AUTO  HvacMitsubishiFanMode
 HvacVanneMode             HVAC_VanneMode,      // Example VANNE_AUTO_MOVE  HvacMitsubishiVanneMode
 HvacAreaMode              HVAC_AreaMode,       // Example AREA_AUTO
 HvacWideVanneMode         HVAC_WideMode,       // Example WIDE_MIDDLE
 int                       HVAC_PLASMA,          // Example true to Turn ON PLASMA Function
 int                       HVAC_CLEAN_MODE,      // Example false 
 int                       HVAC_ISEE,            // Example False
 int                       OFF                   // Example false to Turn ON HVAC / true to request to turn off
 );
```

Functions confirmed in MSZ-GE and MFZ modules from Mitsubishi.

## ilp_control.py usage (to be added when ready)
Usage: "sudo python ilp_commander.py -m 'cooling/heating' -t 'temperature' -f 'fanspeed'
       To power of set temperature to 0
       
Example: sudo python ilp_commander.py -m cooling -t 21 -f Speed2
