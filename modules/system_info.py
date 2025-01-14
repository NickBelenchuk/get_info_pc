import platform
import psutil
import cpuinfo
import logging

def get_system_info():
    system_info = {}
    try:
        system_info["Operating System"] = f"{platform.system()} {platform.release()} ({platform.version()})"
        system_info["Hostname"] = platform.node()
        info = cpuinfo.get_cpu_info()
        system_info["Processor"] = info.get('brand_raw', 'Unknown')
        ram = psutil.virtual_memory()
        system_info["Total RAM"] = f"{ram.total / (1024 ** 3):.2f} GB"
        system_info["Available RAM"] = f"{ram.available / (1024 ** 3):.2f} GB"
    except Exception as e:
        logging.error("Error gathering general system information.", exc_info=True)
    return system_info
