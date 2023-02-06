"""
类的定义 三种形式
1.
class 类名：
    方法
2. 为了以后 继承使用
 object 是固定的单词
class 类名(object):
    方法
3.  了解 -- 不推荐这么写
class 类名():
    方法
猫
类名： Cat
属性： 暂无
方法： eat() 和 drink()
"""



# class Cat:
# class Cat(object):
class Cat():
    def eat(self):
        print("吃鱼")
    def drink(self):
        print("喝水")

# 创建实例对象
# 变量名 = 类名（）
tom = Cat()
# 调用方法
# 对象变量名.方法名（）
tom.eat()
tom.drink()
# 作业。 分析 自己身边的 事务。
# 选择 2 3个 进行类的设计
# 设计完成 定义类 【类里只定义方法】