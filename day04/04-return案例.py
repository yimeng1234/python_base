"""

设计一个函数用于获取两个数中的较大数，数据来自于函数的参数

1. 定义函数  -- 2个形参
2. 根据2个形参 进行大小的比较
3. 返回 较大的数据
4. 调用函数
"""
# 1. 定义函数  -- 2个形参
def get_2_max(num1,num2):
    # 2. 根据2个形参 进行大小的比较
    if num1 > num2:
        # print(num1)
        # num1 大  返回num1
        return num1
    elif num1 == num2:
        # 相等  返回谁都可以
        # print(num1)
        return num1
    else:
        # 否则就是 num2 大
        # print(num2)
        return num2
    #函数里
    # return 一旦 执行 后边的代码 就不在执行了
    print('over')


# 4. 调用函数
result = get_2_max(10,20)
print(result)