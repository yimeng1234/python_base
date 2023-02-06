# 定义一个 动物类
"""
类名： Animal
属性： 暂无
方法： eat() drink() sleep() run()
"""
class Animal:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")
    def sleep(self):
        print("sleep")
    def run(self):
        print("run")
# 定义一个 狗类 -- 狗类继承自动物类
"""
继承的语法：
class 子类类名(父类):
    pass
"""
class Dog(Animal):
    def bark(self):
        print("冰墩墩")

# 对象
d = Dog()
d.run()
d.sleep()
d.bark()