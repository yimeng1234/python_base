"""
类： 抽象的 不能具体使用
对象： 具体的事务。是根据类来创建的

先定义类

然后才能创建对象

猫
类名： Cat
属性： 暂无
方法： eat() 和 drink()
"""
# 先定义类
class Cat:
    def eat(self):
        print("吃鱼")
    def drink(self):
        print("喝水")
# 然后才能创建对象
# 对象变量名 = 类名()
tom = Cat()
# 调用方法
# 语法： 对象变量名.方法名()
tom.eat()
tom.drink()
