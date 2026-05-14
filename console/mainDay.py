from logic.logic_utils import *
from logic.logic_dataDay import handle_day
storage = JsonStorage()

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
            for user in data["users"]:
                if user["username"] == system.user_current:
                    day = len(user["data_day"]) + 1
                    eat = int(input("eat: "))
                    play = int(input("play: "))
                    gas = int(input("gas: "))
                    print(handle.add_day(eat,play,gas,day,data,system.user_current))
            storage.save(data)
        elif choose == "2":
            day = int(input("Input day want to update: "))
            found = any(d["day"] == day for user in data["users"] for d in user["data_day"])
            if not found:
                print("Day not exits")
            else:
                eat = int(input("eat: "))
                play = int(input("play: "))
                gas = int(input("gas: "))
                print(handle.update_day(eat, play, gas, day, data))
        elif choose == "3":
            handle.view_day(data,system.user_current)
        elif choose == "4":
            conti = input("Do you want Delete ??????(Y/N): ")
            if conti == "y":
                day = int(input("Input day want to delete: "))
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
