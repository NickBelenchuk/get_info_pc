import logging
import json
import os

def save_to_file(data, directory="system_info_files"):
    try:
        motherboard_info = data.get("Motherboard", {})
        manufacturer = motherboard_info.get("Manufacturer", "Unknown").replace(" ", "_")
        model = motherboard_info.get("Model", "Unknown").replace(" ", "_")
        serial_number = motherboard_info.get("Serial Number", "Unknown").replace(" ", "_")

        filename = f"{manufacturer}_{model}_{serial_number}.json"
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
        print(f"System information saved to '{file_path}'.")

    except Exception as e:
        logging.error("Error saving to file.", exc_info=True)
