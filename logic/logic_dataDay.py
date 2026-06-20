
class handle_day:
    #add
    def add_day(self,eat,play,gas,data,user_current):
        for user in data["users"]:
            if user["username"] == user_current:
                if not user["transactions"]:
                    return "Không có kế hoạch chi tiêu"
                trans = user["transactions"][-1]
                remaining_days = trans["day"] - len(user["data_day"])
                if remaining_days <= 0:
                    return "Không thể thêm ngày mới. Kế hoạch đã đầy."
                user["data_day"].append({
                    "day": len(user["data_day"]) + 1,
                    "eat": eat,
                    "play": play,
                    "gas": gas
                })
                trans_type = trans.get("typpe", "").lower().replace(" ", "_")
                if trans_type == "save_money":
                    calculator_saveMoney(data, user_current)
                elif trans_type == "comfortable":
                    calculator_comfortable(data, user_current)
                elif trans_type == "discipline":
                    calculator_discipline(data, user_current)
                warning(data, user_current)
                evaluate_discipline(data, user_current)
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
                    elif trans_type == "discipline":
                        calculator_discipline(data,user_current)
                    # Hiển thị đánh giá kỷ luật tài chính
                    evaluate_discipline(data,user_current)
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
            remaining_eat = max(0, trans["total_eat"] - spent_eat)
            remaining_play = max(0, trans["total_play"] - spent_play)
            remaining_gas = max(0, trans["total_gas"] - spent_gas)
            print(f"Total_eat: {format_money(remaining_eat)} --> Target_eat: {format_money(remaining_eat / remaining_days)}")
            print(f"Total_play: {format_money(remaining_play)} --> Target_play: {format_money(remaining_play / remaining_days)}")
            print(f"Total_gas: {format_money(remaining_gas)} --> Target_gas: {format_money(remaining_gas / remaining_days)}")
                
def calculator_comfortable(data, user_current):
    for user in data["users"]:
        if user["username"] == user_current and user["transactions"]:
            trans = user["transactions"][-1]
            remaining_days = trans["day"] - len(user["data_day"])
            if remaining_days <= 0:
                print("Hết tháng rồi")
                return
            base_eat = trans["target_eat"]
            base_play = trans["target_play"]
            base_gas = trans["target_gas"]
            spent_eat = sum(d["eat"] for d in user["data_day"])
            spent_play = sum(d["play"] for d in user["data_day"])
            spent_gas = sum(d["gas"] for d in user["data_day"])

            remaining_eat = max(0, trans["total_eat"] - spent_eat)
            remaining_play = max(0, trans["total_play"] - spent_play)
            remaining_gas = max(0, trans["total_gas"] - spent_gas)

            carry_eat = base_eat * len(user["data_day"]) - spent_eat
            carry_play = base_play * len(user["data_day"]) - spent_play
            carry_gas = base_gas * len(user["data_day"]) - spent_gas

            if carry_eat >= 0:
                today_eat = max(0, base_eat + carry_eat / remaining_days)
            else:
                today_eat = max(0, remaining_eat / remaining_days)

            if carry_play >= 0:
                today_play = max(0, base_play + carry_play / remaining_days)
            else:
                today_play = max(0, remaining_play / remaining_days)

            if carry_gas >= 0:
                today_gas = max(0, base_gas + carry_gas / remaining_days)
            else:
                today_gas = max(0, remaining_gas / remaining_days)

            print(f"Target_eat: {format_money(remaining_eat / remaining_days)} --> Tomorrow eat:  {format_money(today_eat)}")
            print(f"Target_play: {format_money(remaining_play / remaining_days)} --> Tomorrow play: {format_money(today_play)}")
            print(f"Target_gas: {format_money(remaining_gas / remaining_days)} -->Tomorrow gas:  {format_money(today_gas)}")

def calculator_discipline(data, user_current):
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
            remaining_eat = max(0, trans["total_eat"] - spent_eat)
            remaining_play = max(0, trans["total_play"] - spent_play)
            remaining_gas = max(0, trans["total_gas"] - spent_gas)
            target_eat = trans["target_eat"]
            target_play = trans["target_play"]
            target_gas = trans["target_gas"]
            print(f"Daily_limit_eat: {format_money(target_eat)} --> Remaining_eat: {format_money(remaining_eat)}")
            print(f"Daily_limit_play: {format_money(target_play)} --> Remaining_play: {format_money(remaining_play)}")
            print(f"Daily_limit_gas: {format_money(target_gas)} --> Remaining_gas: {format_money(remaining_gas)}")

