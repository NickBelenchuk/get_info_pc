import logging
import ctypes
import os
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error("Error checking administrative privileges.", exc_info=True)
        return False

def request_admin():
    if "--elevated" in sys.argv:
        logging.info("The script is already running with administrative privileges.")
        return True

    if not is_admin():
        try:
            logging.info("Attempting to relaunch the program with administrative privileges.")
            args = sys.argv + ["--elevated"]
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(args), None, 1)
            os._exit(0)
        except Exception as e:
            logging.error("Failed to obtain administrative rights.", exc_info=True)
            print("Failed to obtain administrative rights.")
            os._exit(1)
    return False
