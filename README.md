# Port Scanner by VL_PLAY Games

- [Read in Russian](README.ru.md) 
- [Read in Japanese](README.ja.md)

## Overview
The **Port Scanner** application is a versatile tool designed to analyze and interact with networks. It provides features for checking IP addresses, scanning ports, pinging servers, viewing logs, and accessing terminal commands. The intuitive graphical interface supports multiple functions to cater to developers, network administrators, and tech enthusiasts.

## Features

### 🔍 Main Functions
1. **IP Check** - Display all computer IP addresses
2. **Port Scan** - Scan and show all open ports
3. **All Info** - Complete network overview:
   - IP addresses
   - Open ports
   - Network drivers
   - Additional network data
4. **Custom IP** - Scan ports on specific IP address
5. **Ping** - Check connectivity and latency
6. **Terminal** - Built-in command line interface
7. **Active Devices** - List devices in local network

### ⚙️ Additional Features
- **Help** - Usage instructions and guidance
- **Log** - Program activity history
- **Clear** - Clear results and logs
- **Settings** - Application configuration
- **About** - Version info and credits

## Interface
The interface is divided into two primary sections:
- **Select Option**: Features buttons for each main function.
- **Result Panel**: Displays the results and outputs of the selected operation.

## How to Use
1. Select a function from the main menu by clicking the corresponding button.
2. View the results or logs in the "Result" panel.
3. Use the additional buttons at the bottom to manage logs, clear results, or access the help menu.

## Supported Languages
- **English**
- **Russian**

## Installation
### For Windows
1. Go to the **Releases** section.
2. Download `port_scanner_windows.zip`.
3. Extract the contents and run `port_scanner.exe`.

### For Linux
1. Go to the **Releases** section.
2. Download `port_scanner_linux.zip`.
3. Extract the contents and execute in the terminal:
   ```bash
   ./port_scanner
   ```

---

Feel free to contribute or report any issues!

---

## If windows complains about viruses
I use Pyinstaller to create an .exe file and since Pyinstaller creates a self-extracting archive, Windows (and Virus Total) shows it as a virus
You can look at the source code of the program and make sure that there are no viruses
[https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg](url)