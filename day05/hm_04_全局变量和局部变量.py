
# 定义一个变量
a = 100
# 全局变量： 在函数外部定义的变量(没有定义在任何函数内), 所有函数内部都可以使用这个变量

# 定义一个函数
def test():
    # 局部变量： 在函数内部定义的变量, 只能在函数内部使用
    b = 200
    # 在函数内部也可以用 全局变量
    print("内：",a)
    print(b)


# 函数外可以用
print('外：',a)
# 调用
test()

# 在函数外边 使用 b
# print(b)



