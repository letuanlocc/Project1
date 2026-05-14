from logic.logic_utils import JsonStorage, clear
from logic.logic_saveData import handle_type
from console.mainDay import data_day

storage = JsonStorage() #khởi tạo

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
                    print("3. Exit")
                    choose = input("Nhập lựa chọn: ")
                    if choose == "1":
                        total = int(input("Total money: "))
                        day = int(input("Day: "))
                        handle.save_type("save_money",total,day,system.user_current,data)
                        storage.save(data)
                    elif choose == "2":
                        pass
                    else:
                        return
                    choose_out = input("Do you want continue (Y/N): ")
                    if choose_out == "y":
                        return data_day(system) 
                    else:
                        return