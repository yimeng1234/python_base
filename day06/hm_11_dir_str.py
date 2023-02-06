# 定义类
# 先写初始化方法
class Cat:
    # 在创建实例化对象的时候，我们期望，每一个对象，都有name属性
    # 并且给name属性设置初始值
    def __init__(self,name,age=0):
        # self.属性名 = 形参/数据值
        self.name = name
        self.age = age
    def eat(self):
        # self 具体是值 调用的实例对象
        print(f'小猫：{self.name} 今年{self.age}岁了 正在吃大鱼')
    def drink(self):
        print(f'小猫：{self.name} 今年{self.age}岁了 正在和可乐')
    # def __str__(self)   str 前后 个2个 下划线
    # 1. 主要用于 我们调试 打印 实例对象变量名
    # 2. 该方法 必须要有返回值 返回字符串
    # 3. 返回的字符串，会在 打印 实例对象变量的时候 打印。所以就没有必要在 str里打印
    def __str__(self):
        # print(f"name属性是{self.name} age属性是{self.age}")
        return f"name属性是{self.name} age属性是{self.age}"
# 实例化对象
# 实例化对象变量名 = 类名()
# 现在的 init方法 要求我们填写 参数。特别是 name
tom = Cat(name='tom',age=3)
# 变量名.方法名（）
tom.eat()
print('*'*30)
# print()   函数     直接调用
# eat()     方法      对象变量名.方法名（）
# dir  可以查看对象内的所有属性及方法
# dir(对象变量名)      type(), id()
print( dir(tom) )
# __str__
print('$'*30)
# 打印 实例对象变量名
print(  tom )   # 这个变量的name属性是 tom age属性是 3