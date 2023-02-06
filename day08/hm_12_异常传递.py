# 函数1
def demo1():
    num1 = 100
    num2 = 0
    # 异常 一旦抛出
    # 当前后续的代码不再执行
    print( num1 / num2)
    print('11111')
# 函数2
def demo2():
    print('start')
    try:
        demo1()
    except:
        print('22222')
    print('end')
# 调用函数
demo2()