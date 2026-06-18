# utils.py
import os
import json

class JsonStorage:
    def __init__(self, file="data.json"):
        self.file = file

    def load(self):
        if not os.path.exists(self.file):
            default_data = {"users": []}
            self.save(default_data)
            return default_data

        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            default_data = {"users": []}
            self.save(default_data)
            return default_data

    def save(self, data):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')