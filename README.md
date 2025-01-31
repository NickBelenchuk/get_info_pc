# 🚀 System Info Collector

A Windows-oriented Python project that gathers hardware and network information, then saves the data to a JSON file. It also logs errors to `error_log.txt` and can request administrator privileges on Windows when needed.

## 📋 Table of Contents
- [🌟 Features](#-features)
- [🔧 Requirements](#-requirements)
- [📥 Installation](#-installation)
- [▶️ Usage](#️-usage)
- [📂 Project Structure](#-project-structure)
- [📦 Building a Single EXE](#-building-a-single-exe)

## 🌟 Features
- Collects:
  - **System Information** (operating system, CPU, total/available RAM)
  - **Motherboard** (manufacturer, model, serial number)
  - **Disk Information** (S/N, model, size, number of partitions, media type, interface version and type)
  - **Memory** (capacity, manufacturer, part number, speed, etc.)
  - **Video Cards** (name, driver version, video processor, memory)
  - **Network** (interfaces, MAC addresses, IP addresses, adapter names, serial numbers)
  - **Power Supply Unit** (manufacturer, model, serial number)
- Logs errors to `error_log.txt`.
- Saves results to a JSON file in the `system_info_files/` directory.
- Requests administrator privileges on Windows (if necessary).

## 🔧 Requirements
- **Python 3.7+** (recommended)
- **Windows OS** (for WMI queries and `pywin32`)
- External Python libraries:
  - [psutil](https://pypi.org/project/psutil/)
  - [py-cpuinfo](https://pypi.org/project/py-cpuinfo/)
  - [pywin32](https://pypi.org/project/pywin32/) (Windows-specific)

## 📥 Installation
```bash
# 1. Clone this repository or download the source code.
git clone "repository_link"

# 2. (Optional) Create and activate a virtual environment:
python -m venv venv

# On Windows (cmd):
venv\Scripts\activate

# Or Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Or Git Bash / WSL:
source venv/Scripts/activate

# 3. Install dependencies:
pip install -r requirements.txt
```
## ▶️ Usage
1. Open a terminal or command prompt in the project root (where main.py is located).

2. Run the script: (The script attempts to obtain administrator privileges on Windows.)
```bash
python main.py
```
3. A JSON file with system details will be saved in the system_info_files directory. (The filename follows the format: Manufacturer_Model_SerialNumber.json).

4. Press Enter to exit.

## 📂 Project Structure
```bash
project_folder/
├── main.py
├── build/
│   └── main/                 # Build files
├── modules/
│   ├── __init__.py           # (can be empty)
│   ├── admin_utils.py        # Admin privilege checks and requests
│   ├── disk_info.py          # Disk information
│   ├── system_info.py        # OS, CPU, and RAM details
│   ├── hardware_info.py      # Motherboard, memory modules, video cards
│   ├── network_info.py       # Network interfaces
│   ├── psu_info.py           # Power Supply
│   └── file_utils.py         # JSON file saving
├── requirements.txt
├── README.md
└── system_info_files/        # Directory for saved JSON files
```
# 📦 Building a Single EXE
## To create a standalone .exe file for Windows using PyInstaller:

Install PyInstaller:
```bash 
pyinstaller --onefile --noconsole main.py
```

## Distributing the `.exe`:

In most cases, you only need to provide the `.exe` file.
Ensure that the target machine has standard system libraries (e.g., Microsoft Visual C++ Redistributable).
