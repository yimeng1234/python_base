"""
需求：
• 小明 体重 75.0 公斤
• 小明每次 跑步 会减肥 0.5 公斤
• 小明每次 吃东西 体重增加 1 公斤

# 面向过程是没有问题的
name = '小明'
weight = 75.0
def run():
    # 在函数内部，修改全局变量
    global weight
    weight = weight - 0.5
def eat():
    global weight
    weight += 1

run()
print(weight)

# 面向对象 --- 封装
封装 --》 属性和方法 封装到类中
属性 --> 变量
方法 --> 函数

类的设计
类名：     Person
属性：     name,weight
方法：   __init__(self,name,weight)
        __str__ [最后写]
        run() 和 eat()
"""
# 类定义完成
class Person:
    #初始化方法 -- 只要创建一个实例对象，就要设置属性
    #我们修改初始化方法
    def __init__(self,name,weight):
        # 语法 self.属性 = 形参
        self.name = name
        self.weight = weight
    def run(self):
        #在类内部使用属性  self.属性名
        self.weight = self.weight - 0.5
    def eat(self):
        self.weight += 1
    # <__main__.Person object at 0x000002D5CC31D7F0>
    def __str__(self):
        return f'姓名为 {self.name} 体重为 {self.weight}'

# 创建实例化对象
# 语法：  变量名 = 类名（）
# 1. 类名的（） 要对比 __init__ 方法 该方法如果有参数，我们就要传递参数
# 2. weight 不能为 字符串 。因为我们在类内部的方法中 需要进行 +- 运算
xiaoming = Person(name='小明',weight=75.0)
print(xiaoming)
# 调用方法 和 属性
# 方法
# 实例对象变量名.方法名()
xiaoming.run()
xiaoming.run()
# 方式1 看到 体重
print(xiaoming)
# 方式2
# 在类的外部 获取属性值
# 实例对象变量名.属性
print(xiaoming.weight)
# 实例对象变量名.属性 = 新值
# 小明失恋了，体重爆减
xiaoming.weight = 50

print(xiaoming)

