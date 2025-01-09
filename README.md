# Port Scanner by VL_PLAY Games v1.0

## Overview
The **Port Scanner** application is a versatile tool designed to analyze and interact with networks. It provides features for checking IP addresses, scanning ports, pinging servers, viewing logs, and accessing terminal commands. The intuitive graphical interface supports multiple functions to cater to developers, network administrators, and tech enthusiasts.

## Features

### Main Functions
1. **Check your IP**
   - Displays all IP addresses of the computer.

2. **Check all ports**
   - Scans and displays all open ports for the computer.

3. **All info**
   - Provides detailed information about:
     - IP addresses
     - Open ports
     - Network drivers
     - Additional network data

4. **Custom IP and Ports**
   - Allows scanning for open ports on a specific IP address provided by the user.

5. **Ping**
   - Pings a website, IP, or server to check connectivity and latency.

6. **Terminal**
   - Custom terminal functionality similar to the basic terminal in Windows or Linux.

7. **Active Devices**
   - Lists active devices in the local network.

### Additional Features
- **Help**
  - Displays detailed descriptions and guidance for using the app.

- **Log**
  - Shows a history of program activity and logs.

- **Clear**
  - Clears the current results or log entries.

- **Settings**
  - Adjust application configurations.

- **About**
  - Displays version information and credits.

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

## Credits
Developed by **VL_PLAY Games**

---

Feel free to contribute or report any issues!

---

## If windows complains about viruses
I use Pyinstaller to create an .exe file and since Pyinstaller creates a self-extracting archive, Windows (and Virus Total) shows it as a virus
You can look at the source code of the program and make sure that there are no viruses
[https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg](url)