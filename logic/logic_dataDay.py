
class handle_day:
    #add
    def add_day(self,eat,play,gas,data,user_current):
        for user in data["users"]:
            if user["username"] == user_current:
                if not user["transactions"]:
                    return "Không có kế hoạch chi tiêu"
                user["data_day"].append({
                    "day": len(user["data_day"]) + 1,
                    "eat": eat,
                    "play": play,
                    "gas": gas
                })
                trans = user["transactions"][-1]
                trans_type = trans.get("typpe", "").lower().replace(" ", "_")
                if trans_type == "save_money":
                    calculator_saveMoney(data, user_current)
                elif trans_type == "comfortable":
                    calculator_comfortable(data, user_current)
                warning(data, user_current)
        return "ADD SUCCESSFUL"
    #update
    def update_day(self,eat,play,gas,day,data,user_current):
        for user in data["users"]:
            if user["username"] == user_current:
                for d in user["data_day"]:
                    if d["day"] == day:
                        d["eat"] = eat
                        d["play"] = play
                        d["gas"] = gas
        return "UPDATE SUCCESSFUL"
    #view
    def view_day(self,data,user_current):
        for user in data["users"]:
            if user["username"] == user_current:
                for d in user["data_day"]:
                    print(f"Day: {d['day']}: Eat: {format_money(d['eat'])}, Play: {format_money(d['play'])}, Gas: {format_money(d['gas'])}")
                print("Remaining Amount:")
                if user["transactions"]:
                    trans = user["transactions"][-1]
                    trans_type = trans.get("typpe", "").lower().replace(" ", "_")
                    if trans_type == "save_money":
                        calculator_saveMoney(data,user_current)
                    elif trans_type == "comfortable":
                        calculator_comfortable(data,user_current)
    #delete
    def delete_day(self,day,data,user_current):
        for user in data["users"]:
            if user["username"] == user_current:
                user["data_day"] = [d for d in user["data_day"] if d["day"] != day] #delete
                for index, d in enumerate(user["data_day"]):
                    d["day"] = index + 1
        return "DELETE SUCCESSFUL"
#format
def format_money(money):
    return f"{money:,.0f}".replace(",", ".") + " VND"
#calcu
def calculator_saveMoney(data, user_current):
    for user in data["users"]:
        if user["username"] == user_current and user["transactions"]:
            trans = user["transactions"][-1]
            remaining_days = trans["day"] - len(user["data_day"])
            if remaining_days <= 0:
                print("Hết tháng rồi")
                return
            spent_eat = sum(d["eat"] for d in user["data_day"])
            spent_play = sum(d["play"] for d in user["data_day"])
            spent_gas = sum(d["gas"] for d in user["data_day"])
            print(f"Total_eat: {format_money(trans['total_eat'] - spent_eat)} --> Target_eat: {format_money((trans['total_eat'] - spent_eat) / remaining_days)}")
            print(f"Total_play: {format_money(trans['total_play'] - spent_play)} --> Target_play: {format_money((trans['total_play'] - spent_play) / remaining_days)}")
            print(f"Total_gas: {format_money(trans['total_gas'] - spent_gas)} --> Target_gas: {format_money((trans['total_gas'] - spent_gas) / remaining_days)}")
                
def calculator_comfortable(data, user_current):
    for user in data["users"]:
        if user["username"] == user_current:
            for trans in user["transactions"]:
                remaining_days = trans["day"] - len(user["data_day"])
                if remaining_days <= 0:
                    print("Hết tháng rồi")
                    return
                base_eat  = trans["target_eat"]
                base_play = trans["target_play"]
                base_gas  = trans["target_gas"]
                #tổng tiền đã tiêu của các khoản
                spent_eat  = sum(d["eat"]  for d in user["data_day"])
                spent_play = sum(d["play"] for d in user["data_day"])
                spent_gas  = sum(d["gas"]  for d in user["data_day"])
                
                carry_eat  = base_eat  * len(user["data_day"]) - spent_eat
                carry_play = base_play * len(user["data_day"]) - spent_play
                carry_gas  = base_gas  * len(user["data_day"]) - spent_gas

                today_eat  = (base_eat  + carry_eat)  if carry_eat  >= 0 else (trans["total_eat"]  - spent_eat)  / remaining_days
                today_play = (base_play + carry_play) if carry_play >= 0 else (trans["total_play"] - spent_play) / remaining_days
                today_gas  = (base_gas  + carry_gas)  if carry_gas  >= 0 else (trans["total_gas"]  - spent_gas)  / remaining_days

                print(f"Target_eat: {format_money((trans['total_eat'] - spent_eat) / remaining_days)} --> Tomorrow eat:  {format_money(today_eat)}")
                print(f"Target_play: {format_money((trans['total_play'] - spent_play) / remaining_days)} --> Tomorrow play: {format_money(today_play)}")
                print(f"Target_gas: {format_money((trans['total_gas'] - spent_gas) / remaining_days)} -->Tomorrow gas:  {format_money(today_gas)}")
                
def warning(data,user_current):
    for user in data["users"]:
        if user["username"] == user_current and user["transactions"]:
            trans = user["transactions"][-1]
            check_eat = trans["target_eat"] * 3
            check_play = trans["target_play"] * 3
            check_gas = trans["target_gas"] * 3
            spent_eat = sum(d["eat"] for d in user["data_day"][-3:])
            spent_play = sum(d["play"] for d in user["data_day"][-3:])
            spent_gas = sum(d["gas"] for d in user["data_day"][-3:])
            if spent_eat > check_eat:
                print("Spending more than the limit (eat) !!!!")
            if spent_play > check_play:
                print("Spending more than the limit (play) !!!!")
            if spent_gas > check_gas:
                print("Spending more than the limit (gas) !!!!")
    return
                    