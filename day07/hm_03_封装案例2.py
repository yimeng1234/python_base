"""
需求：
• 进入某 Web 项目登录页面，输入用户名、密码、验证码之后登录系统
要求：
• 模拟实现登录操作，输出每一步的登录信息

面向过程
变量
username = ''
password = ''
verify_code = ''
函数
def login():
    print(用户名是)
    print(密码是)

面向对象 -- 封装
封装 就是把 属性 和 方法 封装到类中

类三要素
类名： LoginPage
属性： username,password,verify_code
方法： login()
      __init__()   和 __str__

"""
class LoginPage:
    # 在初始化的时候，需要填写 三个信息
    # 用户名，密码和验证码
    def __init__(self,username,password,verify_code):
        # 在类的内部 通过使用 self.属性 = 形参
        self.username = username
        self.password = password
        self.verify_code = verify_code
    def __str__(self):
        return "用户名为{} 密码为{} 验证码为{}".format(self.username,
                                            self.password,
                                            self.verify_code)
    def login(self):
        # 把用户名，密码和验证码打印一下就可以
        print(f'用户名为{self.username}')
        print(f'密码为{self.password}')
        print(f'验证码为{self.verify_code}')
        print("登录成功")

if __name__ == '__main__':
    # 创建实例对象
    xiaoming = LoginPage(username='admin',
                         password='123456',
                         verify_code=666777)
    # 调用方法
    xiaoming.login()

    # 再创建一个实例对象
    xiaomei = LoginPage(username='abc',
                        password='xyz',
                        verify_code=123456)
    xiaomei.login()
