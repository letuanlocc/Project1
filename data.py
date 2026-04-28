import json
import os
class data_money:
    def __init__(self, file="data.json"):
        self.file = file
        self.user_current = None
    def load_data(self):
        with open(self.file, "r") as f:
            return json.load(f)
    def save_data(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
    def handle_type_money(self,current_user,data):
        for user in data["users"]:
            if user["username"] == current_user:
                for trans in user["transactions"]:
                    if trans["type"] == "Save Money":
                        result = self.save_money(
                            trans["total"],
                            trans["day"]
                        )
                        print("User:", user["username"])
                        print("total_Eat:", self.format_money(result["total_eat"]), "->", self.format_money(result["target_eat"]))
                        print("total_Play:", self.format_money(result["total_play"]),"->", self.format_money(result["target_play"]))
                        print("total_Gas:", self.format_money(result["total_gas"]),"->", self.format_money(result["target_gas"]))
                        print("-------------------------------------")
                    break 
                return
    def format_money(self,money):
        return f"{money:,.0f}".replace(",", ".") + " VND"
    def save_money(self, total_money, total_day):
        return {
            "total_eat": (total_money * 0.7),
            "total_play": (total_money * 0.1),
            "total_gas": (total_money * 0.2),
            "target_eat": (total_money * 0.7) / total_day,
            "target_play": (total_money * 0.1) / total_day,
            "target_gas": (total_money * 0.2) / total_day
        }
# def main():
#     datas = data()
#     print(datas.save_money(3000000,80000,35000,0,30))
#     datas.handle_type_money
# main()