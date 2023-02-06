
#定义函数
"""
def 函数名(形参1，形参2,...)：
    代码1
    代码2
    ...

函数名(实参1，实参2,...)
"""
def login(username,password,code):
    # （用户名：admin、密码：123456、验证码：8888
    # 注意数据类型： 如果数据类型不一致 也不相等
    if username == 'admin' and password == '123456' and code == 8888:
        print("登录成功")
    elif username != 'admin' and password == '123456' and code == 8888:
        print("用户名不正确")
    elif username == 'admin' and password != '123456' and code == 8888:
        print("密码不正确")
    elif username == 'admin' and password == '123456' and code != 8888:
        print("验证码不正确")
    else:
        print("输入的什么数据啊")

if __name__ == '__main__':
    # 我就想 自己单独运行这个模块，测试一下代码
    # 别的模块 引入 login_service.py 的时候 不会走 if
    login('admin','123456',8888)