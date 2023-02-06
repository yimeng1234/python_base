"""
1. 创建一个学生类Student
2. 实例属性有姓名name，分数score
3. 每创建一个对象自动实现学生个数累加
    类属性为：num
4. 实现__str__方法，打印对象时，输出：学生姓名:xxx, 考试分数:yyy
5. 设计一个类方法show_num，输出：班级总人数为： xxx
"""
class Student:
    #类属性
    num = 0
    #实例属性
    def __init__(self,name,score):
        self.name = name
        self.score = score
        # 让类属性 num 累加
        Student.num += 1
    def __str__(self):
        return f'学生姓名:{self.name}, 考试分数:{self.score}'
    @classmethod
    def show_num(cls):
        print(f'班级总人数为： {cls.num}')

class Animal:
    pass
