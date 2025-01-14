import logging
import platform

try:
    import win32com.client
    has_pywin32 = True
except ImportError:
    has_pywin32 = False

def get_motherboard_info():
    motherboard_info = {}
    try:
        if platform.system() == "Windows" and has_pywin32:
            objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
            objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
            colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_BaseBoard")
            for objItem in colItems:
                motherboard_info = {
                    "Manufacturer": objItem.Manufacturer,
                    "Model": objItem.Product,
                    "Serial Number": objItem.SerialNumber
                }
    except Exception as e:
        logging.error("Error retrieving motherboard information.", exc_info=True)
    return motherboard_info

def get_memory_info():
    memory_info = []
    try:
        if platform.system() == "Windows" and has_pywin32:
            objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
            objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
            colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_PhysicalMemory")
            for objItem in colItems:
                capacity = "Unknown"
                if objItem.Capacity:
                    capacity = f"{int(objItem.Capacity) / (1024 ** 3):.2f} GB"
                part_number = objItem.PartNumber.strip() if objItem.PartNumber else "Unknown"
                serial_number = objItem.SerialNumber.strip() if objItem.SerialNumber else "Unknown"
                speed = f"{objItem.Speed} MHz" if objItem.Speed else "Unknown"

                memory_info.append({
                    "Capacity": capacity,
                    "Manufacturer": objItem.Manufacturer,
                    "Part Number": part_number,
                    "Serial Number": serial_number,
                    "Speed": speed
                })
    except Exception as e:
        logging.error("Error retrieving memory information.", exc_info=True)
    return memory_info

def get_video_card_info():
    video_info = []
    try:
        if platform.system() == "Windows" and has_pywin32:
            objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
            objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
            colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_VideoController")
            for objItem in colItems:
                adapter_ram = "Unknown"
                if objItem.AdapterRAM:
                    adapter_ram = f"{int(objItem.AdapterRAM) / (1024 ** 3):.2f} GB"

                video_info.append({
                    "Name": objItem.Name,
                    "Driver Version": objItem.DriverVersion,
                    "Video Processor": objItem.VideoProcessor,
                    "Adapter RAM": adapter_ram,
                    "Serial Number": objItem.PNPDeviceID
                })
    except Exception as e:
        logging.error("Error retrieving video card information.", exc_info=True)
    return video_info
