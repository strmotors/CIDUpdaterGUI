import pandas as pd
import numpy as np
import pyfiglet
import asyncio, telnetlib3, time
import warnings

# Suppress DeprecationWarning messages
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# Display a banner
ascii_banner = pyfiglet.figlet_format("CID-Updater GUI")
print(ascii_banner)
print("By ST-R Motors")
print()

# Create an empty 'status' file
open('status', 'w').close()

# Initialize variable for manual update URL
manualUpdateURL = ''


# Function for Telnet-based operations
async def rebootShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('reboot\n')
        text_file = open("logs/reboot.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
# Reboot the MCU
def rebootMCU():
    print()
    print("The MCU is going to reboot itself.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=rebootShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)
    

async def urlUpdateShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('install ' + manualUpdateURL + '\n')
        print(outp, flush=True)
        text_file = open("logs/install.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
# Update MCU from a URL
def updateFromURL():
    print()
    print("Update the MCU from given URL.")
    print()
    manualUpdateURL = input('URL to grab update from: ')
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=urlUpdateShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)

# Software Redeploy
async def redeployShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('redeploy\n')
        print(outp, flush=True)
        text_file = open("logs/redeploy.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def redeploy():
    print()
    print("MCU will do a redeploy.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=redeployShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)


# Service Redeploy
async def sRedeployShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('service-redeploy\n')
        print(outp, flush=True)
        text_file = open("logs/service-redeploy.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def sRedeploy():
    print()
    print("MCU will do a service redeploy.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=sRedeployShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)


# Factory Redeploy
async def fRedeployShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('factory-redeploy\n')
        print(outp, flush=True)
        text_file = open("logs/factory-redeploy.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def fRedeploy():
    print()
    print("MCU will do a factory redeploy.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=fRedeployShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)


# Format the SD Card
async def formatSDShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('format-sd-card\n')
        print(outp, flush=True)
        text_file = open("logs/format-sd-card.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def formatSD():
    print()
    print("MCU will format the maps SD card.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=formatSDShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)



# Check the SD Card
async def checkSDShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('check-sd-card\n')
        print(outp, flush=True)
        text_file = open("logs/check-sd-card.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def checkSD():
    print()
    print("Maps SD card will be checked.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=checkSDShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)


# Reset the Updater
async def resetShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('reset\n')
        print(outp, flush=True)
        text_file = open("logs/reset.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def reset():
    print()
    print("The CID-Updater will be restarted.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=resetShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)



# Watch the Update
async def watchShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('watch\n')
        print(outp, flush=True)
        text_file = open("logs/watch.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def watch():
    print()
    print("Watching the update:")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=watchShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)



# Go Staged
async def goStagedShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('gostaged\n')
        print(outp, flush=True)
        text_file = open("logs/gostaged.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def goStaged():
    print()
    print("Software update will be staged.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=goStagedShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)



# Retry Go Staged
async def retryGoStagedShell(reader, writer):
    while True:
        outp = await reader.read(1024)
        writer.write('retry-gostaged\n')
        print(outp, flush=True)
        text_file = open("logs/retry-gostaged.txt", "a")
        n = text_file.write(outp)
        text_file.close()
        time.sleep(5)
        break
    
def retryGoStaged():
    print()
    print("Trying to stage the software update, again.")
    print()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=retryGoStagedShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)



# SYNC Status
async def statusShell(reader, writer):
    while True:
        isBreak = False
        outp = await reader.read(1024)
        if 'Welcome' in outp:
            writer.write('status\n')
        chunks=outp.split('\n')
        text_file = open("status", "a")
        n = text_file.write(outp)
        text_file.close()
        for line in chunks:
            if 'END STATUS' in line:
                isBreak = True
        if isBreak:
            break
    

# Display General Information
def infoCheck():   
    open('status', 'w').close()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=statusShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)
    
    with open('status') as file:
        datas = [line.rstrip() for line in file]
    
    print()
    print('General Information:')
    print()
    for data in datas:
        if 'Welcome' in data:
            infoSplit = data.split(' ')
            print('Vehicle: ' + infoSplit[2] + ' ' + infoSplit[3])
            print('Software Version: ' + infoSplit[10])
            print()
        if 'Online boot bank' in data:
            actPartString = ''
            infoSplit = data.split(':    ')
            actData = infoSplit[1]
            if actData == 'KERNEL_A':
                actPartString = ' (/dev/mmcblk0p1)'
            elif actData == 'KERNEL_B':
                actPartString = ' (/dev/mmcblk0p2)'
            print('Online Boot Bank: ' + actData + actPartString)
        if 'Online map bank' in data: 
            infoSplit = data.split(': ')
            actData = infoSplit[1]
            print('Online Map Bank: ' + actData)
        if 'Board Revision:' in data:
            infoSplit = data.split(':  ')
            print('MCU Board Revision: ' + infoSplit[1])
            print()
        if 'Online dot-' in data: 
            infoSplit = data.split(':  ')
            actData = infoSplit[1]
            actDataGB = int(actData)/1073741824
            print('Online Software Size: ' + actData + ' Bytes (' + str(round(actDataGB,2)) + 'GB)')
        if 'Online map package size' in data: 
            infoSplit = data.split(': ')
            actData = infoSplit[1]
            actDataGB = int(actData)/1073741824
            print('Online Map Package Size: ' + actData + ' Bytes (' + str(round(actDataGB,2)) + 'GB)')
            print()
        if 'vin =' in data:
            infoSplit = data.split(' = ')
            actData = infoSplit[1]
            print('VIN Number: ' + actData)
            print()
        if 'staged_update' in data:
            infoSplit = data.split(' = ')
            actData = infoSplit[1]
            print('Is Staged Update?: ' + actData.capitalize())
        if 'gateway_needs_update' in data:
            infoSplit = data.split(' = ')
            actData = infoSplit[1]
            print('Gateway Needs Update?: ' + actData.capitalize())
    print()


# Check Signatures
def sigCheck():
    open('status', 'w').close()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=statusShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)
    
    with open('status') as file:
        datas = [line.rstrip() for line in file]
    
    print()
    print('Signatures:')
    print()
    signatures = []
    mapSignatures = []
    sigDesc = []
    sigCon = []

    for data in datas:
        if 'signature = ' in data:
            signatures.append(data)
        elif 'signature: ' in data:
            mapSignatures.append(data)

    for signature in mapSignatures:
        signatureCouple = signature.split('signature: ')
        sigDesc.append(signatureCouple[0])
        sigCon.append(signatureCouple[1])
        
    for signature in signatures:
        signatureCouple = signature.split('signature = ')
        sigDesc.append(signatureCouple[0])
        sigCon.append(signatureCouple[1])
    
    sigDesc = [s.replace('_',' ').capitalize() for s in sigDesc]
        
    zipData = zip(sigDesc,sigCon)
    sigData = list(zipData)

    sigTable = pd.DataFrame(sigData, columns=['Name', 'Signature'])
    
    print(sigTable.to_string(index=False))
    
    willBeSaved = input("Save as signatures.txt? (y/n): ")
    if willBeSaved == 'y':
        text_file = open("signatures.txt", "w")
        n = text_file.write(sigTable.to_string(index=False))
        text_file.close()
    print()


# Check the Active Partition
def actPartCheck():
    open('status', 'w').close()
    loop = asyncio.get_event_loop()
    coro = telnetlib3.open_connection('192.168.90.100', 25956, shell=statusShell)
    reader, writer = loop.run_until_complete(coro)
    loop.run_until_complete(writer.protocol.waiter_closed)
    
    with open('status') as file:
        datas = [line.rstrip() for line in file]
    
    print()
    for data in datas:
        if 'bootdata Contents: ' in data:
            dataCouple = data.split(': ')
            apHex = dataCouple[1]
            apHexBase = apHex.split(' ')
            indicator = apHexBase[4]
            activePartition = indicator[3]
            print("Active Partition: /dev/mmcblk0p" + activePartition)
    print()
    

# Main menu function
def mainMenu():
    while True:
        print("1 - General Info")
        print("2 - Signature")
        print("3 - Active Partition")
        print("4 - Reboot MCU")
        print("5 - Update From URL")
        print("6 - Redeploy")
        print("7 - Service Redeploy")
        print("8 - Factory Redeploy")
        print("9 - Format SD Card")
        print("10 - Check SD Card")
        print("11 - Reset Updater")
        print("12 - Watch Update")
        print("13 - Go Staged")
        print("14 - Retry Go Staged")
        print("0 - Exit")
        selectionString = input("Select a number: ")
        try:
            selection = int(selectionString)
            if selection == 1:
                infoCheck()
            elif selection == 2:
                sigCheck()
            elif selection == 3:
                actPartCheck()
            elif selection == 4:
                rebootMCU()
            elif selection == 5:
                updateFromURL()
            elif selection == 6:
                redeploy()
            elif selection == 7:
                sRedeploy()
            elif selection == 8:
                fRedeploy()
            elif selection == 9:
                formatSD()
            elif selection == 10:
                checkSD()
            elif selection == 11:
                reset()
            elif selection == 12:
                watch()
            elif selection == 13:
                goStaged()
            elif selection == 14:
                readyGoStaged()
            elif selection == 0:
                exit()
            else:
                print()
                print("Invalid operation. Please enter a number between 0-14")
                print()
        except ValueError:
            print("Invalid operation. Please enter a number between 0-14")
          
# Start the main menu loop  
mainMenu()
