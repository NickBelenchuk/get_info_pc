# 🚀 System Info Collector

A Windows-oriented Python project that gathers hardware and network information, then saves the data to a JSON file. It also logs errors to `error_log.txt` and can request administrator privileges on Windows when needed.

## 📋 Table of Contents
- [🌟 Features](#-features)
- [🔧 Requirements](#-requirements)
- [📥 Installation](#-installation)
- [▶️ Usage](#️-usage)
- [📂 Project Structure](#-project-structure)
- [📦 Building a Single EXE](#-building-a-single-exe)
- [📜 License](#-license)
- [👤 Author](#-author)

## 🌟 Features
- Collects:
  - **System Information** (operating system, CPU, total/available RAM)
  - **Motherboard** (manufacturer, model, serial number)
  - **Memory** (capacity, manufacturer, part number, speed, etc.)
  - **Video Cards** (name, driver version, video processor, memory)
  - **Network** (interfaces, MAC addresses, IP addresses)
- Logs errors to `error_log.txt`.
- Saves results to `system_info.json`.
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
 Run the script: ```python main.py```

2. The script attempts to obtain administrator privileges on Windows.
3. After it finishes, you will see JSON data in the console and the file `system_info.json` created in the current directory.
4. Press **Enter** to exit.

## 📂 Project Structure
```bash
project_folder/
├── main.py
├── dist/
│   └── main.exe              # The built executable (created after PyInstaller packaging)
├── modules/
│   ├── __init__.py           # (can be empty)
│   ├── admin_utils.py        # Admin privilege checks and requests
│   ├── system_info.py        # OS, CPU, and RAM details
│   ├── hardware_info.py      # Motherboard, memory modules, video cards
│   ├── network_info.py       # Network interfaces
│   └── file_utils.py         # JSON file saving
├── requirements.txt
└── README.md
```
## 📦 Building a Single EXE

## To create a standalone .exe file for Windows using PyInstaller:
1. Install PyInstaller:
```bash
pip install pyinstaller
```
2. Build a one-file executable:
```bash
pyinstaller --onefile main.py
```
* The resulting executable will be placed in the `dist/` folder (e.g., dist/main.exe).

3. To run without a console window, add --noconsole:
```bash
pyinstaller --onefile --noconsole main.py
```
## Distributing the ```.exe```:
* In most cases, you only need to provide the ```.exe``` file.
* Ensure that the target machine has standard system libraries (e.g., Microsoft Visual C++ Redistributable).
