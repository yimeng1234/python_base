# 全局变量
num = 100

def test1():
    """重新修改一下num的值"""
    # global 全局变量名
    # 全局变量名 = 新的值
    global num
    # num = 666 属于 局部变量
    # 升级为 全局变量
    num = 666
    print("test1:",num)

def test2():

    print("test2:",num)

test1()
print('*'*10)
test2()