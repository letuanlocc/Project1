from user import UserSystem
from manage_money import manage_money
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
user()