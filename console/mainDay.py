from logic.logic_utils import *
from logic.logic_dataDay import handle_day
storage = JsonStorage()

def input_non_negative_int(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if value < 0:
            print("Value cannot be negative.")
            continue
        return value

def data_day(system):
    data = storage.load()
    handle = handle_day()
    while True:
        print("1. Add day")
        print("2. Update day")
        print("3. View all day")
        print("4. Delete day")
        print("5. Exit")
        choose = input("Nhập lựa chọn: ")
        if choose == "1":
            eat = input_non_negative_int("eat: ")
            play = input_non_negative_int("play: ")
            gas = input_non_negative_int("gas: ")
            print(handle.add_day(eat,play,gas,data,system.user_current))
            storage.save(data)
        elif choose == "2":
            day = input_non_negative_int("Input day want to update: ")
            found = any(d["day"] == day 
                        for user in data["users"] 
                        if user["username"] == system.user_current
                        for d in user["data_day"])
            if not found:
                print("Day not exits")
            else:
                eat = input_non_negative_int("eat: ")
                play = input_non_negative_int("play: ")
                gas = input_non_negative_int("gas: ")
                print(handle.update_day(eat, play, gas, day, data,system.user_current))
            storage.save(data)
        elif choose == "3":
            handle.view_day(data,system.user_current)
        elif choose == "4":
            conti = input("Do you want Delete ??????(Y/N): ")
            if conti == "y":
                day = input_non_negative_int("Input day want to delete: ")
                found = any(d["day"] == day 
                            for user in data["users"] 
                            if user["username"] == system.user_current
                            for d in user["data_day"])
                if not found:
                    print("Day not exists")
                else:
                    print(handle.delete_day(day,data,system.user_current))
                    storage.save(data)
        else:
            return
        choose_out = input("Do you want continue(Y/N): ")
        if choose_out == "y":
            continue
        else:
            return
        
def format_money(money):
    return f"{money:,.0f}".replace(",", ".") + " VND"