def evaluate_discipline(data, user_current):
    """Đánh giá mức độ kỷ luật tài chính người dùng"""
    for user in data["users"]:
        if user["username"] == user_current and user["transactions"] and user["data_day"]:
            trans = user["transactions"][-1]
            budget_eat = trans["total_eat"]
            budget_play = trans["total_play"]
            budget_gas = trans["total_gas"]
            total_spent_eat = sum(d["eat"] for d in user["data_day"])
            total_spent_play = sum(d["play"] for d in user["data_day"])
            total_spent_gas = sum(d["gas"] for d in user["data_day"])
            # Tính tổng budget và chi tiêu
            total_budget = budget_eat + budget_play + budget_gas
            total_spent = total_spent_eat + total_spent_play + total_spent_gas
            # Tính độ lệch cho mỗi ngày
            day_deviations = []
            days_within_budget = 0
            days_over_budget = 0
            for day_data in user["data_day"]:
                day_total = day_data["eat"] + day_data["play"] + day_data["gas"]
                daily_target = (budget_eat + budget_play + budget_gas) / trans["day"]
                deviation = day_total - daily_target
                
                day_deviations.append({
                    "day": day_data["day"],
                    "spent": day_total,
                    "target": daily_target,
                    "deviation": deviation
                })    
                if deviation <= 0:
                    days_within_budget += 1
                else:
                    days_over_budget += 1
            # Tính streak dài nhất (vượt/trong ngân sách)
            max_over_streak = 0
            max_within_streak = 0
            current_over_streak = 0
            current_within_streak = 0
            for dev in day_deviations:
                if dev["deviation"] > 0:
                    current_over_streak += 1
                    current_within_streak = 0
                    max_over_streak = max(max_over_streak, current_over_streak)
                else:
                    current_within_streak += 1
                    current_over_streak = 0
                    max_within_streak = max(max_within_streak, current_within_streak)
            # Top 3 ngày overspend nhiều nhất
            sorted_deviations = sorted([d for d in day_deviations if d["deviation"] > 0], 
                                      key=lambda x: x["deviation"], reverse=True)[:3]
            # Tính điểm kỷ luật (0-100)
            if total_budget > 0:
                budget_adherence = max(0, 100 * (1 - total_spent / total_budget))
            else:
                budget_adherence = 100  
            
            consistency_score = (days_within_budget / len(user["data_day"]) * 100) if user["data_day"] else 0
            discipline_score = (budget_adherence * 0.6 + consistency_score * 0.4)
            # Đánh giá mức độ
            if discipline_score >= 80:
                rating = "Excellent"
                badge = "[EXCELLENT]"
            elif discipline_score >= 60:
                rating = "Good"
                badge = "[GOOD]"
            elif discipline_score >= 40:
                rating = "Average"
                badge = "[AVERAGE]"
            else:
                rating = "Poor"
                badge = "[POOR]"
            
            # In kết quả
            print("\n" + "="*60)
            print("FINANCIAL DISCIPLINE ASSESSMENT")
            print("="*60)
            print(f"Total Budget: {format_money(total_budget)}")
            print(f"Total Spent: {format_money(total_spent)}")
            remaining_total = max(0, total_budget - total_spent)
            print(f"Remaining: {format_money(remaining_total)}")
            print(f"\nDays Within Budget: {days_within_budget}/{len(user['data_day'])}")
            print(f"Days Over Budget: {days_over_budget}/{len(user['data_day'])}")
            print(f"Longest Over-budget Streak: {max_over_streak} day(s)")
            print(f"Longest Within-budget Streak: {max_within_streak} day(s)")
            
            if sorted_deviations:
                print(f"\nTop Days with Most Overspending:")
                for i, dev in enumerate(sorted_deviations, 1):
                    overspend = dev["spent"] - dev["target"]
                    print(f"  {i}. Day {dev['day']}: Overspent by {format_money(overspend)}")
            
            print(f"\nDiscipline Score: {discipline_score:.1f}/100")
            print(f"Rating: {badge}")
            print("="*60 + "\n")

def warning(data,user_current):
    for user in data["users"]:
        if user["username"] == user_current and user["transactions"]:
            trans = user["transactions"][-1]
            trans_type = trans.get("typpe", "").lower().replace(" ", "_")
            
            if not user["data_day"]:
                return
            
            if trans_type == "discipline":
                # Kiểm tra vượt mức ngày hôm nay
                today = user["data_day"][-1]
                if today["eat"] > trans["target_eat"]:
                    print(f"WARNING: Eat spending {format_money(today['eat'])} exceeds daily limit {format_money(trans['target_eat'])}")
                if today["play"] > trans["target_play"]:
                    print(f"WARNING: Play spending {format_money(today['play'])} exceeds daily limit {format_money(trans['target_play'])}")
                if today["gas"] > trans["target_gas"]:
                    print(f"WARNING: Gas spending {format_money(today['gas'])} exceeds daily limit {format_money(trans['target_gas'])}")
            else:
                # Kiểm tra vượt mức 3 ngày cho save_money và comfortable
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
                    