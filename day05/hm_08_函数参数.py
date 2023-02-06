"""
# 1. 定义
def 函数名(形参1，形参2,...）：
    代码1
    代码2
    ...

2. 使用
函数名(实参1，实参2,...)
"""
# 定义一个函数，输入 学生的姓名，年龄，性别，然后格式化输出
def student_info(name,age,gender):
    print(f'姓名是:{name},年龄是:{age},性别是:{gender}')

# 使用
# 位置参数 -- 就是按照 形参的顺序 一个一个传入
# 缺点： 一旦 对应关系没有搞对，数据就错乱了
student_info('tom',20,'boy')
print('*'*30)
student_info(20,'boy','tom')

# 关键字参数  -- 根据 形参的名字 来赋值
# 语法： 形参 = 数据值
student_info(name='rose',gender='girl',age=18)

# 位置参数可以和关键字参数 混用
print('#'*30)
# 位置参数在前，关键字参数在后
student_info('jerry',gender='girl',age=20)

# 一旦你使用了关键字，后续 必须用 关键字
# student_info(name='lili',60,'girl')