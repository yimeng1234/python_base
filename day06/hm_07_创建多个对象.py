"""
面向对象 --》 核心【类和对象】 --》 类是抽象的 对象是具体的
先定义类，再创建对象

定义类
class 类名：
    def 方法名（self,形参1，形参2...):
        pass

类名： Cat
属性： 暂无
方法： eat() 和 drink()

"""
class Cat:
    def eat(self):
        print("吃鱼")

    def drink(self):
        print("喝水")

#创建实例对象
# 1.第一个对象
tom = Cat()
tom.eat()

print('*'*30)
#2. 第二个对象
# 变量名 = 类名（）
jack = Cat()
jack.drink()

print('!'*30)
# id(变量名) 打印 内存地址
print( id(tom) )
print( id(jack) )
