import logging
try:
    import win32com.client
    has_pywin32 = True
except ImportError:
    has_pywin32 = False

def get_physical_disk_info():
    if not has_pywin32:
        logging.error("The pywin32 library is not installed. Unable to fetch disk details.")
        return [{"Error": "pywin32 is not installed"}]

    disk_info = []
    try:
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(".", "root\\cimv2")
        colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_DiskDrive")

        for objItem in colItems:
            try:
                # Determine disk type (HDD or SSD)
                media_type = "Unknown"
                if objItem.MediaType:
                    if "SSD" in objItem.MediaType.upper():
                        media_type = "SSD"
                    elif "HDD" in objItem.MediaType.upper():
                        media_type = "HDD"
                    else:
                        media_type = objItem.MediaType

                # Determine interface type and version
                interface_type = objItem.InterfaceType or "Unknown"
                sata_version = "Unknown"
                if "SATA" in interface_type.upper():
                    # SATA version detection based on disk speed
                    max_transfer_rate = int(objItem.Capabilities[0]) if objItem.Capabilities else 0
                    if max_transfer_rate >= 600:
                        sata_version = "SATA 3.0 (6 Gbps)"
                    elif max_transfer_rate >= 300:
                        sata_version = "SATA 2.0 (3 Gbps)"
                    else:
                        sata_version = "SATA 1.0 (1.5 Gbps)"

                disk_info.append({
                    "Model": objItem.Model or "Unknown",
                    "Serial Number": objItem.SerialNumber.strip() if objItem.SerialNumber else "Unknown",
                    "Media Type": media_type,
                    "Interface Type": interface_type,
                    "Interface Version": sata_version,
                    "Size (GB)": f"{int(objItem.Size) / (1024 ** 3):.2f} GB" if objItem.Size else "Unknown",
                    "Partitions": objItem.Partitions or "Unknown",
                })
            except Exception as e:
                logging.error(f"Error retrieving information for a disk: {e}", exc_info=True)
    except Exception as e:
        logging.error("Error while collecting physical disk information.", exc_info=True)

    return disk_info
