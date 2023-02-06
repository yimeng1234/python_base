"""
需求:
1. 定义函数 login_front 实现前台系统登录
2. 定义函数 login_back 实现后台登录
3. 要求使用同样的变量名, 分别记录前后台登录信息中的账号和密码

"""
def login_front():
    # 函数内部定义变量
    username = '13312345678'
    password = 'abcdef'
    print(f'账号是{username},密码是{password}')

def login_back():
    #函数内部定义的变量
    username = 'admin'
    password = 'admin'
    print('账号是{},密码是{}'.format(username,password))

if __name__ == '__main__':
    login_front()
    login_back()
