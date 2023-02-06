"""
try:
    有可能出现异常的代码1
    有可能出现异常的代码2
    ...
except Exception as e:
    异常走这里
e 其实就是捕获的那个异常
就类似于 我们用老鼠夹 夹老鼠  夹住的就是 那个老鼠
捕获的 就是异常
"""
# as 就是起别名
# import random as r
# print( r.randint(1,10) )
try:
    # num1 = 100
    # num2 = 0
    # print( num1 / num2 )
    int( 'aaaa' )
except Exception as e:
    # Exception 必须这么写
    # Exception 相当于  形参 代表着异常
    # as e 就是起别名
    print(e)