
from logic.logic_utils import  JsonStorage  

#Xử lý format
def format_money(money):
    return f"{money:,.0f}".replace(",", ".") + " VND"

def save_money_rule(total,day):
    rule = {"eat": 0.7, "play": 0.1, "gas": 0.2}
    total_eat = total * rule["eat"]
    total_play = total * rule["play"]
    total_gas = total * rule["gas"]    
    return total_eat, total_play, total_gas, rule

def cft_money_rule():
    pass

#Xử lý phương thức chọn của người dùng
class handle_type:
    
    def save_type(self,type_manage, total_money, total_day, user_current,data):
        if type_manage == "save_money":
            for user in data["users"]:
                if user["username"] == user_current:
                    total_eat, total_play, total_gas, rule = save_money_rule(total_money,total_day)
                    user["ratio"] = rule
                    if user["data_day"] == []: #kiểm tra có phải lần đầu tiên đăng nhập không
                        user["transactions"].append({
                            "typpe": "Save Money",
                            "total" : total_money,
                            "day": total_day,
                            "total_eat": (total_eat),
                            "total_play": (total_play),
                            "total_gas": (total_gas),
                            "target_eat": (total_eat) / total_day,
                            "target_play": (total_play) / total_day,
                            "target_gas": (total_gas) / total_day
                    }) 
                    self.show_info(data,user_current)
        else:
            pass
    
    def show_info(self,data,user_current):
        for user in data["users"]:
            if user["username"] == user_current:
                for target in user["transactions"]:
                    print("target_Eat:", format_money(target["target_eat"]))
                    print("target_Play:", format_money(target["target_play"]))
                    print("target_Gas:", format_money(target["target_gas"]))
                    print("-------------------------------------")
                    
