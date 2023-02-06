"""
函数嵌套调用：一个函数里面又调用了另外一个函数
"""
# 定义一个函数
def test1():
    print("雪下的那么深11111")

# 定义第二个函数
def test2():
    print("start~~~~")

    #调用另外一个函数
    test1()

    print("end~~~~~~")

#调用
test2()
