# utils.py
import os
import json

class JsonStorage:
    def __init__(self, file="data.json"):
        self.file = file

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')