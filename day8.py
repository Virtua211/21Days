class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = {}

def register():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    confirm_password = input("确认密码: ")

    if password != confirm_password:
        print("密码不一致，请重试！")
        return

    if username in users:
        print("用户名已被注册，请重试！")
        return

    users[username] = User(username, password)
    print("注册成功!")

while True:
    print("欢迎使用用户注册系统")
    print("1. 注册")
    print("2. 退出")

    choice = int(input("请选择: "))

    if choice == 1:
        register()
    elif choice == 2:
        break
    else:
        print("无效，请重试！")
