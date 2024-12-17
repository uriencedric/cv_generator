from datetime import datetime
import json


def get_current_date_time_yyyymmddhis():
    # Get current date and time
    now = datetime.now()

    # Format date and time as YYYYMMDDHHMMSS
    return now.strftime("%Y%m%d%H%M%S")

def import_jsonfile(file_path):
    # Open the file and load the data into a dictionary
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data