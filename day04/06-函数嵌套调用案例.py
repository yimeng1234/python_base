"""
需求:
1. 定义名为 input_username 的函数, 获取用户输入的用户名
2. 定义名为 input_password 的函数, 获取用户输入的密码
3. 定义名为 login 的函数, 判断获取的用户名和密码信息
4. 要求当获取的用户名为:admin 并且密码为: 123456 时, 输出“登录成功!”，否则提示“用户名或密码错误!”
"""
# 需求:
# 1. 定义名为 input_username 的函数, 获取用户输入的用户名
def input_username():
    # 字符串变量名 = input(提示信息)
    username = input("请输入用户名:")
    # print(username)
    # 因为在login的函数里，需要得到 username
    # 所以 应该在函数执行完的地方 携带 信息
    return username
# 2. 定义名为 input_password 的函数, 获取用户输入的密码
def input_password():
    password = input("请输入密码:")
    return password


# 3. 定义名为 login 的函数, 判断获取的用户名和密码信息
def login():
    # 3.1 获取用户名
    # 变量名 = 函数名()
    user = input_username()
    print(user)
    # 3.2 获取密码信息
    pwd = input_password()
    # 4. 判断
    # 4. 要求当获取的用户名为:admin 并且密码为: 123456 时, 输出“登录成功!”，否则提示“用户名或密码错误!”
    if user == 'admin' and pwd == '123456':
        print("登录成功!")
    else:
        print("用户名或密码错误!")
#调用
login()
