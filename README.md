# CID-Updater GUI

This repository contains a Python script designed to provide a user-friendly interface for interacting with an MCU (Microcontroller Unit) and performing various operations on it. The script uses Telnet communication to connect to the MCU and execute commands.

## Features

The script provides the following features:

- General information retrieval from the MCU.
- Signature checking and display.
- Active partition identification.
- Rebooting the MCU.
- Updating the MCU software from a specified URL.
- Redeploying the MCU.
- Service redeployment on the MCU.
- Factory redeployment on the MCU.
- Formatting the maps SD card on the MCU.
- Checking the status of the maps SD card on the MCU.
- Resetting the CID-Updater.
- Watching the update process.
- Staging software updates.
- Retrying staged software updates.

## Prerequisites

- Python 3.x
- Required Python libraries: pandas, numpy, pyfiglet, asyncio, telnetlib3

## Usage

1. Clone this repository to your local machine.

   ```
   git clone https://github.com/strmotors/CIDUpdaterGUI
   cd CIDUpdaterGUI
   ```
   
2. Install the required Python libraries.

   ```
   pip install -r requirements.txt
   ```



3. Connect your computer to the diag port using a Fakra to ethernet cable.

4. Set your local IP to ```192.168.90.125```

5. Perform a secEth unlock using Toolbox or any other method you wish.

6. Run the script in your terminal.

   ```
   python cugui.py
   ```
   
7. Follow the on-screen menu to choose the desired operation.

## Notes
- This script assumes a Telnet connection is established with the MCU at the specified IP address and port. Ensure the MCU is reachable and correctly configured.
- The script provides an interactive menu for ease of use, allowing users to select operations from the list.

## Disclaimer
Please use this script responsibly and ensure you have appropriate permissions before interacting with any MCU or device. The provided script is for demonstration purposes and may need modifications to suit your specific use case.
