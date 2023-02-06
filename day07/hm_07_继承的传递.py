
# 动物类       基类   父类
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")
# 猫类                子类
class Cat(Animal):
    # 初始化方法和 吃 睡 方法都不用再写了。因为继承父类了
    def catch(self):
        print("抓老鼠")
# 狗类                子类
class Dog(Animal):
    #初始化方法和 吃 睡 方法都不用再写了。因为继承父类了
    def look_door(self):
        print("看门")
# 哮天犬类             孙类
class XiaoTianDog(Dog):
    def fly(self):
        print("天上飞")

# 创建一个 哮天犬 对象
# xtq = XiaoTianDog() #  错误的
xtq = XiaoTianDog(name='哮天犬',age=600) # 正确的
# 因为 继承关系 父类的父类中 有初始化方法。
# 我们需要按照 父类的父类的初始化方法创建对象
xtq.fly()
xtq.look_door()
xtq.eat()
xtq.sleep()




