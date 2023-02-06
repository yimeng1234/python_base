"""
1. 回顾 对象属性【实例属性】    实例对象 其实就是对象
class Person:
    def __init__（self,name,age）:
        self.name = name
        self.age = age
xiaoming = Person(name='小明',age=18)
print(xiaoming.name)
xiaomei = Person(name='小美',age=19)
print(xiaomei.name)
① 对象属性 其实就是 Person 中的 name和age
② 对象属性在类的内部 通过 self.属性 调用
③ 对象属性在类的外部 通过 对象变量名.属性 调用
④ 针对于 对象属性。他们的属性是各自独立的

2. 类属性【类对象属性】
class Tool:
    count = 0   # 类属性
    def __init__(self,name):
        self.name = name
① count 是类属性。 它是在 类中 ，类的方法外边 定义的
② 针对于 类属性。 它是共享的，只有一份
③ 类属性的访问 推荐使用 类名.类属性
"""

# 知道使用这个类，创建了多少个工具对象
class Tool:
    # 定义一个类属性
    count = 0

    def __init__(self,name):
        self.name = name
        # +1
        # 类属性的访问
        # 推荐使用 类名.类属性
        Tool.count += 1
# 工具对象
one = Tool(name='铁锹')
# 类属性的访问
# 推荐使用 类名.类属性
print(Tool.count)

two = Tool(name='板子')
print(Tool.count)
