
# 定义类
class Cat(object):
    def eat(self):
        # self 英文含义 就是 自己
        # 哪个 实例对象 调用了这个方法  self就是谁
        # self ==> tom
        # 使用数据的时候
        # self.属性名
        print(f" {self.name} 吃鱼")
    def drink(self):
        print(f"{self.name}喝水")
# 创建对象
# 语法： 变量名 = 类名（）
tom = Cat()
# 在调用 eat（） 前边 写一行代码
# 实例对象变量名.属性 = 数据值
tom.name = 'tom'
# 调用方法
# 实例对象变量名.方法名（）
tom.eat()
tom.drink()
