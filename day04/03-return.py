"""
函数的定义

def 函数名(形参1，形参2，...）：
    代码1
    代码2
    ...

函数的调用
函数名(实参1,实参2)

"""
def money(num):
    # num 100  - 20 = 80
    # num * 0.8
    get = num * 0.8
    # 打印 就相当于 一个收据 只是在控制台 打印
    # print(f"我借到了{get} 钱")

    # return 才是将最终的结果 返回给 调用的地方
    # return 回去
    return get

# 调用
# 变量名 = 函数名(实参)
# 我 = 借钱
a = money(100)
print(a)



