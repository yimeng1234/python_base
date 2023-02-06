# 动物类
class Animal:
    def eat(self):
        print("父类：吃")
# 猫类
class Cat(Animal):
    # 写和父类 同名的方法
    def eat(self):
        # 先调用父类的方法
        # super() 通用写法
        # super() 代表 父类
        super().eat()
        # 然后再调用 自己的代码
        print("子类：吃鱼 吃大鱼 吃鲨鱼")

# 创建猫的对象
c = Cat()
c.eat()