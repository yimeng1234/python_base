"""
先演示问题
"""
# 定义类
class Cat(object):
    # 我们在创建对象的时候【变量名=类名()】
    # 系统会自动调用 def __init__(self) 这个方法       是两个连续的下划线
    def __init__(self):
        # self.属性名 = 值
        self.name = ''
    def eat(self):
        print(f'{self.name} 吃鱼')
    def drink(self):
        print(f"{self.name} 喝水")
# 创建对象1  -- name
# 变量名 = 类名()
tom = Cat()
#添加一个属性 name
tom.name = 'tom'
#调用方法
tom.eat()
tom.drink()

# 创建对象2  -- 没有设置
jack = Cat()
# jack.name = ''
#没有给jack设置name属性
# 调用方法就报错了
# 期望 在创建对象的时候 给name 一个默认值
# 这样我们的程序 至少不会报错
jack.eat()