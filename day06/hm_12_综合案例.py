"""
# 1. 按要求设计类
# 2. 实例化苹果对象apple、橘子对象orange，不同对象，属性不一样
#	 名字：苹果，颜色：红色，价格：5，
#    名字：橘子，颜色：橙色，价格：3
# 3. 打印对象名，显示其属性信息

1. 类的设计
类名： 水果类 Fruit
属性：  名字，颜色和价格       name,color,price
方法：  __init__ 初始化方法
       __str__ 打印对象
2. 定义类
3. 创建实例化对象
4. 打印实例化对象
"""
# 定义类
class Fruit:
    #初始化方法
    def __init__(self,name,color,price=10):
        # self.属性名 = 形参
        self.name = name
        self.color = color
        self.price = price

    # 打印 对象名的时候 显示一些属性信息
    def __str__(self):
        # 必须返回 字符串
        return f"这个水果是{self.name} 颜色是{self.color} 价格是{self.price}"

# 创建对象
# 实例对象变量名 = 类名(实参,...)
apple = Fruit(name='苹果',color="红色",price=5)

# 过了2天 价格下降了
# 修改属性值
apple.price = 3
# 打印属性值
print(apple.price)
# 打印 对象
print(apple)

# 第二个对象
orange = Fruit(name='橘子',color="橙色",price=3)
print(orange)
