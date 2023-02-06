"""
结论： 函数的 参数 和返回值 传递都是引用信息

"""
# 1. 定义一个函数
def test(num):
    print(f"函数参数的内地址：{id(num)}")

    # 再验证返回值
    result = 666
    print('*'*50)
    print(f'返回值的地址 内：{id(result)}')
    return result

# 2. 调用一个函数
a = 10
# 打印一下a地址
print(f"函数参数的外地址:{id(a)}")
b = test(a)
print(f'返回值的地址 外：{id(b)}')