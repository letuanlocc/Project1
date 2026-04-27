from user import UserSystem
import os
def user():
    system = UserSystem() 
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choose = input("Nhập lựa chọn: ") 
        if choose == "1":
            name = input("Nhập Username: ")
            password = input("Nhập Password: ")
            print(system.register(name, password))
        elif choose == "2":
            name = input("Nhập Username: ")
            password = input("Nhập Password: ")
            print(system.login(name, password))
        else:
            return
        if system.user_current is None:
            print("Chưa đăng nhập")
        else:
            print("Đã Đăng nhập")
            print("-----------------------------------------------------")
            return manage_money(system)
        choose_out = input("Do you want continue(Y/N): ")
        if choose_out == "y":
            continue
        else:
            return
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def manage_money(system):
    clear()
    while True:
        print(f"Welcome {system.user_current} to demo mange monney ")
        print("1. Save money")
        print("2. Comfortable")
        print("3. Exit")
        choose = input("Nhập lựa chọn: ")
        if choose == "1":
            print("Was Choose save money")
        elif choose == "2":
            print("Was Choose Comfortable money")
        else:
            return
        choose_out = input("Do you want continue(Y/N): ")
        if choose_out == "y":
            continue
        else:
            return
user()