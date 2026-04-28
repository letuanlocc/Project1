from user import UserSystem
from data import data_money
import os
import json
def user():
    system = UserSystem() 
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choose = input("Nhập lựa chọn: ") 
        if choose == "1":
            name = input("Nhập Username: ")
            password = input("Nhập Password: ")
            print(system.register(name, password))
        elif choose == "2":
            name = input("Nhập Username: ")
            password = input("Nhập Password: ")
            print(system.login(name, password))
        else:
            return
        if system.user_current is None:
            print("Chưa đăng nhập")
        else:
            print("Đã Đăng nhập")
            print("-----------------------------------------------------")
            return manage_money(system)
        choose_out = input("Do you want continue(Y/N): ")
        if choose_out == "y":
            continue
        else:
            return
def load_data():
    with open('data.json', "r") as f:
        return json.load(f)
def save_data(data):
    with open('data.json', "w") as f:
        json.dump(data, f, indent=4)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def manage_money(system):
    clear()
    data = load_data()
    datas = data_money()
    for user in data["users"]:
        if user["username"] == system.user_current:
            user.setdefault("transactions", [])
            if user["transactions"]:
                return datas.handle_type_money(system.user_current,data)
            else:
                while True:
                    print(f"Welcome {system.user_current} to demo mange monney ")
                    print("1. Save money")
                    print("2. Comfortable")
                    print("3. Exit")
                    choose = input("Nhập lựa chọn: ")
                    data = load_data()
                    datas = data_money()
                    if choose == "1":
                            for user in data["users"]:
                                if user["username"] == system.user_current:
                                    if "transactions" not in user:
                                        user["transactions"] = []
                                    total = int(input("Total money: "))
                                    day = int(input("Day: "))
                                    user["transactions"].append({
                                            "type": "Save Money",
                                            "total" : total,
                                            "day": day
                                        })
                                    datas.handle_type_money(system.user_current,data)
                                    break
                            save_data(data)
                    elif choose == "2":
                        for user in data["users"]:
                            if user["username"] == system.user_current:
                                if "transactions" not in user:
                                    user["transactions"] = []
                                user["transactions"].append({
                                    "type": "comfortable"
                                })
                        save_data(data)
                    else:
                        return
                    choose_out = input("Do you want continue(Y/N): ")
                    if choose_out == "y":
                        continue
                    else:
                        return
user()