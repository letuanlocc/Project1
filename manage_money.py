from utils import load_data, save_data, clear
from data import data_money
from data_day import data_day
def manage_money(system):
    clear()
    data = load_data()
    datas = data_money()
    for user in data["users"]:
        if user["username"] == system.user_current:
            user.setdefault("transactions", [])
            user.setdefault("data_day", [])
            if user["transactions"]:
                return datas.handle_type_money(system.user_current,data), data_day(system)
            else:
                while True:
                    print(f"Welcome {system.user_current} to demo mange monney ")
                    print("1. Save money")
                    print("2. Comfortable")
                    print("3. Exit")
                    choose = input("Nhập lựa chọn: ")
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
                                    datas.save_money(total, day, system.user_current,data)
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