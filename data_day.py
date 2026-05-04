from utils import load_data, save_data, clear
def data_day(system):
    data = load_data()
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
                if "data_day" not in user:
                    user["data_day"] = []
                if user["username"] == system.user_current:
                    day = len(user["data_day"]) + 1
                    print(f"input data of {day} day ")
                    eat = int(input("eat: "))
                    play = int(input("play: "))
                    gas = int(input("gas: "))
                    user["data_day"].append({
                            "day": day,
                            "eat" : eat,
                            "play" : play,
                            "gas": gas
                        })
                    break
            try: 
                print("SAVE SUCCESS")
                save_data(data)
            except:
                print("ERROR WHEN SAVE")
        else:
            return
        choose_out = input("Do you want continue(Y/N): ")
        if choose_out == "y":
            continue
        else:
            return