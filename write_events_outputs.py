# write_events_outputs.py

import json

class WriteEventsOutputs:
    def __init__(self):
        self.log_file = "system_log.json"
    
    def log_event(self, settings, sensor_data, actions):
        log_entry = {
            "settings": settings,
            "sensor_data": sensor_data,
            "actions": actions
        }
        with open(self.log_file, "a") as file:
            json.dump(log_entry, file)
            file.write("\n")
        print("Event logged.")
