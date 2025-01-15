import logging
import json

def save_to_file(data, filename="system_info.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"System information saved to '{filename}'.")
    except Exception as e:
        logging.error("Error saving to file.", exc_info=True)
