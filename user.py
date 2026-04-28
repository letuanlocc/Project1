import json
import os
class UserSystem:
    def __init__(self, file="data.json"):
        self.file = file
        self.user_current = None
    def load_users(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
        except:
            data = {"users": []}
        return data
    def save_users(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
    #register
    def register(self, username, password):
        data = self.load_users()
        for user in data["users"]:
            if user["username"] == username:
                print(data["users"])
                return "Username already exists"
        data["users"].append({
            "username": username,
            "password": password
        })
        self.save_users(data)
        return "Register success"
    #login
    def login(self, username, password):
        data = self.load_users()
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                self.user_current = username
                return f"Welcome {self.user_current}"
        return "Username or Password incorrect"