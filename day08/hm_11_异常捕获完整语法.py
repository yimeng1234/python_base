"""
try:
    有可能有异常的的代码1
    有可能有异常的的代码2
    ...
except 已知异常类1:
    捕获了 异常类1，执行异常处理
except 已知异常类2：
    捕获了 异常类2，执行异常处理
except Exception as e:
    不知道什么异常 ，执行异常处理
else:
    没有任何异常
finally:
    不管有没有异常，都走这里
"""
try:
    num = int( input("输入数字:") )
except Exception as e:
    # 如果类型转换错误，会走异常处理
    print("输入错误")
else:
    # 没有异常走这里
    # 1 3 5
    if num % 2 == 1:
        #奇数
        print("奇数")
    else:
        #偶数
        print("偶数")
finally:
    print("程序结束")