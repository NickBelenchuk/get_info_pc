import logging
import psutil
import socket

def get_network_info():
    network_info = []
    try:
        for interface, addrs in psutil.net_if_addrs().items():
            iface_info = {
                "Interface": interface,
                "MAC Address": None,
                "IP Address": None
            }
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    iface_info["MAC Address"] = addr.address
                elif addr.family == socket.AF_INET:
                    iface_info["IP Address"] = addr.address
            network_info.append(iface_info)
    except Exception as e:
        logging.error("Error retrieving network information.", exc_info=True)
    return network_info
