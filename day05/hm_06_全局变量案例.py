# 全局变量 就是在 非函数内部定义的变量。 供全局使用

num = 100

def test1():

    # 定义了一个 和全局变量 同名的 局部变量
    num = "今天情人节，明天元宵节"
    print(num)

def test2():
    print(num)

if __name__ == '__main__':
    test1()
    test2()