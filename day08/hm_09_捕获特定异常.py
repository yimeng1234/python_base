"""
异常 有很多情况的
我们可以针对于 不同的异常 做不同的处理
try:
    有可能有异常的代码1
    有可能有异常的代码2
    ...
except 异常类名1：
    针对于指定异常的处理
except 异常类名2：
    针对于指定异常的处理

类似于
except 感冒：
    吃感冒药
except 发烧：
    吃退烧药
"""
# 1.  # ValueError
# name = 'itcast'
# int(name)

# 2. # ZeroDivisionError
# num1=100
# num2=0
# result = num1 / num2
# print(result)
try:
    num1 = 100
    num2 = 'a'
    print( num1 / num2)
except (ValueError,TypeError):
    print("数据值错误或者类型错误")
except ZeroDivisionError:
    print("0不能做除数")
# except TypeError:
#     print("类型错误")
