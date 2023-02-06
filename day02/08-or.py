"""
or
if 条件判断：
    条件满足，执行代码1
    条件满足，执行代码2
else:
    条件不满足，执行1
    条件不满足，执行2

我们在进行条件判断的时候 有可能有多个条件
只要有一个条件满足 条件判断 就为True
只有都不满足 条件判断 就为False
语法：
    条件1  or 条件2

"""
# 需求：
# 1. 定义两个整数变量python_score、c_score，编写代码判断成绩
python_score = 30
c_score = 50
# 2. 要求只要有一门成绩 > 60 分就算合格
if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("都不合格")
