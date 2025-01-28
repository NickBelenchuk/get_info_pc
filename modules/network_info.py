import logging
import json
import psutil
import socket

try:
    import win32com.client
    has_pywin32 = True
except ImportError:
    has_pywin32 = False

def get_network_info():
    
    network_info = []
    wmi_network_info = []  

    try:
        for interface, addrs in psutil.net_if_addrs().items():
            iface_info = {
                "Interface": interface,
                "MAC Address": None,
                "IP Address": None,
                "Adapter Name": "Unknown",
                "Serial Number": "Unknown"
            }
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    iface_info["MAC Address"] = addr.address.lower()
                elif addr.family == socket.AF_INET:
                    iface_info["IP Address"] = addr.address
            network_info.append(iface_info)
        
        if has_pywin32:
            objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
            objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
            colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_NetworkAdapter WHERE AdapterTypeID=0")

            for objItem in colItems:
                adapter_name = objItem.Name or "Unknown"
                mac_address = objItem.MACAddress.lower() if objItem.MACAddress else "Unknown"
                serial_number = objItem.PNPDeviceID or "Unknown"

                wmi_network_info.append({
                    "Adapter Name": adapter_name,
                    "MAC Address": mac_address,
                    "Serial Number": serial_number
                })


            for iface in network_info:
                for wmi_adapter in wmi_network_info:
                    if iface["MAC Address"] and wmi_adapter["MAC Address"] and iface["MAC Address"] == wmi_adapter["MAC Address"]:
                        iface["Adapter Name"] = wmi_adapter["Adapter Name"]
                        iface["Serial Number"] = wmi_adapter["Serial Number"]

    except Exception as e:
        logging.error("Error retrieving network information.", exc_info=True)

    return {
        "Network Interfaces (psutil)": network_info,
        "Network Adapters (WMI)": wmi_network_info
    }

if __name__ == "__main__":
    data = get_network_info()
    print(json.dumps(data, indent=4, ensure_ascii=False))
