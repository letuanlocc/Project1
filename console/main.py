from logic.logic_user import UserSystem
from console.mainTypeMoney import manage_money
from logic.logic_utils import JsonStorage

storage = JsonStorage()

def user():
    data = storage.load()
    system = UserSystem() 
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choose = input("Nhập lựa chọn: ") 
        if choose == "1":
            name = input("Nhập Username: ")
            password = input("Nhập Password: ")
            print(system.register(name, password,data))
            storage.save(data)
        elif choose == "2":
            name = input("Nhập Username: ")
            password = input("Nhập Password: ")
            print(system.login(name, password,data))
            storage.save(data)
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