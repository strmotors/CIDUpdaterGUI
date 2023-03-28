# CIDUpdaterGUI
 Tesla CID-Updater GUI, written in Python.

## Functions

1 - General Info: General information about the vehicle. (VIN, software size and version etc.)
2 - Signature: Get the installed software signatures for all units, including maps.
3 - Active Partition: See the active partition name.
4 - Reboot MCU: (Beta) Soft-reboot the MCU.
5 - Update From URL: Update the MCU from given URL.
6 - Redeploy: Do a software redeploy.
7 - Service Redeploy: Do a service redeploy.
8 - Factory Redeploy: Do a factory redeploy.
9 - Format SD Card: (Beta) Format the maps SD card.
10 - Check SD Card: (Beta) Check the maps SD card.
11 - Reset Updater: Re-initialize the CID-Updater.
12 - Watch Update: Watch the current update status and show logs.
13 - Go Staged: (Beta) Set the software to be staged.
14 - Retry Go Staged: (Beta) Retry to stage the software.

## Installation
```
git pull https://github.com/strmotors/CIDUpdaterGUI
cd CIDUpdaterGUI
pip install -r requirements.txt
python cugui.py
```

## Usage
- Connect your computer to the diag port using a Fakra to ethernet cable.
- Set your local IP to ```192.168.90.125```
- Run the Python script and follow the in-program instructions.
