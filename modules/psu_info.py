import logging
try:
    import win32com.client
    has_pywin32 = True
except ImportError:
    has_pywin32 = False

def get_psu_info():
   
    psu_info = []
    if not has_pywin32:
        logging.error("The pywin32 library is not installed. Unable to fetch PSU details.")
        return [{"Error": "pywin32 is not installed"}]

    try:
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
        colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_SystemEnclosure")

        for objItem in colItems:
            try:
                # Retrieve basic details about the PSU
                manufacturer = objItem.Manufacturer or "Unknown"
                serial_number = objItem.SerialNumber or "Unknown"
                model = objItem.Model or "Unknown"

                psu_info.append({
                    "Manufacturer": manufacturer,
                    "Serial Number": serial_number,
                    "Model": model
                })
            except Exception as e:
                logging.error("Error while retrieving information about the power supply unit.", exc_info=True)

    except Exception as e:
        logging.error("Error while collecting information about the power supply unit.", exc_info=True)

    return psu_info
