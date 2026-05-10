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
        print("4. Update day")
        print("5. Delete day")
        print("5. Exit")
        choose = input("Nhập lựa chọn: ")
        if choose == "1":
            for user in data["users"]:
                # if "data_day" not in user:
                #     user["data_day"] = []
                if user["username"] == system.user_current:
                    eat = int(input("eat: "))
                    play = int(input("play: "))
                    gas = int(input("gas: "))
                    print("thanks for add")
        else:
            return
        choose_out = input("Do you want continue(Y/N): ")
        if choose_out == "y":
            continue
        else:
            return
        
def format_money(money):
    return f"{money:,.0f}".replace(",", ".") + " VND"


                    # day = len(user["data_day"]) + 1
                    # print(f"input data of {day} day ")
                    # eat = int(input("eat: "))
                    # play = int(input("play: "))
                    # gas = int(input("gas: "))
                    # user["data_day"].append({
                    #         "day": day,
                    #         "eat" : eat,
                    #         "play" : play,
                    #         "gas": gas
                    #     })
                    # for trans in user["transactions"]:
                    #     remaining_days = trans["day"] - len(user["data_day"])
                    #     spent_eat = sum(d["eat"] for d in user["data_day"])
                    #     spent_play = sum(d["play"] for d in user["data_day"])
                    #     spent_gas = sum(d["gas"] for d in user["data_day"])
                    #     print(f"Total_eat: {format_money(trans["total_eat"] - spent_eat)} -->Target_eat: {format_money((trans["total_eat"] - spent_eat) / remaining_days )}")
                    #     print(f"Total_play: {format_money(trans["total_play"] - spent_play)} -->Target_play: {format_money((trans["total_play"] - spent_play) / remaining_days )}")
                    #     print(f"Total_gas: {format_money(trans["total_gas"] - spent_gas)} -->Target_gas: {format_money((trans["total_gas"] - spent_gas) / remaining_days )}")
                    # break
            # try: 
            #     print("SAVE SUCCESS")
            #     storage.save(data)
            # except:
            #     print("ERROR WHEN SAVE")