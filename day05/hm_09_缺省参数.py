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
# 定义函数的时候，可以给函数的形参 设置一个默认值
# 有默认值的形参，要放在参数位置的最后边
def student_info(name,age,gender='boy'):
    print("姓名是：{},年龄是：{}，性别是{}".format(name,age,gender))
# print()
# [].sort()
# 和尚班
student_info(name='张三',age=20,gender='boy')
student_info('李四',21,'boy')
student_info(name='王五',age=18,gender='boy')
student_info(name='赵六',age=20,gender='boy')
print('*'*30)
# 如果不传递 默认值的参数，形参就使用默认值
student_info(name='tom',age=10)
student_info(name='jack',age=11)
print('#'*30)
# 尼姑班
## 如果传递 ，形参就使用传递的值
student_info(name='小姐姐',age=18,gender='girl')
