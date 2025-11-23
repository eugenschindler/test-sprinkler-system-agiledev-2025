# read_settings.py

import os
import json

class ReadSettings:
    def __init__(self):
        self.settings_file = "settings.json"
        self.settings = {
            "reservoir_size": 1000,  # in liters
        }
    
    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as file:
                self.settings = json.load(file)
            print("Settings loaded from file.")
        else:
            print("No preset settings found. Please enter new settings.")
    
    def save_settings(self):
        with open(self.settings_file, "w") as file:
            json.dump(self.settings, file, indent=4)
        print("Settings saved to file.")
    
    def display_settings(self):
        print(f"Current Settings: {self.settings}")
    
    def get_user_input(self):
        self.settings["reservoir_size"] = int(input(f"Enter reservoir size (current: {self.settings['reservoir_size']} liters): ") or self.settings["reservoir_size"])
        self.save_settings()

