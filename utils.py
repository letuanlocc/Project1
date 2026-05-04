import os
import json
def load_data():
    with open('data.json', "r") as f:
        return json.load(f)
def save_data(data):
    with open('data.json', "w") as f:
        json.dump(data, f, indent=4)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')