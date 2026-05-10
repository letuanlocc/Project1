import json
import os
from logic.logic_utils import JsonStorage, clear

class UserSystem:
    
    def __init__(self):
        self.user_current = None
        
    #register
    def register(self, username, password,data):
        for user in data["users"]:
            if user["username"] == username:
                print(data["users"])
                return "Username already exists"
        data["users"].append({
            "username": username,
            "password": password
        })
        return "Register success"
    
    #login
    def login(self, username, password,data):
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                self.user_current = username
                return f"Welcome {self.user_current}"
        return "Username or Password incorrect"
        