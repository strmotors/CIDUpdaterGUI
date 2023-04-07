# CIDUpdaterGUI
 Tesla CID-Updater GUI, written in Python.

## Functions

- **General Info:** General information about the vehicle. (VIN, software size and version etc.)
- **Signature:** Get the installed software signatures for all units, including maps.
- **Active Partition:** See the active partition name.
- **Reboot MCU:** (Beta) Soft-reboot the MCU.
- **Update From URL:** Update the MCU from given URL.
- **Redeploy:** Do a software redeploy.
- **Service Redeploy:** Do a service redeploy.
- **Factory Redeploy:** Do a factory redeploy.
- **Format SD Card:** (Beta) Format the maps SD card.
- **Check SD Card:** (Beta) Check the maps SD card.
- **Reset Updater:** Re-initialize the CID-Updater.
- **Watch Update:** Watch the current update status and show logs.
- **Go Staged:** (Beta) Set the software to be staged.
- **Retry Go Staged:** (Beta) Retry to stage the software.

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
- Perform a seceth unlock using Toolbox or any other method you wish.
- Run the Python script and follow the in-program instructions.
