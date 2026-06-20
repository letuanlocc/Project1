from logic.logic_utils import JsonStorage, clear
from logic.logic_saveData import handle_type
from console.mainDay import data_day

storage = JsonStorage() #khởi tạo

def input_positive_int(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if value <= 0:
            print("Value must be greater than 0.")
            continue
        return value


def manage_money(system):
    clear()
    data = storage.load()
    handle = handle_type()
    for user in data["users"]:
        if user["username"] == system.user_current:
            if user["transactions"]:
                return data_day(system)
            else:
                while True:
                    print(f"Welcome {system.user_current} to demo mange monney ")
                    print("1. Thrifty spending")
                    print("2. Comfortable spending")
                    print("3. Discipline spending")
                    print("4. Exit")
                    choose = input("Nhập lựa chọn: ")
                    if choose == "1":
                        total = input_positive_int("Total money: ")
                        day = input_positive_int("Day: ")
                        try:
                            handle.save_type("save_money", total, day, system.user_current, data)
                            storage.save(data)
                        except ValueError as exc:
                            print("Error:", exc)
                    elif choose == "2":
                        total = input_positive_int("Total money: ")
                        day = input_positive_int("Day: ")
                        try:
                            handle.comfor_type("comfortable", total, day, system.user_current, data)
                            storage.save(data)
                        except ValueError as exc:
                            print("Error:", exc)
                    elif choose == "3":
                        total = input_positive_int("Total money: ")
                        day = input_positive_int("Day: ")
                        try:
                            handle.discipline_type("discipline", total, day, system.user_current, data)
                            storage.save(data)
                        except ValueError as exc:
                            print("Error:", exc)
                    elif choose == "4":
                        return
                    else:
                        print("Invalid selection. Please choose 1-4.")
                        continue
                    choose_out = input("Do you want continue (Y/N): ")
                    if choose_out.lower() == "y":
                        return data_day(system)
                    else:
                        return