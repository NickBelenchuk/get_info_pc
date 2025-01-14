import logging
import json

from modules.admin_utils import request_admin
from modules.system_info import get_system_info
from modules.hardware_info import (
    get_motherboard_info,
    get_memory_info,
    get_video_card_info
)
from modules.network_info import get_network_info
from modules.file_utils import save_to_file

logging.basicConfig(
    filename='error_log.txt',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    encoding='utf-8'
)

def main():
    if not request_admin():
        return

    info = {
        "System Information": get_system_info(),
        "Motherboard": get_motherboard_info(),
        "Memory": get_memory_info(),
        "Video Cards": get_video_card_info(),
        "Network": get_network_info()
    }

    print(json.dumps(info, indent=4, ensure_ascii=False))

    save_to_file(info, "system_info.json")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
