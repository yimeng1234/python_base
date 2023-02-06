# 定义一个函数 来计算2个数的和
"""
定义
def 函数名():
    代码1
    代码2

调用
函数名()
"""
# 1. 定义函数
"""
def 函数名(参数1，参数2，...):
    代码1
    代码2
"""
def get_2_sum(num1,num2):
    """函数的文档注释: 用于 计算2个数的和 """
    # pass 的作用是 用于 维护代码结构。 里边的代码我稍后写
    # 先不要报语法错误
    # 定义了2个数
    # num1 = 10
    # num2 = 20
    # 求和
    # total 英语 总共 总计
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
# 2. 函数调用
# 函数名(数据1，数据2)
# 张三
get_2_sum(10,20)
# 李四  100 200
get_2_sum(100,200)


"""
函数 使用步骤分为2步：

1. 定义
def 函数名(形参1，形参2，...):
    代码1
    代码2

2. 使用
函数名(实参1，实参2，...)

"""